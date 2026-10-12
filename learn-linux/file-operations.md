# File Operations

Linux file operations are important in data engineering because data pipelines frequently create, copy, move, rename, and delete files.

A simple data workflow can look like this:

```text
raw/
   ↓
processed/
   ↓
archive/
```

---

## Creating Directories — `mkdir`

`mkdir` means **make directory**.

It creates a new directory.

Example:

```bash
mkdir raw
mkdir processed
mkdir archive
```

This creates:

```text
raw/
processed/
archive/
```

---

## Creating Empty Files — `touch`

`touch` can create an empty file if the file does not already exist.

Example:

```bash
touch raw/customers.csv
```

This creates:

```text
raw/
└── customers.csv
```

`touch` can also update the timestamp of an existing file.

---

# Copying Files — `cp`

`cp` means **copy**.

Example:

```bash
cp raw/customers.csv processed/customers.csv
```

After this command:

```text
raw/
└── customers.csv

processed/
└── customers.csv
```

The original file still exists.

### Key Idea

```text
cp
↓
source stays
+
a copy is created
```

This is useful when raw data should be preserved while another copy is processed.

---

# Moving Files — `mv`

`mv` means **move**.

Example:

```bash
mv processed/customers.csv archive/customers.csv
```

The file disappears from `processed` and appears in `archive`.

```text
Before:

processed/
└── customers.csv

archive/


After:

processed/

archive/
└── customers.csv
```

---

## Renaming Files with `mv`

`mv` can also rename a file.

Example:

```bash
mv archive/customers.csv archive/customers-old.csv
```

The file stays in the same directory but gets a new name.

### `cp` vs `mv`

```text
cp → creates a copy, original stays

mv → moves the file, original location becomes empty
```

---

# Removing Files — `rm`

`rm` means **remove**.

Example:

```bash
rm file.txt
```

Linux normally does not use a recycle bin when files are removed from the command line.

Because of this, I should be careful when using `rm`.

---

## Interactive Removal

A safer option while learning is:

```bash
rm -i file.txt
```

`-i` means **interactive**.

Linux asks for confirmation before deleting the file.

Example:

```text
rm: remove regular file 'file.txt'?
```

I can answer:

```text
y
```

to delete it.

---

# Wildcards and Patterns

Wildcards allow me to work with multiple filenames without writing every filename manually.

---

## `*` — Zero or More Characters

`*` can match zero or more characters.

Example:

```bash
ls raw/*.csv
```

This means:

> Show files inside `raw` whose names end with `.csv`.

It could match:

```text
customers.csv
orders.csv
products.csv
data10.csv
```

but not:

```text
notes.txt
```

---

## `?` — Exactly One Character

`?` represents exactly one character.

Example:

```bash
ls raw/data?.csv
```

It can match:

```text
data1.csv
data2.csv
data9.csv
```

but not:

```text
data10.csv
```

because `10` contains two characters.

---

## `[]` — One Character from a Set

Square brackets match one character from the given set.

Example:

```bash
ls raw/data[12].csv
```

This means:

```text
data + (1 or 2) + .csv
```

It can match:

```text
data1.csv
data2.csv
```

but not:

```text
data10.csv
data12.csv
data21.csv
```

because `[12]` represents only one character at that exact position.

---

## Character Ranges

A range can also be used:

```bash
ls raw/data[0-9].csv
```

This means:

> Match one digit between 0 and 9.

Examples:

```text
data0.csv
data1.csv
data5.csv
data9.csv
```

`data10.csv` does not match because `[0-9]` represents only one digit.

---

# Brace Expansion — `{}`

Brace expansion is different from wildcards.

Example:

```bash
touch raw/test_{1..3}.csv
```

Bash expands this into:

```text
raw/test_1.csv
raw/test_2.csv
raw/test_3.csv
```

Another example:

```bash
touch raw/file_{a,b,c}.txt
```

becomes:

```text
file_a.txt
file_b.txt
file_c.txt
```

### Wildcards vs Brace Expansion

```text
* ? []  → match existing filenames

{}      → generate multiple pieces of text
```

---

# Relative Paths in File Operations

I often used paths such as:

```text
raw/customers.csv
```

This is a **relative path** because it starts from my current directory.

An absolute version could look like:

```text
/home/esma_nur/data-engineering-journey/learn-linux/file-operations-lab/raw/customers.csv
```

---

# Commands I Tested

```bash
mkdir raw
mkdir processed
mkdir archive

touch raw/customers.csv

cp raw/customers.csv processed/customers.csv

mv processed/customers.csv archive/customers.csv

mv archive/customers.csv archive/customers-old.csv

rm -i archive/customers-old.csv

ls raw/*
ls raw/*.csv
ls raw/data?.csv
ls raw/data[12].csv
ls raw/data[0-9].csv

touch raw/test_{1..3}.csv
```

---

# What I Learned

- `mkdir` creates directories.
- `touch` can create empty files.
- `cp` copies a file while keeping the original.
- `mv` moves files and can also rename them.
- `rm` removes files.
- `rm -i` asks for confirmation before deleting.
- `*` matches zero or more characters.
- `?` matches exactly one character.
- `[12]` means one character that is either `1` or `2`.
- `[0-9]` means one numeric character.
- `{}` generates multiple text combinations.
- Relative paths depend on my current directory.

---

# Data Engineering Connection

File operations are useful when working with data pipeline directories such as:

```text
incoming/
raw/
processed/
archive/
logs/
```

A data engineer may need to:

- preserve raw datasets
- copy files for processing
- move completed outputs
- rename generated files
- archive old datasets
- clean temporary files
- work with many CSV or log files at once

The goal is not to memorize every command.

The goal is to understand how to manage data files safely and efficiently in a Linux environment.