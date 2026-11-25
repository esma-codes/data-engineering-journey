from pathlib import Path
import csv
import logging
import time


# 1. File paths

BASE_DIR = Path(__file__).resolve().parent

RAW_FILE = BASE_DIR / "data" / "raw" / "nyc_311_10000.csv"
CLEAN_FILE = BASE_DIR / "data" / "processed" / "cleaned.csv"
REJECTED_FILE = BASE_DIR / "data" / "processed" / "rejected.csv"
LOG_FILE = BASE_DIR / "logs" / "pipeline.log"

TEMP_CLEAN_FILE = CLEAN_FILE.with_suffix(".csv.tmp")
TEMP_REJECTED_FILE = REJECTED_FILE.with_suffix(".csv.tmp")


# 2. Create required directories

CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


# 3. Required columns

REQUIRED_COLUMNS = {
    "unique_key",
    "created_date",
    "borough",
    "incident_zip",
    "status",
    "closed_date"
}


# 4. Logging configuration

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

start_time = time.perf_counter()

logging.info("NYC 311 pipeline started.")


try:

    # 5. Extract

    with (
        open(RAW_FILE, "r", encoding="utf-8", newline="") as file,
        open(TEMP_CLEAN_FILE, "w", encoding="utf-8", newline="") as clean_file,
        open(TEMP_REJECTED_FILE, "w", encoding="utf-8", newline="") as rejected_file
    ):

        logging.info("Input CSV opened successfully.")

        reader = csv.DictReader(file)

        fieldnames = reader.fieldnames


        # 6. Schema validation

        actual_columns = set(fieldnames or [])

        missing_columns = REQUIRED_COLUMNS - actual_columns

        if missing_columns:
            logging.error(
                "Missing required columns: %s",
                missing_columns
            )

            raise ValueError("CSV schema validation failed.")

        logging.info("Schema validation passed.")


        # 7. CSV writers

        clean_writer = csv.DictWriter(
            clean_file,
            fieldnames=fieldnames
        )

        rejected_writer = csv.DictWriter(
            rejected_file,
            fieldnames=fieldnames
        )

        clean_writer.writeheader()
        rejected_writer.writeheader()


        # 8. Counters

        row_count = 0

        missing_unique_key = 0
        missing_created_date = 0
        missing_borough = 0
        missing_zip = 0
        closed_without_date = 0

        valid_count = 0
        invalid_count = 0


        # 9. Transform and data quality validation

        for row in reader:

            row_count += 1

            unique_key = row["unique_key"].strip()
            created_date = row["created_date"].strip()
            borough = row["borough"].strip()
            incident_zip = row["incident_zip"].strip()
            status = row["status"].strip()
            closed_date = row["closed_date"].strip()


            if unique_key == "":
                missing_unique_key += 1

            if created_date == "":
                missing_created_date += 1

            if borough == "":
                missing_borough += 1

            if incident_zip == "":
                missing_zip += 1

            if status == "Closed" and closed_date == "":
                closed_without_date += 1


            # 10. Load into temporary files

            if unique_key == "" or created_date == "":

                rejected_writer.writerow(row)
                invalid_count += 1

            else:

                clean_writer.writerow(row)
                valid_count += 1


        # 11. Summary logs

        logging.info("Processed %s rows.", row_count)

        logging.info("Missing unique_key: %s", missing_unique_key)

        logging.info("Missing created_date: %s", missing_created_date)

        logging.info("Missing borough: %s", missing_borough)

        logging.info("Missing incident_zip: %s", missing_zip)

        logging.info("Closed without closed_date: %s", closed_without_date)

        logging.info("Valid records: %s", valid_count)

        logging.info("Invalid records: %s", invalid_count)


        # 12. Data reconciliation

        if row_count != valid_count + invalid_count:

            logging.error("Data reconciliation failed.")

            raise ValueError("Record count mismatch.")

        else:

            logging.info("Data reconciliation passed.")


        # 13. Warning logs

        if missing_borough > 0:

            logging.warning(
                "Found %s rows with missing borough.",
                missing_borough
            )

        if missing_zip > 0:

            logging.warning(
                "Found %s rows with missing incident ZIP.",
                missing_zip
            )

        if closed_without_date > 0:

            logging.warning(
                "Found %s closed requests without a closed_date.",
                closed_without_date
            )


        # 14. Error logs

        if missing_unique_key > 0:

            logging.error(
                "Found %s rows with missing unique_key.",
                missing_unique_key
            )

        if missing_created_date > 0:

            logging.error(
                "Found %s rows with missing created_date.",
                missing_created_date
            )


    # 15. Atomic file replacement

    TEMP_CLEAN_FILE.replace(CLEAN_FILE)

    TEMP_REJECTED_FILE.replace(REJECTED_FILE)

    logging.info("Valid records saved to %s", CLEAN_FILE)

    logging.info("Invalid records saved to %s", REJECTED_FILE)


# 16. Exception handling

except FileNotFoundError as error:

    logging.error(
        "Required file or directory not found: %s",
        error
    )

    raise


# 17. Successful completion and execution time

else:

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    logging.info(
        "Execution time: %.3f seconds.",
        execution_time
    )

    logging.info("NYC 311 pipeline finished successfully.")

finally:

    TEMP_CLEAN_FILE.unlink(missing_ok=True)

    TEMP_REJECTED_FILE.unlink(missing_ok=True)