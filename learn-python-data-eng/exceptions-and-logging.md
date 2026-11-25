# Exception Handling and Logging in Python

## 1. Overview

Data Engineering pipelines must handle unexpected
situations without silently producing incorrect results.

Common pipeline problems include:

- Missing input files
- Invalid data types
- Missing required fields
- Unexpected CSV schemas
- Invalid JSON responses
- Permission errors
- Network failures
- Incomplete output files

Exception handling and logging help developers detect,
understand, and manage these problems.

## 2. Syntax Errors vs Exceptions

### Syntax Error

A syntax error occurs when Python code does not follow
the rules of the Python language.

```python
if True
    print("Hello")
```

The missing colon causes a SyntaxError.

Python cannot execute the script successfully
because the code cannot be parsed.

### Exception

An exception can occur during program execution,
even when the syntax is correct.

```python
number = int("hello")
```

This produces a ValueError.

| Syntax Error | Exception at Runtime |
|---|---|
| Invalid Python syntax | Problem during execution |
| Detected during parsing | Detected during execution |
| Script cannot start normally | Script may execute before the error occurs |

SyntaxError is itself a Python exception class.

## 3. Common Python Exceptions

| Exception | Description |
|---|---|
| FileNotFoundError | A required file or directory does not exist |
| ValueError | A value is inappropriate for an operation |
| TypeError | An operation receives an inappropriate data type |
| KeyError | A dictionary key does not exist |
| IndexError | A sequence index is out of range |
| ZeroDivisionError | Division by zero |
| PermissionError | Insufficient permissions |
| AttributeError | An attribute or method does not exist |
| JSONDecodeError | Invalid JSON content |

JSONDecodeError is provided by the json module.

The other exceptions listed above are built-in
Python exception classes.

## 4. The try and except Statements

The try block contains code that may raise an exception.

The except block handles a matching exception.

```python
try:
    number = int("hello")

except ValueError:
    print("Invalid number.")
```

Output:

```text
Invalid number.
```

- try is a Python keyword.
- except is a Python keyword.
- ValueError is a built-in exception class.

## 5. Handling Multiple Exceptions

Different exceptions may require different responses.

```python
try:
    with open("records.txt", "r", encoding="utf-8") as file:
        number = int(file.read())

except FileNotFoundError:
    print("Input file does not exist.")

except ValueError:
    print("Invalid numeric value.")
```

Multiple exception classes can also be handled together.

```python
try:
    number = int(None)

except (ValueError, TypeError):
    print("Invalid value or data type.")
```

Specific exception handling makes error management
more predictable and easier to understand.

## 6. Exception Objects

The as keyword can assign a caught exception object
to a variable.

```python
try:
    number = int("hello")

except ValueError as error:
    print(error)
```

Example output:

```text
invalid literal for int() with base 10: 'hello'
```

### Terminology

| Component | Category |
|---|---|
| ValueError | Exception class |
| error | User-defined variable |
| Caught exception | Exception object |
| as | Python keyword |
| print() | Built-in function |

The variable error references the exception object.

It provides information about the problem that occurred.

## 7. The else Block

The else block executes when the try block
completes normally without raising an exception.

```python
try:
    number = int("100")

except ValueError:
    print("Invalid number.")

else:
    print("Conversion successful.")
```

Output:

```text
Conversion successful.
```

The else block is useful for operations that should
only occur after successful execution of the try block.

### Pipeline Example

```python
try:
    # Process the input data.
    pass

except FileNotFoundError as error:
    print(error)
    raise

else:
    print("Pipeline finished successfully.")
```

## 8. The finally Block

The finally block is used for cleanup operations.

It normally executes whether the try block succeeds
or raises an exception.

```python
try:
    number = int("hello")

except ValueError:
    print("Invalid value.")

finally:
    print("Cleanup completed.")
```

Output:

```text
Invalid value.
Cleanup completed.
```

Common use cases:

- Closing resources
- Removing temporary files
- Releasing connections
- Performing cleanup operations

Forced process termination or power loss may prevent
the finally block from executing.

## 9. Complete Exception Handling Structure

```python
try:
    # Execute the main operation.
    pass

except ValueError as error:
    # Handle a specific exception.
    print(error)

else:
    # Execute after normal completion.
    print("Operation successful.")

finally:
    # Perform cleanup.
    print("Cleanup completed.")
```

Execution flow:

```text
              try
               |
        Exception raised?
          /          \
        Yes           No
         |             |
      except         else
         |             |
          \           /
             finally
```

The diagram assumes that a matching except block
is available.

An unhandled exception propagates after cleanup.

## 10. Raising Exceptions

