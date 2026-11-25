# NYC 311 ETL Pipeline

## Overview

A file-based batch ETL pipeline developed using Python
and real-world public service request data from NYC Open Data.

This project demonstrates fundamental Data Engineering
principles, including incremental data processing,
data quality validation, exception handling, operational
logging, idempotency, and reliable file publication.

The initial dataset contains 10,000 NYC 311 service requests.

The project is part of my Data Engineering learning journey.

## 1. Project Objectives

- Process real-world datasets using Python.
- Build a memory-efficient ETL pipeline.
- Validate incoming data structures.
- Detect missing and invalid values.
- Separate valid and invalid records.
- Preserve original raw data.
- Monitor pipeline execution through logs.
- Prevent unintended output duplication.
- Protect existing outputs during processing failures.
- Document a reproducible data processing workflow.

## 2. Data Source

The dataset is provided by NYC Open Data.

**Dataset:** NYC 311 Service Requests

**Provider:** City of New York

**Dataset ID:** erm2-nwe9

**Source:**

https://data.cityofnewyork.us/d/erm2-nwe9

**API Endpoint:**

https://data.cityofnewyork.us/resource/erm2-nwe9.csv

NYC 311 service requests include information about
non-emergency public service requests submitted
to New York City agencies.

The downloaded dataset snapshot contains:

- 10,000 records
- 44 columns
- Service request identifiers
- Creation and closure timestamps
- Complaint categories
- Request status information
- Responsible agencies
- Geographic information

The source dataset changes over time.

Downloading the same API query at a later date may
produce different records and validation results.

## 3. Technologies

| Technology | Purpose |
|---|---|
| Python | Pipeline development |
| pathlib | File and directory management |
| csv | Incremental CSV reading and writing |
| logging | Operational event logging |
| time | Execution time measurement |
| Linux | Development and execution environment |
| curl | Manual data ingestion |
| SHA-256 | File integrity comparison |
| Git | Version control |
| GitHub | Project hosting and documentation |

The Python pipeline uses only standard library modules.

No external Python packages are required.

## 4. Pipeline Architecture

```text
                NYC Open Data API
                         |
                         | curl
                         v
                  Raw CSV Dataset
                         |
                         v
                  Extract Records
                         |
                         v
                  Schema Validation
                         |
                         v
                Data Quality Validation
                         |
            +------------+------------+
            |                         |
            v                         v
       Valid Records            Invalid Records
            |                         |
            v                         v
    cleaned.csv.tmp          rejected.csv.tmp
            |                         |
            +------------+------------+
                         |
                         v
                 Data Reconciliation
                         |
                         v
              Atomic File Replacement
                         |
            +------------+------------+
            |                         |
            v                         v
       cleaned.csv               rejected.csv
```

Logging records operational events throughout
pipeline execution.

Temporary file cleanup is performed using
a finally block.

## 5. Project Structure

```text
nyc-311-pipeline/
├── README.md
├── .gitignore
├── pipeline.py
├── data/
│   ├── raw/
│   │   └── nyc_311_10000.csv
│   └── processed/
│       ├── cleaned.csv
│       └── rejected.csv
└── logs/
    └── pipeline.log
```

The data and log directories contain local runtime files.

Raw datasets, generated outputs, temporary files,
and execution logs are excluded from version control.

The processed data and log directories are created
automatically by the pipeline when required.

## 6. ETL Workflow

### Extract

The pipeline reads the downloaded CSV dataset
using csv.DictReader.

Records are processed individually instead of
loading the complete dataset into memory.

```python
reader = csv.DictReader(file)

for row in reader:
    # Process one record at a time.
    pass
```

### Transform

The pipeline performs:

- Required-column validation
- Missing value detection
- Whitespace-aware field validation
- Record classification
- Record count tracking
- Data reconciliation

Validation determines whether a record should
be retained or rejected.

The original field values are preserved in the output.

Whitespace stripping is used for validation, rather
than permanently modifying every field.

### Load

Valid records are written to:

```text
data/processed/cleaned.csv
```

Invalid records are written to:

```text
data/processed/rejected.csv
```

The pipeline initially writes to temporary files.

Final output files are replaced only after
record processing and validation are complete.

## 7. Schema Validation

The following columns are required:

| Column | Description |
|---|---|
| unique_key | Service request identifier |
| created_date | Request creation timestamp |
| borough | NYC borough |
| incident_zip | Incident ZIP code |
| status | Service request status |
| closed_date | Request closure timestamp |

Required columns are compared with the
actual CSV header using set difference.

```python
missing_columns = REQUIRED_COLUMNS - actual_columns
```

If a required column is missing, the pipeline
raises a ValueError and stops execution.

Additional columns are allowed and preserved.

This implementation validates required column
presence rather than a complete typed schema.

## 8. Data Quality Rules

