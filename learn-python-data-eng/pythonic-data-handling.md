# Pythonic Data Handling

## 1. Overview

Python provides powerful tools for processing, transforming,
and filtering data efficiently.

These concepts are particularly important in Data Engineering,
where pipelines may need to process large datasets without
loading all records into memory.

## 2. Iterables and Iterators

### Iterable

An iterable is an object that can be iterated over.

Examples:

- Lists
- Tuples
- Strings
- Dictionaries
- Sets

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

### Iterator

An iterator is an object that produces elements one at a time.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

- `iter()` is a built-in function that returns an iterator.
- `next()` is a built-in function that retrieves the next item.
- `StopIteration` is a built-in exception raised when the
  iterator is exhausted.

Every iterator is iterable, but not every iterable is an iterator.

## 3. Generators and yield

A generator produces values lazily, one at a time.

A generator function uses the `yield` keyword instead of
returning all its results at once.

```python
def generate_numbers():
    for number in range(5):
        yield number

generator = generate_numbers()

for number in generator:
    print(number)
```

### How yield works

1. The generator function is called.
2. A generator object is created.
3. Execution starts when the next value is requested.
4. `yield` produces a value and suspends execution.
5. Execution resumes when another value is requested.

### yield vs return

| yield | return |
|---|---|
| Suspends execution | Ends function execution |
| Preserves execution state | Does not preserve suspended state |
| Can produce multiple values over time | Returns a result once |
| Supports lazy processing | Returns a result immediately when reached |

### Data Engineering Example

```python
def read_records(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()
```

This generator allows records to be processed one at a time.

Generators can reduce memory consumption when data is generated
or read incrementally instead of being fully loaded into memory.

## 4. List Comprehensions

List comprehensions provide a concise way to create lists.

Traditional approach:

```python
squares = []

for number in range(5):
    squares.append(number ** 2)
```

Pythonic approach:

```python
squares = [number ** 2 for number in range(5)]
```

### Filtering

```python
numbers = [10, 15, 20, 25, 30]

filtered = [number for number in numbers if number >= 20]
```

Output:

```text
[20, 25, 30]
```

A list comprehension creates the entire resulting list in memory.

## 5. Dictionary Comprehensions

Dictionary comprehensions create dictionaries using
a concise expression.

```python
numbers = [1, 2, 3, 4]

squares = {number: number ** 2 for number in numbers}
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

### Data Transformation Example

```python
records = {
    "brooklyn": 120,
    "manhattan": 150,
    "queens": 90
}

normalized = {
    borough.upper(): count
    for borough, count in records.items()
}
```

Dictionary comprehensions are useful for transforming
structured data.

## 6. Generator Expressions

Generator expressions are similar to list comprehensions,
but they produce values lazily.

```python
numbers = (number ** 2 for number in range(1000000))
```

Unlike a list comprehension, this expression creates
a generator object instead of a complete list.

| List comprehension | Generator expression |
|---|---|
| Uses square brackets | Uses parentheses |
| Creates a list | Creates a generator |
| Eager evaluation | Lazy evaluation |
| Stores all results | Produces values on demand |

## 7. Unpacking

Unpacking allows values from an iterable to be assigned
to multiple variables.

```python
record = ("Brooklyn", 120)

borough, count = record
```

### Extended Unpacking

```python
numbers = [10, 20, 30, 40, 50]

first, *remaining = numbers
```

Output:

```text
first = 10
remaining = [20, 30, 40, 50]
```

### Iterable Unpacking

```python
first_batch = [1, 2, 3]
second_batch = [4, 5, 6]

combined = [*first_batch, *second_batch]
```

### Dictionary Unpacking

```python
record = {
    "id": 101,
    "borough": "Brooklyn"
}

metadata = {
    "source": "NYC 311",
    "validated": True
}

combined = {**record, **metadata}
```

Dictionary unpacking is useful for combining records
and adding metadata.

If dictionaries contain the same key, the later value
overwrites the earlier value.

## 8. Lambda Functions

A lambda is a small anonymous function containing
a single expression.

Traditional function:

```python
def square(number):
    return number ** 2
```

Lambda equivalent:

```python
square = lambda number: number ** 2
```

A lambda automatically returns the result of its expression.

`lambda` is a Python keyword.

## 9. map()

The `map()` built-in function applies a function
to each item of an iterable.

```python
boroughs = ["brooklyn", "queens", "manhattan"]

result = map(lambda borough: borough.upper(), boroughs)

print(list(result))
```

Output:

```text
['BROOKLYN', 'QUEENS', 'MANHATTAN']
```

In Python 3, `map()` returns a lazy iterator.

Common use cases:

- Data transformation
- Text normalization
- Type conversion
- Applying operations to multiple records

## 10. filter()

The `filter()` built-in function selects elements
that satisfy a condition.

```python
records = [
    {"id": 101, "status": "Closed"},
    {"id": 102, "status": "Open"},
    {"id": 103, "status": "Closed"}
]

closed_records = filter(
    lambda record: record["status"] == "Closed",
    records
)

print(list(closed_records))
```

In Python 3, `filter()` returns a lazy iterator.

Common use cases:

- Selecting valid records
- Filtering unwanted data
- Applying business rules

## 11. Eager vs Lazy Evaluation

### Eager Evaluation

Results are computed and stored immediately.

```python
numbers = [number for number in range(1000000)]
```

### Lazy Evaluation

Results are produced when requested.

```python
numbers = (number for number in range(1000000))
```

Lazy evaluation is especially useful when processing
large datasets and streaming data.

Converting a lazy iterator into a list materializes
its remaining elements in memory.

## 12. Context Managers

Context managers manage resources automatically.

The `with` keyword is commonly used when working with files.

```python
with open("records.csv", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

The file is automatically closed when execution
leaves the with block, including when an exception occurs.

## 13. Python Terminology

| Name | Category |
|---|---|
| iter() | Built-in function |
| next() | Built-in function |
| map() | Built-in function |
| filter() | Built-in function |
| open() | Built-in function |
| range | Built-in type |
| list | Built-in type |
| dict | Built-in type |
| StopIteration | Built-in exception class |
| yield | Keyword |
| return | Keyword |
| lambda | Keyword |
| with | Keyword |
| append() | List method |
| items() | Dictionary method |
| upper() | String method |
| strip() | String method |

## 14. Importance in Data Engineering

These concepts support:

- Memory-efficient data processing
- Incremental file reading
- Data transformation
- Data filtering
- Data normalization
- Resource management
- Scalable pipeline development

## Key Takeaways

- Iterators produce values one at a time.
- Generators support lazy evaluation.
- The yield keyword suspends generator execution.
- Comprehensions simplify data transformations.
- Unpacking simplifies structured data handling.
- map() transforms elements.
- filter() selects elements.
- Context managers provide automatic resource cleanup.
- Memory efficiency is an important consideration when
  designing data pipelines.