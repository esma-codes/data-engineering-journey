# CSV, JSON and JSON Lines in Python

## 1. Overview

Data formats define how information is structured,
stored, and exchanged between systems.

Common data formats in Data Engineering include:

- CSV
- JSON
- JSON Lines (JSONL)
- Parquet
- Avro

This section focuses on CSV, JSON, and JSON Lines
using Python's standard library.

## 2. CSV (Comma-Separated Values)

CSV is a text-based format commonly used to store
tabular data.

Example:

```csv
unique_key,borough,status
101,BROOKLYN,Closed
102,MANHATTAN,Open
103,QUEENS,In Progress
```

### CSV Terminology

| Term | Description |
|---|---|
| Header | Column names |
| Row | A record in the dataset |
| Column | A field shared by records |
| Delimiter | Character separating fields |
| Field | An individual value |

CSV is commonly used for:

- Data exports
- Tabular datasets
- Data ingestion
- Data exchange between systems
- ETL pipelines

CSV does not inherently preserve Python data types.

## 3. The csv Module

Python provides a standard library module
for working with CSV files.

```python
import csv
```

No external package installation is required.

Main components:

- csv.reader()
- csv.writer()
- csv.DictReader
- csv.DictWriter

## 4. Reading CSV with csv.reader()

The reader() function returns a reader object
that produces rows as lists.

```python
import csv

with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['unique_key', 'borough', 'status']
['101', 'BROOKLYN', 'Closed']
['102', 'MANHATTAN', 'Open']
['103', 'QUEENS', 'In Progress']
```

By default, CSV field values are read as strings.

The header is also returned as a row.

## 5. Skipping the Header

The next() built-in function can retrieve
the first row before iteration.

```python
with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        print(row)
```

The header is stored separately from the data records.

For an empty file, next(reader) raises StopIteration.

A default value can be provided:

```python
header = next(reader, None)
```

## 6. Reading CSV with DictReader

DictReader is a class provided by the csv module.

It maps each CSV row to a dictionary using
the column names as keys.

```python
import csv

with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Output:

```text
{'unique_key': '101', 'borough': 'BROOKLYN', 'status': 'Closed'}
{'unique_key': '102', 'borough': 'MANHATTAN', 'status': 'Open'}
{'unique_key': '103', 'borough': 'QUEENS', 'status': 'In Progress'}
```

Individual fields can be accessed by column name.

```python
print(row["borough"])
print(row["status"])
```

This approach improves readability because column
positions do not need to be memorized.

## 7. Accessing Column Names

DictReader provides the fieldnames attribute.

```python
reader = csv.DictReader(file)

fieldnames = reader.fieldnames

print(fieldnames)
```

Output:

```text
['unique_key', 'borough', 'status']
```

fieldnames is an attribute, not a method.

It was used in the NYC 311 pipeline for:

- Schema validation
- Preserving column names
- Creating output CSV headers

## 8. reader() vs DictReader

| csv.reader() | csv.DictReader |
|---|---|
| Module function | Class |
| Returns rows as lists | Returns rows as dictionaries |
| Uses column indexes | Uses column names |
| Header is returned as a row | Header becomes dictionary keys |

Example:

```python
# Using csv.reader()
borough = row[1]

# Using csv.DictReader
borough = row["borough"]
```

DictReader is particularly useful when working
with datasets containing many columns.

## 9. Writing CSV with csv.writer()

```python
import csv

with open(
    "records.csv",
    "w",
    encoding="utf-8",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "unique_key",
        "borough",
        "status"
    ])

    writer.writerow([
        101,
        "BROOKLYN",
        "Closed"
    ])
```

writerow() writes a single row.

## 10. Writing Multiple Rows

The writerows() method writes multiple rows
from an iterable.

```python
records = [
    [101, "BROOKLYN", "Closed"],
    [102, "MANHATTAN", "Open"],
    [103, "QUEENS", "In Progress"]
]

with open(
    "records.csv",
    "w",
    encoding="utf-8",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "unique_key",
        "borough",
        "status"
    ])

    writer.writerows(records)
```

| Method | Description |
|---|---|
| writerow() | Writes one record |
| writerows() | Writes multiple records |

writerows() can consume an iterable incrementally.

It does not require all records to be stored
in a list beforehand.

## 11. Writing CSV with DictWriter

DictWriter is a class provided by the csv module.

It writes dictionaries as CSV rows.

```python
import csv

