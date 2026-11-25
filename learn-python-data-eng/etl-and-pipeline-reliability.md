# ETL and Pipeline Reliability

## 1. Overview

Data Engineering involves collecting, processing,
transforming, storing, and delivering data reliably.

A data pipeline should not only process data successfully.
It should also detect failures, protect existing outputs,
and produce consistent results when executed repeatedly.

This section introduces fundamental Data Engineering
concepts through the NYC 311 ETL pipeline project.

## 2. What Is a Data Pipeline?

A data pipeline is a sequence of connected operations
that moves and processes data between systems.

A typical data pipeline may include:

- Data ingestion
- Data extraction
- Data validation
- Data transformation
- Data storage
- Logging
- Monitoring
- Error handling

Example:

```text
Data Source
    |
    v
Data Ingestion
    |
    v
Data Validation
    |
    v
Data Transformation
    |
    v
Data Storage
    |
    v
Analytics and Reporting
```

A pipeline may operate continuously or execute
at scheduled intervals.

## 3. ETL (Extract, Transform, Load)

ETL is a common data integration process consisting
of three main stages.

### Extract

Extracting data from a source.

Common data sources include:

- CSV files
- JSON files
- REST APIs
- Relational databases
- Application logs
- Cloud storage
- Streaming systems

Example:

```python
reader = csv.DictReader(file)

for row in reader:
    print(row)
```

### Transform

Processing data according to defined requirements.

Common transformation operations include:

- Data cleaning
- Data validation
- Type conversion
- Filtering
- Deduplication
- Data normalization
- Data aggregation
- Enrichment

Example:

```python
borough = row["borough"].strip()

if borough == "":
    missing_borough += 1
```

### Load

Writing processed data to a destination.

Common destinations include:

- CSV files
- JSON files
- Relational databases
- Data warehouses
- Data lakes
- Cloud object storage

Example:

```python
clean_writer.writerow(row)
```

## 4. ETL vs Data Pipeline

| ETL | Data Pipeline |
|---|---|
| Extract, Transform, Load | A broader sequence of data operations |
| Focuses on data integration | May include ingestion, monitoring, and orchestration |
| Contains three conceptual stages | May contain many different stages |

An ETL process is a type of data pipeline.

Not every data pipeline necessarily follows
the traditional ETL pattern.

## 5. ETL vs ELT

### ETL

```text
Extract -> Transform -> Load
```

Data is transformed before being loaded
into the destination system.

### ELT

```text
Extract -> Load -> Transform
```

Data is loaded into the destination system
before transformation.

ELT is commonly used with modern analytical
databases and cloud data warehouses.

The appropriate approach depends on the system
architecture and processing requirements.

Our NYC 311 project uses the ETL approach.

## 6. Raw and Processed Data

### Raw Data

Raw data represents information received from
the original source before transformation.

```text
data/raw/nyc_311_10000.csv
```

Raw data should generally be preserved to support:

- Reprocessing
- Debugging
- Reproducibility
- Data auditing
- Recovery

### Processed Data

Processed data has passed through one or more
validation or transformation stages.

```text
data/processed/cleaned.csv
data/processed/rejected.csv
```

Keeping raw and processed data separate improves
organization and reduces the risk of modifying
the original dataset.

## 7. Batch Processing

Batch processing handles a finite collection
of records during one execution.

Examples:

- Daily transaction processing
- Hourly application log processing
- Monthly financial reports
- Scheduled CSV ingestion

The NYC 311 pipeline is a batch processing pipeline.

It processes a downloaded dataset containing
10,000 records during each execution.

## 8. Memory-Efficient Processing

Large datasets should not always be loaded
entirely into memory.

Memory-intensive approach:

```python
records = list(csv.DictReader(file))

for row in records:
    process(row)
```

Incremental approach:

```python
reader = csv.DictReader(file)

for row in reader:
    process(row)
```