The raise keyword explicitly raises an exception.

```python
age = -10

if age < 0:
    raise ValueError("Age cannot be negative.")
```

### Data Engineering Example

```python
required_columns = {"id", "status"}

actual_columns = {"status", "city"}

missing_columns = required_columns - actual_columns

if missing_columns:
    raise ValueError("Required columns are missing.")
```

Raising exceptions is useful when a pipeline detects
a condition that prevents safe processing.

## 11. Re-raising Exceptions

The raise keyword can also re-raise
the currently handled exception.

```python
try:
    with open("missing_file.csv", "r") as file:
        content = file.read()

except FileNotFoundError as error:
    print(error)
    raise
```

The exception is initially caught.

Its information is displayed.

The bare raise statement then re-raises
the original exception.

This allows the failure to propagate instead of
being silently ignored.

## 12. Exit Codes

An exit code communicates the execution status
of a process to the operating system.

| Exit Code | Meaning |
|---|---|
| 0 | Successful execution |
| Non-zero | Failure or another exceptional status |

In Linux, the exit code of the most recently
executed command can be inspected using:

```bash
echo $?
```

Example:

```bash
python3 pipeline.py
echo $?
```

An unhandled Python exception normally results
in exit code 1.

### Why Exit Codes Matter

Workflow orchestration systems can use process
exit codes to determine whether a task succeeded.

Examples include:

- Apache Airflow
- Shell scripts
- CI/CD pipelines
- Scheduled batch jobs

Depending on their configuration, these systems
may retry failed tasks or send notifications.

## 13. The logging Module

Python provides a standard library module
for recording application events.

```python
import logging
```

Logging is useful for:

- Monitoring pipeline execution
- Recording errors
- Tracking warnings
- Measuring performance
- Investigating failures
- Maintaining execution history

No external package installation is required.

## 14. print() vs Logging

The print() function displays information,
usually in the terminal.

```python
print("Pipeline started.")
```

Logging provides additional information and
configuration options.

```python
logging.info("Pipeline started.")
```

| print() | Logging |
|---|---|
| Basic output | Structured event information |
| No built-in severity levels | Multiple severity levels |
| No automatic timestamp by default | Configurable timestamps |
| Usually writes to standard output | Supports configurable destinations |
| Useful for quick debugging | Suitable for application monitoring |

Logging is generally preferred for recording
operational events in data pipelines.

## 15. Configuring Logging

```python
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

### Parameters

| Parameter | Description |
|---|---|
| filename | Destination log file |
| level | Minimum logging severity |
| format | Structure of each log message |

### Format Fields

| Field | Description |
|---|---|
| %(asctime)s | Timestamp |
| %(levelname)s | Logging severity |
| %(message)s | Log message |

Example output:

```text
2026-11-25 12:52:40,700 - INFO - Pipeline started.
```

By default, file-based logging appends new messages
to the existing log file.

## 16. Logging Levels

Python provides five standard logging levels.

| Level | Numeric Value | Purpose |
|---|---:|---|
| DEBUG | 10 | Detailed debugging information |
| INFO | 20 | Normal operational events |
| WARNING | 30 | Unexpected but manageable conditions |
| ERROR | 40 | An operation encountered a serious problem |
| CRITICAL | 50 | A particularly severe problem |

### DEBUG

```python
logging.debug("Reading the next record.")
```

Used for detailed technical information.

### INFO

```python
logging.info("Pipeline started.")
```

Used for normal execution events.

### WARNING

```python
logging.warning("Some records have missing ZIP codes.")
```

Used for potential problems that may not require
the pipeline to stop.

### ERROR

```python
logging.error("Required input file was not found.")
```

Used when an operation encounters a serious problem.

### CRITICAL

```python
logging.critical("The system cannot continue safely.")
```

Used for particularly severe failures.

Logging severity alone does not control
program execution.

## 17. Logging Level Threshold

```python
logging.basicConfig(level=logging.INFO)
```

With the threshold set to INFO:

```text
DEBUG       Not recorded

INFO        Recorded
WARNING     Recorded
ERROR       Recorded
CRITICAL    Recorded
```

Messages below the configured threshold are ignored
by that logging configuration.

Changing the threshold to DEBUG allows more
detailed information to be recorded.

## 18. Logging Variable Values

Logging supports placeholders for variable values.

```python
row_count = 10000

logging.info("Processed %s rows.", row_count)
```

Output:

```text
INFO - Processed 10000 rows.
```

Multiple values can be included.

```python
valid_count = 9998
invalid_count = 2