fieldnames = [
    "unique_key",
    "borough",
    "status"
]

records = [
    {
        "unique_key": 101,
        "borough": "BROOKLYN",
        "status": "Closed"
    },
    {
        "unique_key": 102,
        "borough": "MANHATTAN",
        "status": "Open"
    }
]

with open(
    "records.csv",
    "w",
    encoding="utf-8",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(records)
```

### Important Components

| Component | Description |
|---|---|
| DictWriter | Class |
| writer | User-defined variable referencing the writer object |
| fieldnames | Parameter defining the output columns |
| writeheader() | Writes column names |
| writerow() | Writes one dictionary record |
| writerows() | Writes multiple dictionary records |

## 12. Memory-Efficient CSV Processing

Loading all records into memory:

```python
with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.DictReader(file)

    records = list(reader)
```

This approach creates a list containing all records.

Incremental processing:

```python
with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["unique_key"])
```

The second approach processes records one at a time.

It avoids creating a complete list of the dataset.

This principle was used in the NYC 311 ETL pipeline.

## 13. Missing CSV Values

CSV files may contain empty fields.

```csv
unique_key,borough,status
101,BROOKLYN,Closed
102,,Open
```

An empty CSV field is normally read as an empty string.

```python
borough = row["borough"].strip()

if borough == "":
    print("Missing borough.")
```

An empty string is different from None.

If a malformed CSV row contains fewer fields
than expected, DictReader may return None
for missing fields.

A more defensive approach is:

```python
borough = (row.get("borough") or "").strip()
```

Data validation rules should determine whether
a missing value is acceptable.

## 14. CSV Delimiters and Quoting

Although commas are common delimiters,
CSV-like files may use other separators.

```python
reader = csv.reader(file, delimiter=";")
```

Example:

```text
101;BROOKLYN;Closed
102;MANHATTAN;Open
```

Quoted fields may contain commas:

```csv
101,"Noise, Residential",Closed
```

Python's csv module handles quoted fields correctly.

Avoid manually parsing CSV using:

```python
line.split(",")
```

This approach can fail when fields contain
quoted delimiters or embedded newlines.

## 15. JSON (JavaScript Object Notation)

JSON is a text-based format for representing
structured data.

Example:

```json
{
    "unique_key": 101,
    "borough": "BROOKLYN",
    "status": "Closed",
    "validated": true,
    "closed_date": null
}
```

JSON supports:

- Objects
- Arrays
- Strings
- Numbers
- Boolean values
- Null values

JSON is commonly used in:

- REST APIs
- Configuration files
- Data exchange
- Nested datasets
- Web applications
- Data ingestion pipelines

## 16. JSON vs Python Data Types

| JSON | Python |
|---|---|
| Object | dict |
| Array | list |
| String | str |
| Integer number | int |
| Decimal number | float |
| true | True |
| false | False |
| null | None |

JSON and Python dictionaries are related,
but they are not the same thing.

JSON is a data representation format.

A Python dictionary is an in-memory data structure.

JSON object keys must be strings.

## 17. Nested JSON

Unlike CSV, JSON naturally supports nested structures.

```json
{
    "unique_key": 101,
    "location": {
        "borough": "BROOKLYN",
        "incident_zip": "11226"
    },
    "request": {
        "status": "Closed",
        "complaint_type": "Noise"
    }
}
```

After converting the JSON into a Python dictionary,
nested fields can be accessed as follows:

```python
borough = record["location"]["borough"]

status = record["request"]["status"]
```

Nested data is frequently encountered in API responses.

## 18. The json Module

Python provides a standard library module
for working with JSON.

```python
import json
```

Four important functions:

- json.load()
- json.loads()
- json.dump()
- json.dumps()

## 19. Reading JSON Files with load()

load() reads JSON from a file-like object and
converts it into Python objects.

```python
import json

with open(
    "records.json",
    "r",
    encoding="utf-8"
) as file:

    records = json.load(file)

print(records)
```

The resulting Python type depends on the
structure of the JSON document.

A JSON object becomes a dictionary.

A JSON array becomes a list.

## 20. Reading JSON Strings with loads()

loads() parses a JSON string.

```python
import json

json_text = '''
{
    "unique_key": 101,
    "borough": "BROOKLYN",
    "validated": true
}
'''

record = json.loads(json_text)

print(record["borough"])
print(record["validated"])
```

Output:

```text
BROOKLYN
True
```

The letter "s" in loads() can be remembered
as "string".

## 21. Writing JSON Files with dump()

dump() serializes Python objects and writes
JSON directly to a file-like object.

```python
import json