The second approach avoids creating a complete
list of the dataset.

In this example, process() represents a hypothetical
user-defined processing function.

Our NYC 311 pipeline reads, validates, and writes
records incrementally using CSV reader and writer objects.

This approach is useful for processing datasets
that may be larger than available memory.

## 9. Data Quality

Data quality describes how suitable data is
for its intended purpose.

Common data quality dimensions include:

| Dimension | Description |
|---|---|
| Completeness | Required values are present |
| Accuracy | Values correctly represent reality |
| Consistency | Related values do not contradict each other |
| Validity | Values satisfy defined rules |
| Uniqueness | Records do not contain unintended duplicates |
| Timeliness | Data is sufficiently up to date |

A dataset may pass one quality dimension
while failing another.

For example, a record may contain every required
field but still contain an incorrect value.

## 10. Schema Validation

A schema defines the expected structure of data.

A schema may describe:

- Column names
- Data types
- Required fields
- Nullable fields
- Constraints
- Relationships

Schema validation checks whether incoming data
conforms to the expected structure.

Our pipeline currently performs required-column
validation.

It does not implement complete data type
or constraint validation.

## 11. Required Column Validation

The NYC 311 pipeline requires six columns.

```python
REQUIRED_COLUMNS = {
    "unique_key",
    "created_date",
    "borough",
    "incident_zip",
    "status",
    "closed_date"
}
```

The actual CSV columns are obtained using:

```python
reader = csv.DictReader(file)

fieldnames = reader.fieldnames

actual_columns = set(fieldnames or [])
```

Missing columns are identified using set difference.

```python
missing_columns = REQUIRED_COLUMNS - actual_columns
```

Validation:

```python
if missing_columns:

    logging.error(
        "Missing required columns: %s",
        missing_columns
    )

    raise ValueError("CSV schema validation failed.")

logging.info("Schema validation passed.")
```

The pipeline stops when any required column
is missing.

Additional columns are allowed.

This makes the validation compatible with
datasets containing fields that are not
directly used by the current pipeline.

## 12. Set Difference

A set is a collection of unique elements.

```python
required = {"id", "name", "status"}

actual = {"id", "name", "city"}

missing = required - actual

print(missing)
```

Output:

```text
{'status'}
```

Set difference returns elements present in the
first set but absent from the second set.

This operation is useful for comparing schemas.

An empty set is evaluated as False in a
Boolean context.

A non-empty set is evaluated as True.

```python
if missing:
    print("Required columns are missing.")
```

## 13. Data Quality Validation

Schema validation checks the structure of data.

Data quality validation checks whether individual
values satisfy defined requirements.

Example:

```python
unique_key = row["unique_key"].strip()

if unique_key == "":
    missing_unique_key += 1
```

Another example:

```python
if status == "Closed" and closed_date == "":
    closed_without_date += 1
```

The second example checks consistency between
two related fields.

## 14. Critical and Non-Critical Data Issues

Not every missing value should cause
a record to be rejected.

Validation requirements should depend on
the intended use of the data.

The following rules were defined for
our NYC 311 learning project.

| Validation Rule | Severity | Action |
|---|---|---|
| Missing unique_key | ERROR | Reject record |
| Missing created_date | ERROR | Reject record |
| Missing borough | WARNING | Retain record |
| Missing incident_zip | WARNING | Retain record |
| Closed request without closed_date | WARNING | Retain record |
| Missing required column | ERROR | Fail pipeline |

These are project-specific validation rules.

They are not official NYC 311 data quality policies.

An open service request may legitimately
have an empty closed_date.

Context is important when defining
data validation rules.

## 15. Valid and Invalid Records

Valid records are written to:

```text
data/processed/cleaned.csv
```

Invalid records are written to:

```text
data/processed/rejected.csv
```

Implementation:

```python
if unique_key == "" or created_date == "":

    rejected_writer.writerow(row)
    invalid_count += 1

else:

    clean_writer.writerow(row)
    valid_count += 1
```

