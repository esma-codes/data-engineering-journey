# Files and Paths in Python

## 1. Overview

File handling is a fundamental skill in Data Engineering.

Data pipelines frequently need to:

- Locate input files.
- Create directories.
- Read raw data.
- Write processed data.
- Manage temporary files.
- Store execution logs.
- Check whether files exist.

Python provides built-in functions and standard library
modules for managing files and directories.

## 2. The pathlib Module

The pathlib module provides an object-oriented approach
to working with file system paths.

```python
from pathlib import Path
```

- pathlib is a standard library module.
- Path is a class provided by pathlib.
- A Path object represents a file system path.

```python
file_path = Path("data/raw/records.csv")
```

Creating a Path object does not create a physical file.

## 3. Current Working Directory

```python
from pathlib import Path

current_directory = Path.cwd()

print(current_directory)
```

`cwd()` is a class method that returns the current
working directory.

It is similar to the Linux `pwd` command.

## 4. Path Attributes

```python
file_path = Path("data/raw/nyc_311.csv")

print(file_path.name)
print(file_path.suffix)
print(file_path.stem)
print(file_path.parent)
```

Output:

```text
nyc_311.csv
.csv
nyc_311
data/raw
```

| Attribute | Description |
|---|---|
| name | File or directory name |
| suffix | File extension |
| stem | File name without its final extension |
| parent | Parent directory |

These are attributes, not methods.

Therefore, parentheses are not required.

## 5. Relative and Absolute Paths

### Relative Path

A relative path is interpreted relative to the
current working directory.

```python
file_path = Path("data/raw/records.csv")
```

### Absolute Path

An absolute path specifies the complete location
in the file system.

```python
file_path = Path("/home/user/project/data/records.csv")
```

### Resolving Paths

```python
absolute_path = file_path.resolve()
```

`resolve()` is a Path method that produces an absolute
path and resolves symbolic links.

## 6. Script-Based Paths

The current working directory may change depending on
where a Python script is executed.

Data pipelines should avoid unnecessary dependence
on the current working directory.

```python
BASE_DIR = Path(__file__).resolve().parent

RAW_FILE = BASE_DIR / "data" / "raw" / "nyc_311.csv"
```

- `__file__` is a special module variable containing
  the script's file path.
- `Path(__file__)` creates a Path object.
- `resolve()` produces an absolute path.
- `parent` returns the containing directory.
- `BASE_DIR` is a user-defined variable.

This approach was used in the NYC 311 ETL pipeline.

## 7. Joining Paths

The `/` operator can be used with Path objects
to combine path components.

```python
base_directory = Path("data")

raw_directory = base_directory / "raw"

file_path = raw_directory / "records.csv"

print(file_path)
```

Output:

```text
data/raw/records.csv
```

In this context, `/` performs path joining,
not mathematical division.

This behavior is provided through operator overloading.

## 8. Checking Files and Directories

```python
file_path = Path("data/raw/records.csv")

print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())
```

| Method | Description |
|---|---|
| exists() | Checks whether the path exists |
| is_file() | Checks whether the path is a file |
| is_dir() | Checks whether the path is a directory |

These methods return Boolean values.

Example:

```python
if not file_path.exists():
    raise FileNotFoundError(file_path)
```

## 9. Creating Directories

```python
output_directory = Path("data/processed")

output_directory.mkdir(
    parents=True,
    exist_ok=True
)
```

### Parameters

- `parents=True`: Creates missing parent directories.
- `exist_ok=True`: Does not raise an error if the
  target directory already exists.

Equivalent Linux command:

```bash
mkdir -p data/processed
```

### Pipeline Example

```python
CLEAN_FILE = BASE_DIR / "data" / "processed" / "cleaned.csv"

CLEAN_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)
```

This ensures that the output directory exists
before writing the processed data.

## 10. The open() Function

`open()` is a built-in Python function.

It opens a file and returns a file object.

```python
file = open("records.txt", "r", encoding="utf-8")

content = file.read()

print(content)

file.close()
```