record = {
    "unique_key": 101,
    "borough": "BROOKLYN",
    "validated": True
}

with open(
    "record.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        record,
        file,
        indent=4,
        ensure_ascii=False
    )
```

### Parameters

- indent=4: Formats nested JSON using four spaces.
- ensure_ascii=False: Allows Unicode characters
  to be written without unnecessary ASCII escaping.

## 22. Creating JSON Strings with dumps()

dumps() serializes a Python object into a JSON string.

```python
import json

record = {
    "unique_key": 101,
    "borough": "BROOKLYN",
    "validated": True
}

json_text = json.dumps(record, indent=4)

print(json_text)
```

The return value is a Python string.

No physical file is created by dumps().

## 23. JSON Functions Comparison

| Function | Input | Result |
|---|---|---|
| json.load() | File-like object containing JSON | Python object |
| json.loads() | JSON string | Python object |
| json.dump() | Python object and file-like object | Writes JSON to the file |
| json.dumps() | Python object | JSON string |

### Memory Aid

- load: Read JSON from a file.
- loads: Read JSON from a string.
- dump: Write JSON to a file.
- dumps: Create a JSON string.

All four are module functions provided by
Python's json module.

## 24. Serialization and Deserialization

### Serialization

Converting a Python object into a representation
that can be stored or transmitted.

```python
record = {"unique_key": 101}

json_text = json.dumps(record)
```

### Deserialization

Converting a serialized representation back
into Python objects.

```python
record = json.loads(json_text)
```

Data flow:

```text
Python object
     |
     | Serialization
     v
JSON representation
     |
     | Deserialization
     v
Python object
```

These concepts are fundamental when working
with APIs, files, and distributed systems.

## 25. Converting CSV to JSON

```python
import csv
import json

with open(
    "records.csv",
    "r",
    encoding="utf-8",
    newline=""
) as csv_file:

    reader = csv.DictReader(csv_file)

    records = list(reader)

with open(
    "records.json",
    "w",
    encoding="utf-8"
) as json_file:

    json.dump(
        records,
        json_file,
        indent=4,
        ensure_ascii=False
    )
```

Data flow:

```text
CSV file
   |
   | csv.DictReader
   v
Python dictionaries
   |
   | list()
   v
List of dictionaries
   |
   | json.dump()
   v
JSON file
```

CSV values remain strings unless they are
explicitly converted into other data types.

For example:

```python
row["unique_key"] = int(row["unique_key"])
```

Type conversion should only be performed when
appropriate for the dataset and its schema.

Identifiers do not always need to be integers.

## 26. Converting JSON to CSV

This example assumes that the JSON file contains
a non-empty list of dictionaries with consistent fields.

```python
import json
import csv

with open(
    "records.json",
    "r",
    encoding="utf-8"
) as json_file:

    records = json.load(json_file)

fieldnames = list(records[0].keys())