logging.info(
    "Valid: %s, Invalid: %s",
    valid_count,
    invalid_count
)
```

### Common Formatting Placeholders

| Placeholder | Purpose |
|---|---|
| %s | String representation |
| %d | Integer formatting |
| %f | Floating-point formatting |
| %.3f | Floating-point value with three decimal places |

Example:

```python
execution_time = 0.251782

logging.info(
    "Execution time: %.3f seconds.",
    execution_time
)
```

Output:

```text
INFO - Execution time: 0.252 seconds.
```

## 19. Logging Placeholders vs f-strings

Using an f-string:

```python
logging.info(f"Processed {row_count} rows.")
```

Using logging placeholders:

```python
logging.info("Processed %s rows.", row_count)
```

Both approaches are valid.

However, logging placeholders allow message formatting
to be deferred until the logging system needs it.

An f-string is evaluated before the logging
function is called.

Deferred formatting can be useful when some logging
messages are disabled by the configured logging level.

## 20. Logging Exceptions

Logging can be combined with exception handling.

```python
try:
    with open("missing_file.csv", "r") as file:
        content = file.read()

except FileNotFoundError as error:

    logging.error(
        "Required file not found: %s",
        error
    )

    raise
```

This approach:

1. Catches the exception.
2. Records information about the problem.
3. Re-raises the original exception.
4. Allows the process to report failure.

## 21. Logging Does Not Stop Execution

The logging.error() function records an error message.

It does not automatically raise an exception
or terminate the program.

```python
logging.error("A record is invalid.")

print("Processing continues.")
```

To explicitly raise an exception:

```python
logging.error("Required schema is missing.")

raise ValueError("Schema validation failed.")
```

The responsibilities are different.

| Operation | Responsibility |
|---|---|
| Validation | Detects a problem |
| Logging | Records information about the problem |
| Exception handling | Manages an exception |
| raise | Raises or re-raises an exception |

## 22. Record-Level Errors vs Pipeline-Level Failures

Not every data quality problem should stop
an entire pipeline.

### Record-Level Errors

A single record may contain invalid information.

Example:

```python
if unique_key == "":
    rejected_writer.writerow(row)
    invalid_count += 1
```

The invalid record is separated from valid records.

The pipeline can continue processing the remaining data.

### Pipeline-Level Failures

Some problems prevent the pipeline from
operating safely.

Examples:

- Missing input file
- Missing required CSV columns
- Record count mismatch
- Failure to write output files

Example:

```python
if missing_columns:
    logging.error(
        "Missing required columns: %s",
        missing_columns
    )

    raise ValueError("CSV schema validation failed.")
```

The appropriate behavior depends on the pipeline's
data quality requirements and business rules.

## 23. Error Handling in the NYC 311 Pipeline

The NYC 311 pipeline uses different responses
for different validation failures.

| Problem | Severity | Action |
|---|---|---|
| Missing incident ZIP | WARNING | Retain record |
| Missing borough | WARNING | Retain record |
| Closed request without closed date | WARNING | Retain record |
| Missing unique_key | ERROR | Reject record |
| Missing created_date | ERROR | Reject record |
| Missing required column | ERROR | Fail pipeline |
| Missing input file | ERROR | Fail pipeline |
| Record count mismatch | ERROR | Fail pipeline |

These are validation rules defined for our learning
project, not official NYC 311 data quality rules.

A valid record is a record that satisfies the
validation requirements implemented in the pipeline.

It is not necessarily free of every possible
data quality issue.

## 24. Real Pipeline Execution Results

The original NYC 311 dataset contained 10,000 records.

Observed results:

```text
INFO - Processed 10000 rows.
INFO - Missing unique_key: 0
INFO - Missing created_date: 0
INFO - Missing borough: 0
INFO - Missing incident_zip: 102
INFO - Closed without closed_date: 0
INFO - Valid records: 10000
INFO - Invalid records: 0
WARNING - Found 102 rows with missing incident ZIP.
INFO - NYC 311 pipeline finished successfully.
```

Missing ZIP codes did not cause pipeline failure
because they were classified as non-fatal issues.

## 25. Testing Invalid Records

A separate copy of the original dataset was created
for failure testing.

Two records were intentionally modified:

- One record with a missing unique_key.
- One record with a missing created_date.

Observed results:

```text
Processed records: 10000
Valid records: 9998
Invalid records: 2
```

Log output:

```text
ERROR - Found 1 rows with missing unique_key.
ERROR - Found 1 rows with missing created_date.
INFO - NYC 311 pipeline finished successfully.
```

The pipeline successfully identified and separated
the invalid records.

An ERROR message does not necessarily mean that
the entire pipeline failed.

## 26. Testing Missing Input Files

The input path was temporarily changed to reference
a nonexistent CSV file.

```python
RAW_FILE = BASE_DIR / "data" / "raw" / "missing_file.csv"
```

Observed terminal output:

```text
FileNotFoundError: [Errno 2] No such file or directory
```

The pipeline recorded an ERROR message.

It did not record a successful completion message
for that execution.

The process exit code was inspected using:

```bash
echo $?
```

Observed result:

```text
1
```

This confirmed that the missing-file failure was
communicated to the operating system.

The original input file was not deleted or modified.

## 27. Temporary File Cleanup

The pipeline writes processed data to temporary files
before replacing the final output files.

```python
TEMP_CLEAN_FILE = CLEAN_FILE.with_suffix(".csv.tmp")