Rejected records are preserved instead of
being silently discarded.

This allows them to be investigated,
corrected, or reprocessed later.

A record classified as valid has passed
the implemented validation rules.

It may still contain other data quality problems.

## 16. Data Reconciliation

Data reconciliation compares data between
processing stages to verify consistency.

In our pipeline, the following relationship
must hold:

```text
Total Records = Valid Records + Invalid Records
```

Example:

```text
Total records:   10000
Valid records:    9998
Invalid records:     2
```

The record counts are consistent.

### Implementation

```python
if row_count != valid_count + invalid_count:

    logging.error("Data reconciliation failed.")

    raise ValueError("Record count mismatch.")

else:

    logging.info("Data reconciliation passed.")
```

This check verifies that the internal record
classification counters are consistent.

More comprehensive reconciliation may also include:

- Independent output record counts
- Source and destination comparisons
- Primary key comparisons
- Financial total comparisons
- Checksums
- Duplicate detection

Count equality alone does not prove that
every output record is correct.

## 17. Idempotency

Idempotency means that repeating an operation
with the same input has the same intended effect
on the target state.

A reliable pipeline should avoid creating
unintended duplicate records during retries.

### Non-Idempotent Example

```text
Execution 1: 10000 records
Execution 2: 20000 records
Execution 3: 30000 records
```

The same records are repeatedly appended
to the destination.

### Idempotent Output Example

```text
Execution 1: 10000 records
Execution 2: 10000 records
Execution 3: 10000 records
```

The target data remains consistent
across successful executions.

## 18. Idempotency in File-Based Pipelines

Append mode:

```python
open("cleaned.csv", "a")
```

This may append the same records every time
the pipeline is executed.

Write mode:

```python
open("cleaned.csv", "w")
```

This replaces existing file content.

For a deterministic pipeline that processes
the same unchanged input, replacing the output
can support idempotent data generation.

Our pipeline generates replacement output files
instead of appending records.

The log file intentionally continues to grow
because each execution must have its own history.

Idempotency applies to the intended data output,
not necessarily every system side effect.

## 19. Testing Idempotency

The NYC 311 pipeline was executed three times.

```bash
python3 pipeline.py

wc -l data/processed/cleaned.csv
```

Observed results:

| Execution | Data Records | Physical Lines |
|---|---:|---:|
| First | 10000 | 10001 |
| Second | 10000 | 10001 |
| Third | 10000 | 10001 |

The additional line is the CSV header.

This confirmed that repeated executions
did not increase the observed output record count.

However, equal line counts do not prove
that file contents are identical.

Also, wc -l counts newline characters,
not logical CSV records.

CSV fields containing embedded newlines
may require a CSV-aware counting method.

## 20. Checksums and Hashing

A checksum or hash can be used to compare
file contents.

SHA-256 is a cryptographic hash algorithm
that produces a 256-bit hash value.

Linux provides the sha256sum command.

```bash
sha256sum data/processed/cleaned.csv
```

The resulting hash is represented using
64 hexadecimal characters.

A change to the file content is extremely likely
to produce a different hash.

### Comparing Pipeline Outputs

Calculate the initial hashes:

```bash
sha256sum data/processed/cleaned.csv \
data/processed/rejected.csv
```

Execute the pipeline again:

```bash
python3 pipeline.py
```

Calculate the hashes again:

```bash
sha256sum data/processed/cleaned.csv \
data/processed/rejected.csv
```

Matching hashes provide strong evidence that
the output files have identical byte contents.

Checksums can support:

- File integrity verification
- Reproducibility testing
- Idempotency testing
- Detecting unexpected file changes

They do not independently verify whether
the contents are semantically correct.

## 21. Execution Time

Execution time measures how long an operation takes.

Monitoring execution time helps identify
unexpected performance changes.

