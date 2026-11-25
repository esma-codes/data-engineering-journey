# Python for Data Engineering

## Overview

This section is part of my Data Engineering learning journey.

The goal is to develop practical Python skills for building
efficient, reliable, and reproducible data pipelines.

Rather than focusing only on Python syntax, this section
emphasizes real-world data processing and fundamental
Data Engineering principles.

## Learning Objectives

- Write readable and efficient Python code.
- Process large datasets incrementally.
- Work with files and directories.
- Read and write structured data formats.
- Validate data structures and individual records.
- Handle exceptions and pipeline failures.
- Implement logging and performance monitoring.
- Build reliable and reproducible ETL pipelines.
- Develop practical Data Engineering projects.

## Study Notes

| Topic | Description |
|---|---|
| [Pythonic Data Handling](pythonic-data-handling.md) | Iterators, generators, yield, comprehensions, unpacking, lambda, map, and filter |
| [Files and Paths](files-and-paths.md) | Pathlib, file operations, context managers, encoding, and temporary files |
| [CSV and JSON](csv-and-json.md) | CSV processing, JSON, JSONL, serialization, and format conversion |
| [Exceptions and Logging](exceptions-and-logging.md) | Exception handling, logging levels, exit codes, and execution time |
| [ETL and Pipeline Reliability](etl-and-pipeline-reliability.md) | ETL, data quality, schema validation, reconciliation, idempotency, and atomic file replacement |

## Learning Progress

### Phase 1 — Python Foundations for Data Engineering

- [x] Iterables and iterators
- [x] Generators and yield
- [x] Lazy and eager evaluation
- [x] List and dictionary comprehensions
- [x] Generator expressions
- [x] Unpacking
- [x] Lambda functions
- [x] map() and filter()
- [x] Context managers

### Phase 2 — Files and Data Formats

- [x] Object-oriented path management with pathlib
- [x] Relative and absolute paths
- [x] File reading and writing
- [x] Memory-efficient file processing
- [x] Character encoding
- [x] CSV reader and writer
- [x] DictReader and DictWriter
- [x] JSON serialization and deserialization
- [x] CSV and JSON conversion
- [x] JSON Lines fundamentals

### Phase 3 — Exception Handling and Pipeline Reliability

- [x] Exception handling
- [x] Raising and re-raising exceptions
- [x] Process exit codes
- [x] Logging configuration
- [x] Logging severity levels
- [x] ETL fundamentals
- [x] Schema validation
- [x] Data quality validation
- [x] Data reconciliation
- [x] Execution time measurement
- [x] Idempotency fundamentals
- [x] Checksum fundamentals
- [x] Temporary file management
- [x] Atomic file replacement
- [x] Failure testing fundamentals

### Phase 4 — Python Environments and API Ingestion

- [ ] Virtual environments
- [ ] pip and package management
- [ ] Dependency management
- [ ] requirements.txt
- [ ] Environment variables
- [ ] Secrets management
- [ ] HTTP fundamentals
- [ ] REST APIs
- [ ] API requests with Python
- [ ] Query parameters and headers
- [ ] Pagination
- [ ] Timeouts
- [ ] Retry mechanisms
- [ ] Automated API ingestion pipeline

### Phase 5 — Software Engineering for Data Pipelines

- [ ] Modular pipeline architecture
- [ ] Functions and reusable components
- [ ] Python modules and packages
- [ ] Entry points and main functions
- [ ] Type hints
- [ ] Configuration management
- [ ] Unit testing with pytest
- [ ] Automated data validation tests

### Phase 6 — Advanced Data Processing

- [ ] Large dataset processing
- [ ] Chunk-based processing
- [ ] Pandas for Data Engineering
- [ ] Data type optimization
- [ ] Data transformation and aggregation
- [ ] Parquet file format
- [ ] Apache Arrow and PyArrow
- [ ] Performance optimization

### Phase 7 — Final Python ETL Project