Files should be closed after use to release
system resources.

## 11. File Modes

| Mode | Description |
|---|---|
| r | Opens an existing file for reading |
| w | Writes to a file, replacing existing content |
| a | Appends content to the end of a file |
| x | Creates a new file; fails if it already exists |
| b | Binary mode modifier |
| t | Text mode modifier; used by default |

### Read Mode

```python
with open("records.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Write Mode

```python
with open("records.txt", "w", encoding="utf-8") as file:
    file.write("New record\n")
```

Write mode creates the file if it does not exist.

If the file already exists, its previous content
is truncated when it is opened.

### Append Mode

```python
with open("records.txt", "a", encoding="utf-8") as file:
    file.write("Additional record\n")
```

Append mode preserves the existing content and writes
new content at the end of the file.

## 12. Context Managers

The `with` statement provides automatic resource
management.

```python
with open("records.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

The file is automatically closed when execution
leaves the with block, including when an exception occurs.

- `with` is a Python keyword.
- `as` is a Python keyword.
- `file` is a user-defined variable referencing
  the file object.

Context managers are preferred over manually opening
and closing files in most file-handling operations.

## 13. Managing Multiple Files

Multiple files can be managed in the same with statement.

```python
with (
    open("input.txt", "r", encoding="utf-8") as input_file,
    open("output.txt", "w", encoding="utf-8") as output_file
):
    for line in input_file:
        output_file.write(line)
```

Both files are automatically closed when execution
leaves the block.

This approach was used in the NYC 311 ETL pipeline
to manage input, cleaned, and rejected files.

## 14. Reading Files

### read()

Reads the entire remaining file content by default.

```python
with open("records.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### readline()

Reads one line at a time.

```python
with open("records.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
```

### readlines()

Reads the remaining lines into a list.

```python
with open("records.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

### Comparison

| Method | Return Type |
|---|---|
| read() | String |
| readline() | String |
| readlines() | List of strings |

These return types apply to files opened in text mode.

## 15. Memory-Efficient File Reading

Large files should not always be loaded entirely
into memory.

Instead, records can be processed incrementally.

```python
with open("large_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

The file object supports iteration.

This allows lines to be processed individually
without storing the entire file in memory.

### Comparison

| read() | Iterating over a file |
|---|---|
| Reads all remaining content by default | Processes lines incrementally |
| May consume significant memory | Usually consumes less memory |
| Useful for small files | Useful for large files |

This principle is important for scalable
Data Engineering pipelines.

## 16. Writing Files

### write()

Writes a string to a text file.

```python
with open("records.txt", "w", encoding="utf-8") as file:
    file.write("Record 1\n")
    file.write("Record 2\n")
```

### writelines()

Writes an iterable of strings to a file.

```python
records = [
    "Record 1\n",
    "Record 2\n",
    "Record 3\n"
]

with open("records.txt", "w", encoding="utf-8") as file:
    file.writelines(records)
```

Neither write() nor writelines() automatically adds
newline characters between records.

## 17. Character Encoding

Character encoding determines how text is represented
as bytes.

UTF-8 is a widely used encoding that supports
a broad range of Unicode characters.

```python
with open("records.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Explicitly specifying the encoding helps prevent
platform-dependent decoding problems.

The selected encoding must match the file's actual encoding.

## 18. Newline Handling

CSV files should generally be opened with `newline=""`
when using Python's csv module.

```python
with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:
    pass
```

This allows the csv module to manage newline characters
correctly, including newlines inside quoted fields.

## 19. String Cleaning with strip()

```python
value = "  Brooklyn  \n"

cleaned_value = value.strip()

print(cleaned_value)
```

Output:

```text
Brooklyn
```

`strip()` is a string method.

It removes leading and trailing whitespace by default.

Related methods:

- `lstrip()`: Removes leading whitespace.
- `rstrip()`: Removes trailing whitespace.

These methods do not remove whitespace located
inside the string.

### Data Validation Example

```python
unique_key = row["unique_key"].strip()

if unique_key == "":
    print("Missing unique key.")
```

## 20. Reading and Writing with pathlib

Path objects also provide convenient methods
for reading and writing small files.

### write_text()

```python
file_path = Path("message.txt")

file_path.write_text(
    "Pipeline completed.",
    encoding="utf-8"
)
```

### read_text()

```python
content = file_path.read_text(encoding="utf-8")

print(content)
```

`write_text()` replaces existing file content.

`read_text()` loads the entire file content into memory.

For large datasets, incremental processing with
open() is generally more appropriate.

## 21. Temporary File Paths

Temporary files help protect existing output files
while a new version is being generated.

```python
CLEAN_FILE = Path("data/processed/cleaned.csv")

TEMP_CLEAN_FILE = CLEAN_FILE.with_suffix(".csv.tmp")
```

Result:

```text
data/processed/cleaned.csv.tmp
```

`with_suffix()` returns a new Path object with
the specified suffix.

It does not rename or create the physical file.

## 22. Replacing Files

```python
TEMP_CLEAN_FILE.replace(CLEAN_FILE)
```

`replace()` is a Path method that renames the source
path to the target path, replacing an existing file
when permitted.

In our ETL pipeline, processed records are first
written to temporary files.

After processing and validation are complete,
the temporary files replace the final output files.

A successful replacement on the same file system
is atomic for an individual file.

Replacing multiple files separately does not provide
a single atomic transaction for all outputs.

## 23. Deleting Temporary Files

```python
TEMP_CLEAN_FILE.unlink(missing_ok=True)
```

`unlink()` removes a file or symbolic link.

`missing_ok=True` prevents FileNotFoundError
when the target does not exist.

It does not suppress other errors, such as
permission errors.

### Automatic Cleanup

```python
try:
    # Process data and write temporary files.
    pass

finally:
    TEMP_CLEAN_FILE.unlink(missing_ok=True)
```

The finally block normally executes after the try block,
whether an exception occurs or not.

However, forced process termination or power loss
may prevent cleanup from running.

## 24. Python Terminology

| Name | Category |
|---|---|
| pathlib | Standard library module |
| Path | Class |
| open() | Built-in function |
| cwd() | Path class method |
| resolve() | Path method |
| exists() | Path method |
| is_file() | Path method |
| is_dir() | Path method |
| mkdir() | Path method |
| with_suffix() | Path method |
| replace() | Path method |
| unlink() | Path method |
| read_text() | Path method |
| write_text() | Path method |
| name | Path attribute |
| suffix | Path attribute |
| stem | Path attribute |
| parent | Path attribute |
| read() | File object method |
| readline() | File object method |
| readlines() | File object method |
| write() | File object method |
| writelines() | File object method |
| close() | File object method |
| strip() | String method |
| with | Keyword |
| as | Keyword |
| finally | Keyword |
| __file__ | Special module variable |

## 25. Linux and Python Comparison

| Linux | Python |
|---|---|
| pwd | Path.cwd() |
| mkdir -p | Path.mkdir(parents=True, exist_ok=True) |
| cat file.txt | Path.read_text() |
| rm file.txt | Path.unlink() |
| mv source target | Path.rename() or Path.replace() |
| test -f file.txt | Path.is_file() |
| test -d directory | Path.is_dir() |

These operations have similar purposes, although
their exact behavior may differ.

## 26. Importance in Data Engineering

File and path management supports:

- Raw data ingestion
- Directory organization
- Memory-efficient processing
- ETL pipeline development
- Reliable output generation
- Temporary file management
- Resource cleanup
- Cross-platform code development
- Reproducible project execution

## Key Takeaways

- pathlib provides object-oriented path management.
- Path objects represent file system paths.
- Absolute and script-based paths improve reproducibility.
- Context managers automatically close files.
- Write mode replaces existing file content.
- Append mode preserves existing content.
- Incremental reading improves memory efficiency.
- UTF-8 is a widely used text encoding.
- Temporary files help protect existing pipeline outputs.
- Atomic file replacement improves output reliability.
- Cleanup operations remove unnecessary temporary files.