TEMP_REJECTED_FILE = REJECTED_FILE.with_suffix(".csv.tmp")
```

After successful processing:

```python
TEMP_CLEAN_FILE.replace(CLEAN_FILE)

TEMP_REJECTED_FILE.replace(REJECTED_FILE)
```

Temporary files are cleaned up using finally.

```python
finally:
    TEMP_CLEAN_FILE.unlink(missing_ok=True)

    TEMP_REJECTED_FILE.unlink(missing_ok=True)
```

This helps prevent unnecessary temporary files
from remaining after normal execution or exceptions.

The missing_ok parameter prevents FileNotFoundError
if the temporary file has already been removed.

Other errors, such as permission errors,
can still occur during cleanup.

This implementation assumes that only one pipeline
instance is running at a time.

## 28. Measuring Execution Time

Python's time module provides perf_counter()
for measuring elapsed execution time.

```python
import time

start_time = time.perf_counter()

# Execute pipeline operations.

end_time = time.perf_counter()

execution_time = end_time - start_time
```

The elapsed time can be recorded using logging.

```python
logging.info(
    "Execution time: %.3f seconds.",
    execution_time
)
```

Example observed during the NYC 311 lab:

```text
INFO - Execution time: 0.251 seconds.
```

Execution time may vary between runs and environments.

In our implementation, execution time is recorded
for successful processing before final cleanup.

## 29. Logging Best Practices

- Use appropriate severity levels.
- Include timestamps.
- Record pipeline start and completion.
- Include processed record counts.
- Record validation results.
- Log meaningful exception information.
- Avoid silently ignoring important exceptions.
- Do not report success after a fatal processing error.
- Avoid logging passwords, API keys, and access tokens.
- Avoid unnecessarily logging sensitive record contents.
- Avoid excessive per-record logging for large datasets.
- Measure execution time when appropriate.
- Use clear and consistent log messages.

Production pipelines may also require centralized
logging, structured logs, monitoring, and log rotation.

## 30. Python Terminology

| Name | Category |
|---|---|
| logging | Standard library module |
| time | Standard library module |
| basicConfig() | Logging module function |
| debug() | Logging module function |
| info() | Logging module function |
| warning() | Logging module function |
| error() | Logging module function |
| critical() | Logging module function |
| INFO | Logging module constant |
| WARNING | Logging module constant |
| ERROR | Logging module constant |
| perf_counter() | Time module function |
| FileNotFoundError | Built-in exception class |
| ValueError | Built-in exception class |
| TypeError | Built-in exception class |
| KeyError | Built-in exception class |
| JSONDecodeError | Exception class in the json module |
| try | Python keyword |
| except | Python keyword |
| else | Python keyword |
| finally | Python keyword |
| raise | Python keyword |
| as | Python keyword |
| unlink() | Path method |
| replace() | Path method |
| error | User-defined variable referencing an exception object |
| start_time | User-defined variable |
| execution_time | User-defined variable |

## 31. Importance in Data Engineering

Exception handling and logging support:

- Pipeline reliability
- Failure detection
- Data quality monitoring
- Operational visibility
- Troubleshooting
- Automated task execution
- Retry mechanisms
- Resource cleanup
- Performance monitoring
- Workflow orchestration

These concepts provide a foundation for working
with production-oriented tools such as databases,
APIs, Apache Airflow, and distributed data systems.

## Key Takeaways

- Exceptions represent problems that interrupt
  normal execution unless handled.
- try and except provide controlled exception handling.
- else executes after normal completion of the try block.
- finally is useful for cleanup operations.
- raise explicitly raises or re-raises an exception.
- Logging records application events.
- Logging severity does not automatically stop execution.
- Record-level errors and pipeline-level failures
  should be handled differently.
- Exit codes communicate process execution status.
- Temporary files help protect existing outputs.
- Execution time provides useful performance information.
- Reliable pipelines must report failures accurately.