- [ ] Automated data ingestion
- [ ] Modular ETL architecture
- [ ] Data transformation
- [ ] Data quality validation
- [ ] Error handling and logging
- [ ] Automated testing
- [ ] Reproducible execution
- [ ] Project documentation

## Hands-On Projects

### 01 — NYC 311 ETL Pipeline

[View Project](labs/nyc-311-pipeline/)

A file-based batch ETL pipeline built using real-world
public service request data from NYC Open Data.

The initial dataset contains 10,000 service requests.

#### Technologies

- Python
- Python Standard Library
- pathlib
- csv
- logging
- time
- Linux
- Git and GitHub
- NYC Open Data API
- curl

#### Implemented Features

- Incremental CSV processing
- Required-column validation
- Record-level data quality checks
- Valid and invalid record separation
- Record count reconciliation
- Operational logging
- Exception handling
- Execution time measurement
- Idempotent output generation
- Temporary output files
- Individual atomic file replacement
- Temporary file cleanup

#### Pipeline Architecture

```text
NYC Open Data API
        |
        | Manual download with curl
        v
     Raw CSV
        |
        v
  Python ETL Pipeline
        |
        v
  Schema Validation
        |
        v
  Data Quality Validation
        |
        +----------------------+
        |                      |
        v                      v
   Valid Records         Invalid Records
        |                      |
        v                      v
   Temporary CSV          Temporary CSV
        |                      |
        +----------------------+
                   |
                   v
         Data Reconciliation
                   |
                   v
          File Replacement
                   |
          +--------+--------+
          |                 |
          v                 v
      cleaned.csv      rejected.csv
```

#### Observed Results

| Metric | Result |
|---|---:|
| Input records | 10,000 |
| Valid records | 10,000 |
| Invalid records | 0 |
| Missing incident ZIP codes | 102 |
| Example execution time | 0.251 seconds |

The missing ZIP codes were retained according to
the project's validation rules.

These results belong to the original downloaded
dataset snapshot.

Downloading newer records may produce different results.

#### Failure Testing

| Test | Status |
|---|---|
| Normal pipeline execution | Passed |
| Required-column validation with valid input | Passed |
| Missing unique_key | Passed |
| Missing created_date | Passed |
| Missing input file | Passed |
| Non-zero exit code on missing input | Passed |
| Record count reconciliation | Passed |
| Execution time logging | Passed |
| Repeated execution without record count growth | Passed |
| Checksum-based output comparison | Not yet verified |
| Simulated failure and temporary file cleanup | Not yet verified |

The project is an educational implementation and is not
intended to represent a complete production-ready system.

## Directory Structure

```text
learn-python-data-eng/
├── README.md
├── pythonic-data-handling.md
├── files-and-paths.md
├── csv-and-json.md
├── exceptions-and-logging.md
├── etl-and-pipeline-reliability.md
└── labs/
    └── nyc-311-pipeline/
        ├── README.md
        ├── .gitignore
        ├── pipeline.py
        ├── data/
        │   ├── raw/
        │   └── processed/
        └── logs/
```

Raw datasets, generated output files, temporary files,
and runtime logs are intended to remain outside version control.

## Engineering Principles

Throughout this learning journey, I focus on:

- Memory efficiency
- Data quality
- Reliability
- Reproducibility
- Maintainability
- Observability
- Idempotency
- Clear documentation
- Safe failure handling
- Practical problem-solving

## Learning Approach

Each topic follows a structured learning process:

1. Understand the fundamental concept.
2. Study practical Python examples.
3. Implement the concept in code.
4. Apply it to real-world data.
5. Test normal and failure scenarios.
6. Document the knowledge.
7. Track progress with Git and GitHub.

## Next Steps

The next phase focuses on Python virtual environments,
dependency management, and automated API ingestion.

The NYC 311 dataset will continue to serve as a practical
data source for developing more advanced pipelines.

Future stages will introduce database integration,
workflow orchestration, and scalable data processing.

---

Part of my long-term Data Engineering learning journey.