| Validation Rule | Severity | Action |
|---|---|---|
| Missing unique_key | ERROR | Reject record |
| Missing created_date | ERROR | Reject record |
| Missing borough | WARNING | Retain record |
| Missing incident_zip | WARNING | Retain record |
| Closed request without closed_date | WARNING | Retain record |
| Missing required column | ERROR | Fail pipeline |
| Missing input file | ERROR | Fail pipeline |
| Record count mismatch | ERROR | Fail pipeline |

These rules were designed for this educational project.

They are not official NYC 311 data quality policies.

Records classified as valid have passed the
implemented validation rules.

They may still contain other data quality issues.

## 9. Data Reconciliation

The pipeline verifies the following relationship:

```text
Total Records = Valid Records + Invalid Records
```

Implementation:

```python
if row_count != valid_count + invalid_count:
    raise ValueError("Record count mismatch.")
```

This checks the consistency of internal
record classification counters.

It does not independently verify every
record written to the output files.

## 10. Memory-Efficient Processing

The pipeline processes CSV records incrementally.

```python
for row in reader:
    # Validate and write the current record.
    pass
```

It does not create a complete in-memory list
of all input records.

This approach reduces memory requirements
when processing large datasets.

## 11. Idempotency

The pipeline generates replacement output files
instead of appending records to existing outputs.

Repeated successful executions using the same
unchanged input do not intentionally duplicate data.

Observed record count test:

| Execution | Output Records | Physical Lines |
|---|---:|---:|
| First | 10000 | 10001 |
| Second | 10000 | 10001 |
| Third | 10000 | 10001 |

The additional physical line is the CSV header.

The log file intentionally retains the history
of multiple pipeline executions.

## 12. Temporary Files and Atomic Replacement

The pipeline initially writes data to:

```text
cleaned.csv.tmp
rejected.csv.tmp
```

After successful processing:

```python
TEMP_CLEAN_FILE.replace(CLEAN_FILE)

TEMP_REJECTED_FILE.replace(REJECTED_FILE)
```

This prevents existing final outputs from being
truncated during the initial processing stage.

Temporary files are removed using:

```python
finally:
    TEMP_CLEAN_FILE.unlink(missing_ok=True)

    TEMP_REJECTED_FILE.unlink(missing_ok=True)
```

Each output file is replaced individually.

The two replacements do not constitute
a single atomic transaction.

The current implementation assumes that
only one pipeline instance is running at a time.

## 13. Logging and Monitoring

Pipeline events are recorded in:

```text
logs/pipeline.log
```

Logging levels used in this project:

| Level | Purpose |
|---|---|
| INFO | Normal pipeline events and execution metrics |
| WARNING | Non-fatal data quality issues |
| ERROR | Invalid records or detected pipeline failures |

Logged information includes:

- Pipeline start
- Input file opening
- Schema validation results
- Total processed records
- Missing field counts
- Valid and invalid record counts
- Reconciliation results
- Output file locations
- Execution time
- Successful completion

A missing input file is logged and its
exception is re-raised.

Other unhandled exceptions also cause
the Python process to fail.

## 14. Execution Time

The pipeline measures elapsed processing time
using time.perf_counter().

```python
start_time = time.perf_counter()

# Pipeline operations

end_time = time.perf_counter()

execution_time = end_time - start_time
```

An observed execution time was:

```text
Execution time: 0.251 seconds.
```

This measurement belongs to one local execution
of the 10,000-record dataset.

It is not a formal performance benchmark.

## 15. Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- curl
- Linux, macOS, or Windows with WSL

No additional Python packages are required.

### Step 1: Clone the Repository

```bash
git clone https://github.com/esma-codes/data-engineering-journey.git

cd data-engineering-journey
```

### Step 2: Navigate to the Project

```bash
cd learn-python-data-eng/labs/nyc-311-pipeline
```

### Step 3: Create the Raw Data Directory

```bash
mkdir -p data/raw
```

### Step 4: Download the Dataset

```bash
curl -fL \
'https://data.cityofnewyork.us/resource/erm2-nwe9.csv?$limit=10000&$order=created_date%20DESC,unique_key%20DESC' \
-o data/raw/nyc_311_10000.csv
```

The query requests up to 10,000 recent service requests.

Because the source dataset is updated over time,
the downloaded records may differ from the
original project snapshot.

### Step 5: Inspect the Input

```bash
head -n 2 data/raw/nyc_311_10000.csv

wc -l data/raw/nyc_311_10000.csv

du -h data/raw/nyc_311_10000.csv
```

The wc command counts physical newline characters,
not logical CSV records.

### Step 6: Execute the Pipeline

```bash
python3 pipeline.py
```

The pipeline creates the processed data and
log directories if they do not exist.

### Step 7: Inspect the Results

```bash
ls data/processed

wc -l data/processed/cleaned.csv

wc -l data/processed/rejected.csv
```

### Step 8: Inspect Pipeline Logs

```bash
tail -n 20 logs/pipeline.log
```

## 16. Observed Results

The following results were obtained from
the original dataset snapshot.