Python provides the time module.

```python
import time

start_time = time.perf_counter()

# Execute pipeline operations.

end_time = time.perf_counter()

execution_time = end_time - start_time
```

The result is recorded in the log file.

```python
logging.info(
    "Execution time: %.3f seconds.",
    execution_time
)
```

Observed execution example:

```text
INFO - Execution time: 0.251 seconds.
```

Execution time may depend on:

- Dataset size
- Hardware performance
- Disk speed
- Transformation complexity
- Network latency
- System load

The observed execution time is not a formal
performance benchmark.

## 22. The Problem with Direct Output Writing

Consider an existing output file containing
10,000 successfully processed records.

```python
open("cleaned.csv", "w")
```

Opening the file in write mode immediately
truncates its previous contents.

If the pipeline fails after writing only
4,000 records, the final output may be incomplete.

```text
Previous successful output: 10000 records

Pipeline starts.

Existing output is truncated.

4000 records are written.

Pipeline fails.

Final output: incomplete
```

This creates a risk for downstream systems
that depend on the processed file.

## 23. Temporary Files

Temporary files allow the pipeline to prepare
new outputs without immediately replacing
existing successful outputs.

```python
TEMP_CLEAN_FILE = CLEAN_FILE.with_suffix(".csv.tmp")

TEMP_REJECTED_FILE = REJECTED_FILE.with_suffix(".csv.tmp")
```

Temporary output paths:

```text
data/processed/cleaned.csv.tmp
data/processed/rejected.csv.tmp
```

The pipeline writes records to these files first.

```python
with open(
    TEMP_CLEAN_FILE,
    "w",
    encoding="utf-8",
    newline=""
) as clean_file:

    # Write processed records.
    pass
```

If processing fails before publication,
the previous final output can remain unchanged.

## 24. Atomic File Replacement

After processing and validation are complete,
temporary files replace the final output files.

```python
TEMP_CLEAN_FILE.replace(CLEAN_FILE)

TEMP_REJECTED_FILE.replace(REJECTED_FILE)
```

Data flow:

```text
Raw Data
    |
    v
Extract
    |
    v
Validate and Transform
    |
    v
Write Temporary Files
    |
    v
Complete Validation
    |
    v
Replace Final Files
```

A successful replacement on the same file system
can provide atomic visibility for an individual file.

Readers see either the previous file or the
replacement file rather than a partially written file.

### Important Limitations

- Each output file is replaced separately.
- Both output files are not published as one
  atomic transaction.
- A failure between replacements may leave outputs
  from different executions.
- Atomic replacement alone does not guarantee
  durability during power loss.
- Fixed temporary file names are not safe for
  concurrent pipeline executions.

More advanced production systems may use database
transactions, versioned outputs, or publication manifests.

## 25. Temporary File Cleanup

Temporary files may remain after a processing failure.

The finally block is used to perform cleanup.

```python
finally:

    TEMP_CLEAN_FILE.unlink(missing_ok=True)

    TEMP_REJECTED_FILE.unlink(missing_ok=True)
```

The unlink() method removes a file.

The missing_ok=True parameter prevents an exception
when the file does not exist.

Cleanup normally executes after successful processing
or an exception.

However, cleanup may not execute after forced
process termination or power loss.

Other file system errors can still cause
cleanup to fail.

## 26. Failure Testing

A pipeline should be tested under both
successful and unsuccessful conditions.

Testing only normal execution may hide
important reliability problems.

Common failure scenarios include:

- Missing input file
- Missing required columns
- Empty datasets
- Invalid records
- Unexpected data types
- Permission errors
- Interrupted processing
- Incomplete output generation

Failure testing helps verify that the pipeline
responds appropriately to unexpected conditions.

## 27. NYC 311 Test: Normal Dataset

The original dataset contained 10,000 records.

Observed results:

