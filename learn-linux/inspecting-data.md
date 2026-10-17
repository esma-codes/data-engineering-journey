# Inspecting and Processing Data

Linux provides simple command-line tools for quickly inspecting and analyzing files.

These tools are especially useful in data engineering when working with:

- CSV files
- log files
- text files
- pipeline outputs
- large datasets

The goal is often to inspect a file without opening the entire dataset in an editor.

---

# `cat` — Display File Content

`cat` can display the entire content of a file in the terminal.

Example:

```bash
cat raw/customers.csv
```

Example output:

```text
id,name
1,Esma
2,Ayse
```

`cat` is useful for small files.

For very large files, commands such as `head`, `tail`, and `less` are usually more practical.

---

# `head` — View the Beginning of a File

`head` displays the first lines of a file.

Example:

```bash
head raw/customers.csv
```

By default, it shows the first 10 lines.

To choose the number of lines:

```bash
head -n 2 raw/customers.csv
```

This shows only the first 2 lines.

## Data Engineering Use

When I receive a new dataset, I can quickly inspect:

- column names
- file structure
- sample values

without opening the entire file.

---

# `tail` — View the End of a File

`tail` displays the last lines of a file.

Example:

```bash
tail raw/customers.csv
```

By default, it shows the last 10 lines.

To show only the last line:

```bash
tail -n 1 raw/customers.csv
```

---

## Following a File

A useful option is:

```bash
tail -f pipeline.log
```

`-f` means **follow**.

It keeps watching the file and displays new lines as they are added.

This is useful for monitoring logs while a pipeline or application is running.

Example:

```text
Pipeline started...
Reading data...
Loaded 1000 rows...
ERROR: database connection failed
```

---

# `less` — Read Large Files

`less` allows me to inspect a file without printing the entire file at once.

Example:

```bash
less raw/customers.csv
```

I can move through the file inside the terminal.

To exit:

```text
q
```

This is useful when a file is too large for `cat`.

---

# `wc` — Count Lines, Words, and Bytes

`wc` means **word count**.

Example:

```bash
wc raw/customers.csv
```

It can display information such as:

```text
lines  words  bytes  filename
```

---

## Count Lines

The option I will probably use most often in data work is:

```bash
wc -l raw/customers.csv
```

`-l` means **lines**.

Example output:

```text
10001 raw/customers.csv
```

This means the file contains 10,001 lines.

## Data Engineering Use

I can compare row counts before and after processing.

Example:

```text
raw data       -> 10001 lines
processed data -> 9500 lines
```

If the numbers are different, I should understand why.

---

# `grep` — Search Inside Files

`grep` searches for text or patterns inside files.

Example:

```bash
grep "Esma" raw/customers.csv
```

This displays lines containing:

```text
Esma
```

---

## Ignore Uppercase and Lowercase

Linux text matching is normally case-sensitive.

For example:

```text
Esma
esma
ESMA
```

are different.

To ignore case:

```bash
grep -i "esma" raw/customers.csv
```

`-i` means **ignore case**.

---

## Count Matching Lines

```bash
grep -c "Esma" raw/customers.csv
```

`-c` means **count**.

It shows how many lines matched.

---

## Show Lines That Do Not Match

```bash
grep -v "Esma" raw/customers.csv
```

`-v` means the opposite selection.

It shows lines that do **not** contain `Esma`.

---

## Data Engineering Use

`grep` is especially useful for searching logs.

Example:

```bash
grep "ERROR" pipeline.log
```

This allows me to quickly find error messages produced by a pipeline.

---

# `sort` — Sort Lines

`sort` sorts the lines of a file.

Example:

```bash
sort names.txt
```

If the file contains:

```text
Ayse
Esma
Mehmet
Ayse
```

the result becomes:

```text
Ayse
Ayse
Esma
Mehmet
```

---

# `uniq` — Remove Adjacent Duplicate Lines

`uniq` removes repeated lines that are next to each other.

Because of this, it is commonly used together with `sort`.

Example:

```bash
sort names.txt | uniq
```

Result:

```text
Ayse
Esma
Mehmet
```

---

## Count Duplicate Values

```bash
sort names.txt | uniq -c
```

Example result:

```text
2 Ayse
2 Esma
1 Mehmet
```

This shows how many times each value appears.

---

# Commands I Tested

```bash
cat raw/customers.csv

head raw/customers.csv
head -n 2 raw/customers.csv

tail raw/customers.csv
tail -n 1 raw/customers.csv

less raw/customers.csv

wc raw/customers.csv
wc -l raw/customers.csv

grep "Esma" raw/customers.csv
grep -i "esma" raw/customers.csv
grep -c "Esma" raw/customers.csv
grep -v "Esma" raw/customers.csv

sort names.txt
sort names.txt | uniq
sort names.txt | uniq -c
```

---

# What I Learned

- `cat` displays an entire small file.
- `head` shows the beginning of a file.
- `tail` shows the end of a file.
- `tail -f` can monitor a file while it changes.
- `less` helps inspect larger files.
- `wc -l` counts lines.
- `grep` searches for matching text.
- `grep -i` ignores letter case.
- `grep -v` shows non-matching lines.
- `sort` sorts lines.
- `uniq` removes adjacent duplicate lines.
- `uniq -c` counts repeated values.

---

# Data Engineering Connection

These commands allow me to inspect data directly from the terminal.

Instead of opening a large dataset manually, I can quickly answer questions such as:

```text
What does this file look like?
How many lines are there?
What are the first records?
What are the latest records?
Does this log contain errors?
How many times does a value appear?
Are there duplicate values?
```

These simple Linux tools can be useful for debugging and validating data pipelines.