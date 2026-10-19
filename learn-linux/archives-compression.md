# Archives and Compression

Linux provides tools for grouping files into archives and compressing them.

This is useful in data engineering when working with:

- log files
- backups
- exported datasets
- server files
- files that need to be transferred

---

# `tar`

`tar` is commonly used to combine multiple files or directories into a single archive.

Example:

```bash
tar -cvf archive-test.tar archive-test/
```

Here:

```text
c → create
v → verbose
f → file
```

This creates:

```text
archive-test.tar
```

from:

```text
archive-test/
```

---

# Viewing Archive Contents

I can inspect the contents of a `.tar` file without extracting it:

```bash
tar -tvf archive-test.tar
```

Here:

```text
t → list archive contents
v → verbose
f → archive file
```

---

# Extracting a TAR Archive

To extract an archive:

```bash
tar -xvf archive-test.tar
```

Here:

```text
x → extract
```

To extract into a specific directory:

```bash
mkdir extracted
tar -xvf archive-test.tar -C extracted
```

`-C` tells `tar` where to extract the files.

---

# `gzip`

`gzip` compresses data.

Example:

```bash
gzip archive-test.tar
```

This changes:

```text
archive-test.tar
```

into:

```text
archive-test.tar.gz
```

A useful distinction:

```text
.tar → archive
.gz  → gzip compression
```

---

# `gunzip`

`gunzip` removes gzip compression.

Example:

```bash
gunzip archive-test.tar.gz
```

This restores:

```text
archive-test.tar
```

---

# Creating a Compressed Archive Directly

Instead of creating a `.tar` file and compressing it separately, I can do both in one command:

```bash
tar -czvf archive-test.tar.gz archive-test/
```

Here:

```text
c → create
z → use gzip compression
v → verbose
f → file
```

---

# Extracting a `.tar.gz` Archive

A compressed archive can be extracted with:

```bash
tar -xzvf archive-test.tar.gz
```

Here:

```text
x → extract
z → gzip
v → verbose
f → file
```

---

# Checking File Size

I can inspect archive size with:

```bash
ls -lh archive-test.tar.gz
```

`-h` shows file sizes in a human-readable format.

---

# Commands I Tested

```bash
mkdir archive-test

echo "data one" > archive-test/file1.txt
echo "data two" > archive-test/file2.txt

tar -cvf archive-test.tar archive-test/

ls -lh archive-test.tar

tar -tvf archive-test.tar

mkdir extracted

tar -xvf archive-test.tar -C extracted

ls -R extracted

gzip archive-test.tar

ls -lh

gunzip archive-test.tar.gz

tar -czvf archive-test.tar.gz archive-test/

ls -lh archive-test.tar.gz
```

---

# What I Learned

- `tar` groups files and directories into an archive.
- `.tar` represents an archive.
- `gzip` compresses data.
- `.gz` represents gzip compression.
- `.tar.gz` is a tar archive compressed with gzip.
- `tar -cvf` creates an archive.
- `tar -tvf` lists archive contents.
- `tar -xvf` extracts an archive.
- `tar -czvf` creates a gzip-compressed tar archive.
- `tar -xzvf` extracts a gzip-compressed tar archive.
- `gunzip` removes gzip compression.

---

# Data Engineering Connection

A Data Engineer may use archives and compression when:

```text
storing old logs
creating backups
moving datasets
sending files between servers
reducing storage usage
packaging pipeline outputs
```

A common pattern is:

```text
directory
   ↓
tar
   ↓
archive
   ↓
gzip
   ↓
compressed archive
```

Example:

```bash
tar -czvf logs-backup.tar.gz logs/
```