| Metric | Value |
|---|---:|
| Processed records | 10000 |
| Missing unique_key | 0 |
| Missing created_date | 0 |
| Missing borough | 0 |
| Missing incident_zip | 102 |
| Closed without closed_date | 0 |
| Valid records | 10000 |
| Invalid records | 0 |

The pipeline completed successfully.

Records with missing incident ZIP codes
were retained according to the defined rules.

## 28. NYC 311 Test: Invalid Records

A separate copy of the dataset was created.

```bash
cp data/raw/nyc_311_10000.csv \
data/raw/nyc_311_test.csv
```

Two records were intentionally modified.

- One record was given an empty unique_key.
- One record was given an empty created_date.

Observed results:

| Metric | Value |
|---|---:|
| Processed records | 10000 |
| Valid records | 9998 |
| Invalid records | 2 |
| Missing unique_key | 1 |
| Missing created_date | 1 |

The pipeline successfully separated the
two invalid records and completed execution.

The original dataset was preserved.

## 29. NYC 311 Test: Missing Input File

The input path was temporarily changed.

```python
RAW_FILE = BASE_DIR / "data" / "raw" / "missing_file.csv"
```

The pipeline was executed.

```bash
python3 pipeline.py
```

Observed exception:

```text
FileNotFoundError
```

The exit code was inspected.

```bash
echo $?
```

Observed result:

```text
1
```

The error was recorded in the log file.

No successful completion message was recorded
for the failed execution.

## 30. NYC 311 Test: Simulated Processing Failure

A failure can be intentionally introduced
after opening the temporary output files.

```python
clean_writer.writeheader()

rejected_writer.writeheader()

raise ValueError("Simulated pipeline failure.")
```

The purpose of this test is to verify that:

- The pipeline reports failure.
- The previous final outputs remain unchanged.
- The temporary files are removed by finally.

Output file hashes should be calculated
before and after the failure.

```bash
sha256sum data/processed/cleaned.csv \
data/processed/rejected.csv
```

Temporary files can be inspected using:

```bash
ls data/processed
```

The simulated exception must be removed
after completing the test.

This test procedure was prepared during the lab.
Its final output was not independently verified.

## 31. Pipeline Observability

Observability helps engineers understand
what is happening inside a system.

Common observability components include:

### Logs

Records describing application events.

Examples:

- Pipeline started
- Schema validation passed
- Invalid records detected
- Pipeline completed

### Metrics

Numerical measurements describing system behavior.

Examples:

- Processed record count
- Invalid record count
- Execution time
- Failure count

### Traces

Information about how operations are connected
across different components of a system.

Our pipeline provides basic logging and
records several execution metrics in its log file.

It does not yet implement centralized monitoring
or distributed tracing.

## 32. Retries

A retry is another attempt to execute
a previously failed operation.

Retries are useful for temporary failures.

Examples:

- Temporary network problems
- Temporary database connection failures
- Service unavailability

Not every failure should be retried.

For example, repeatedly executing a pipeline
with a missing required column may not solve
the underlying problem.

Idempotency is important when implementing retries.

Our current pipeline does not implement
automatic retry logic.

Workflow orchestration and API retry strategies
will be studied later.

## 33. NYC 311 Pipeline Architecture

```text
NYC Open Data
      |
      | Manual HTTP download with curl
      v
Raw CSV File
      |
      v
Python ETL Pipeline
      |
      v
Schema Validation
      |
      v
Record-Level Data Validation
      |
      +------------------------+
      |                        |
      v                        v
Valid Records            Invalid Records
      |                        |
      v                        v
cleaned.csv.tmp          rejected.csv.tmp
      |                        |
      +------------------------+
                 |
                 v
       Data Reconciliation
                 |
                 v
       Atomic File Replacement
                 |
        +--------+--------+
        |                 |
        v                 v
   cleaned.csv       rejected.csv
```

Logging records operational events throughout
the pipeline.

Temporary file cleanup is performed using finally.