| Metric | Result |
|---|---:|
| Total processed records | 10000 |
| Missing unique_key | 0 |
| Missing created_date | 0 |
| Missing borough | 0 |
| Missing incident_zip | 102 |
| Closed without closed_date | 0 |
| Valid records | 10000 |
| Invalid records | 0 |
| Example execution time | 0.251 seconds |

The 102 records with missing ZIP codes were
retained according to the defined validation rules.

## 17. Example Log Output

The following excerpt combines representative
messages observed during project development.

```text
INFO - NYC 311 pipeline started.
INFO - Input CSV opened successfully.
INFO - Schema validation passed.
INFO - Processed 10000 rows.
INFO - Missing unique_key: 0
INFO - Missing created_date: 0
INFO - Missing borough: 0
INFO - Missing incident_zip: 102
INFO - Closed without closed_date: 0
INFO - Valid records: 10000
INFO - Invalid records: 0
INFO - Data reconciliation passed.
WARNING - Found 102 rows with missing incident ZIP.
INFO - Execution time: 0.251 seconds.
INFO - NYC 311 pipeline finished successfully.
```

The actual log file also includes timestamps
and output file locations.

## 18. Failure Testing

### Test 1: Invalid Records

A separate copy of the original dataset was created.

Two records were intentionally modified:

- One record with a missing unique_key.
- One record with a missing created_date.

Observed results:

| Metric | Result |
|---|---:|
| Total records | 10000 |
| Valid records | 9998 |
| Invalid records | 2 |

The pipeline successfully separated
the two invalid records.

### Test 2: Missing Input File

The input path was temporarily changed
to reference a nonexistent file.

Observed exception:

```text
FileNotFoundError
```

Process exit code:

```text
1
```

The pipeline recorded the failure and did not
report successful completion for that execution.

### Test 3: Repeated Execution

The pipeline was executed three times.

The cleaned output contained 10,001 physical
lines after each execution.

This verified that the observed output record count
did not increase during repeated executions.

### Test 4: Checksum Comparison

Output file contents can be compared using:

```bash
sha256sum data/processed/cleaned.csv \
data/processed/rejected.csv
```

Run the pipeline again and compare the hashes.

Matching hashes provide strong evidence
that file contents remained identical.

### Test 5: Simulated Processing Failure

A controlled exception can be introduced
after temporary output files are opened.

```python
raise ValueError("Simulated pipeline failure.")
```

Expected behavior:

- The pipeline fails.
- Previous final outputs remain unchanged.
- Temporary files are removed.

The simulated exception must be removed
after completing the test.

## 19. Test Summary

| Test | Status |
|---|---|
| Normal pipeline execution | Passed |
| Valid input schema | Passed |
| Invalid record detection | Passed |
| Invalid record separation | Passed |
| Missing input file | Passed |
| Non-zero failure exit code | Passed |
| Data reconciliation | Passed |
| Execution time logging | Passed |
| Repeated execution record count | Passed |
| Temporary output replacement during normal execution | Passed |
| Missing-column failure scenario | Not yet verified |
| Checksum-based content verification | Not yet verified |
| Simulated failure cleanup verification | Not yet verified |

These are manual development tests.

Automated unit and integration tests have
not yet been implemented.

## 20. Engineering Principles

This project applies the following principles:

- Memory-efficient processing
- Separation of raw and processed data
- Data quality validation
- Fail-fast behavior for critical errors
- Record-level error isolation
- Data reconciliation
- Idempotent output generation
- Temporary file management
- Atomic replacement of individual files
- Operational logging
- Resource cleanup
- Reproducible execution

## 21. Current Limitations

This project is an educational implementation.

It is not a complete production-ready data platform.

Current limitations include:

- Manual data ingestion through curl
- Limited schema and data quality validation
- No comprehensive data type validation
- No duplicate identifier detection
- No automated unit tests
- No automatic retry mechanism
- No concurrent execution protection
- No transaction covering both output files
- No centralized monitoring
- No log rotation
- No database integration
- No workflow orchestration

Atomic file replacement does not independently
guarantee durability during power loss.

## 22. Future Improvements

- Automated API ingestion with Python
- HTTP pagination
- Request timeouts and retries
- Environment-based configuration
- Modular pipeline architecture
- Type hints
- Automated testing with pytest
- More comprehensive data validation
- Parquet output
- PostgreSQL integration
- Workflow orchestration with Apache Airflow
- Containerized execution with Docker

These improvements will be explored in later
stages of the Data Engineering learning journey.

## 23. Learning Outcomes

Through this project, I developed practical
experience with:

- Python file handling
- Structured data processing
- Real-world public datasets
- ETL pipeline development
- Data quality and schema validation
- Exception handling
- Operational logging
- Failure testing
- Pipeline reliability
- Linux command-line tools
- Technical documentation

## 24. Data Attribution

The source dataset is provided by the City of New York
through the NYC Open Data platform.

The source data is not owned by the author of this project.

Dataset source:

https://data.cityofnewyork.us/d/erm2-nwe9

---

Part of my Data Engineering learning journey.