with open(
    "records.csv",
    "w",
    encoding="utf-8",
    newline=""
) as csv_file:

    writer = csv.DictWriter(
        csv_file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(records)
```

Data flow:

```text
JSON file
   |
   | json.load()
   v
List of dictionaries
   |
   | csv.DictWriter
   v
CSV file
```

In real pipelines, empty datasets, inconsistent keys,
and nested JSON structures must be handled explicitly.

## 27. Limitations of Standard JSON Processing

Consider a JSON file containing millions of records.

```python
records = json.load(file)
```

The complete JSON document is parsed into
Python objects in memory.

This may cause:

- High memory consumption
- Increased processing time
- Memory-related failures

For large datasets, alternative formats
or incremental JSON parsers may be preferable.

JSON Lines is one useful alternative.

## 28. JSON Lines (JSONL)

JSON Lines is also commonly called
Newline-Delimited JSON (NDJSON).

Each line contains an independent, valid JSON value.

Example:

```json
{"unique_key": 101, "borough": "BROOKLYN"}
{"unique_key": 102, "borough": "MANHATTAN"}
{"unique_key": 103, "borough": "QUEENS"}
```

Common file extensions:

- .jsonl
- .ndjson

Unlike a standard JSON array, JSON Lines does not
require surrounding square brackets or commas
between records.

## 29. Reading JSON Lines

```python
import json

with open(
    "records.jsonl",
    "r",
    encoding="utf-8"
) as file:

    for line in file:

        record = json.loads(line)

        print(record["borough"])
```

Each line is processed independently.

This allows large datasets to be processed
without loading the complete file into memory.

A blank line is not a valid JSON value.

Malformed lines require explicit error handling.

## 30. Writing JSON Lines

```python
import json

records = [
    {"unique_key": 101, "borough": "BROOKLYN"},
    {"unique_key": 102, "borough": "MANHATTAN"},
    {"unique_key": 103, "borough": "QUEENS"}
]

with open(
    "records.jsonl",
    "w",
    encoding="utf-8"
) as file:

    for record in records:

        json_text = json.dumps(
            record,
            ensure_ascii=False
        )

        file.write(json_text + "\n")
```

Each record is serialized independently.

The newline character separates JSON records.

Unlike standard formatted JSON, each JSONL record
should remain on a single physical line.

## 31. Streaming CSV to JSON Lines

CSV records can be converted to JSON Lines
without loading the entire dataset into memory.

```python
import csv
import json

with (
    open(
        "nyc_311_10000.csv",
        "r",
        encoding="utf-8",
        newline=""
    ) as csv_file,

    open(
        "nyc_311.jsonl",
        "w",
        encoding="utf-8"
    ) as jsonl_file
):

    reader = csv.DictReader(csv_file)

    for row in reader:

        jsonl_file.write(
            json.dumps(row, ensure_ascii=False) + "\n"
        )
```

Data flow:

```text
CSV input
    |
    v
Read one record
    |
    v
Convert dictionary to JSON
    |
    v
Write one JSONL record
    |
    v
Repeat
```

This is an example of incremental,
memory-efficient format conversion.

## 32. CSV vs JSON vs JSONL

| Feature | CSV | JSON | JSONL |
|---|---|---|---|
| Text-based | Yes | Yes | Yes |
| Tabular data | Excellent | Supported | Supported |
| Nested data | Not native | Yes | Yes |
| Native value types | No | Yes | Yes |
| Incremental processing | Easy | Requires suitable structure or parser | Easy |
| API responses | Sometimes | Very common | Sometimes |
| Event and log records | Possible | Possible | Common |

The appropriate format depends on the data structure,
processing requirements, and target system.

## 33. Python Terminology

| Name | Category |
|---|---|
| csv | Standard library module |
| json | Standard library module |
| reader() | csv module function |
| writer() | csv module function |
| DictReader | Class |
| DictWriter | Class |
| fieldnames | DictReader attribute / DictWriter parameter |
| writeheader() | DictWriter method |
| writerow() | Writer method |
| writerows() | Writer method |
| load() | json module function |
| loads() | json module function |
| dump() | json module function |
| dumps() | json module function |
| JSONDecodeError | Exception class in the json module |
| open() | Built-in function |
| next() | Built-in function |
| list | Built-in type |
| int | Built-in type |
| keys() | Dictionary method |
| get() | Dictionary method |
| strip() | String method |
| write() | File object method |

## 34. Application in the NYC 311 Pipeline

The NYC 311 pipeline uses CSV files as both
input and output formats.

```text
Raw CSV
   |
   v
csv.DictReader
   |
   v
Schema Validation
   |
   v
Data Quality Validation
   |
   +--------------------+
   |                    |
   v                    v
Valid Records      Invalid Records
   |                    |
   v                    v
csv.DictWriter     csv.DictWriter
   |                    |
   v                    v
cleaned.csv        rejected.csv
```

The pipeline processes records incrementally.

It preserves the original column structure
and separates records according to validation rules.

The same fundamental concepts can later be applied
to API ingestion, databases, and distributed pipelines.

## 35. Importance in Data Engineering

Understanding data formats supports:

- API data ingestion
- File-based pipelines
- Data serialization
- Data deserialization
- Data transformation
- Schema validation
- Data exchange between systems
- Memory-efficient processing
- Large dataset management

## Key Takeaways

- CSV is commonly used for tabular data.
- JSON supports structured and nested data.
- JSON Lines stores independent JSON values per line.
- DictReader converts CSV rows into dictionaries.
- DictWriter writes dictionaries as CSV records.
- load() and loads() deserialize JSON.
- dump() and dumps() serialize Python objects.
- CSV values are normally read as strings.
- Standard json.load() materializes the parsed document.
- JSONL supports incremental record processing.
- Processing records one at a time improves
  memory efficiency.
- Data format selection is an important engineering decision.