The Python pipeline currently reads a local CSV file.

The API download is performed separately using curl.

## 34. Project Directory Structure

```text
nyc-311-pipeline/
├── pipeline.py
├── README.md
├── .gitignore
├── data/
│   ├── raw/
│   │   └── nyc_311_10000.csv
│   └── processed/
│       ├── cleaned.csv
│       └── rejected.csv
└── logs/
    └── pipeline.log
```

Raw datasets, generated output files, temporary
files, and runtime logs should generally remain
outside version control for this project.

The source code and documentation should provide
instructions for reproducing the pipeline.

## 35. Reproducibility

Reproducibility means being able to reproduce
an operation or result under documented conditions.

A reproducible project should document:

- Data source
- Input requirements
- Software requirements
- Execution instructions
- Validation rules
- Expected outputs
- Known limitations

Our dataset was downloaded using the NYC Open Data API.

The API query retrieves recent records.

Downloading the same query at a later date may
return different records because the source
dataset changes over time.

Exact result reproducibility requires retaining
the original input snapshot or retrieving a
fixed, versioned dataset.

## 36. Current Pipeline Limitations

The NYC 311 pipeline is an educational project
rather than a complete production system.

Current limitations include:

- Manual API download using curl.
- Limited schema validation.
- Limited record-level validation.
- No comprehensive data type validation.
- No duplicate unique_key detection.
- No automatic retry mechanism.
- No automated unit tests.
- No concurrent execution protection.
- No transaction covering both output files.
- No centralized logging or monitoring.
- No database or data warehouse integration.

These limitations represent opportunities
for future improvements.

## 37. Engineering Terminology

| Term | Meaning |
|---|---|
| ETL | Extract, Transform, Load |
| ELT | Extract, Load, Transform |
| Ingestion | Collecting data into a system |
| Schema | Expected data structure |
| Validation | Checking data against requirements |
| Data Quality | Suitability of data for its intended purpose |
| Reconciliation | Comparing data for consistency |
| Idempotency | Consistent intended effect across repeated operations |
| Checksum | A value used to verify data integrity |
| Hash | A value calculated from input data |
| Batch Processing | Processing a finite collection of records |
| Atomic Replacement | Publishing a replacement as an individual atomic operation |
| Temporary File | An intermediate file used during processing |
| Cleanup | Removing unnecessary resources or files |
| Retry | Repeating a failed operation |
| Observability | Understanding system behavior through its outputs |
| Reproducibility | Recreating an operation under documented conditions |

## 38. Importance in Data Engineering

The concepts covered in this project provide
a foundation for more advanced technologies.

| Concept | Future Application |
|---|---|
| Schema Validation | Databases, APIs, Spark |
| Data Quality | dbt and data testing |
| Reconciliation | Database and warehouse pipelines |
| Idempotency | Airflow, SQL, batch processing |
| Logging | Monitoring and DataOps |
| Batch Processing | Airflow and Spark |
| Atomic Operations | Database transactions |
| Retry | API ingestion and workflow orchestration |
| Reproducibility | Git, Docker, and CI/CD |

The tools used in Data Engineering may change.

The fundamental engineering principles remain
important across different technologies.

## Key Takeaways

- ETL consists of extraction, transformation, and loading.
- Raw and processed data should be kept separate.
- Large datasets benefit from incremental processing.
- Schema validation checks the expected data structure.
- Data quality validation checks individual values.
- Invalid records should not be silently discarded.
- Reconciliation verifies consistency between stages.
- Idempotency helps prevent unintended duplication.
- Checksums support file integrity verification.
- Execution time provides useful performance information.
- Temporary files help protect previous successful outputs.
- Atomic replacement improves individual file publication.
- Failure testing is essential for pipeline reliability.
- Logging provides operational visibility.
- Reproducibility requires clear documentation.
- Reliable pipelines must handle both data problems
  and operational failures.