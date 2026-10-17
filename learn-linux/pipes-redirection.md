# Pipes and Redirection

Linux commands communicate using standard input and output streams.

Understanding these streams makes it possible to connect commands, redirect output to files, and separate normal results from errors.

This is useful in data engineering when working with:

- data files
- pipeline logs
- command-line tools
- automation scripts
- server environments

---

# Standard Streams

Linux programs normally have three standard streams:

```text
0 → stdin
1 → stdout
2 → stderr
```

---

## `stdin` — Standard Input

`stdin` is the standard input of a program.

It represents data entering a program.

A simple mental model:

```text
input
  ↓
program
```

For example, a program may receive text typed by the user or data produced by another command.

---

## `stdout` — Standard Output

`stdout` is the normal output produced by a program.

Example:

```bash
echo "Hello Esma"
```

Output:

```text
Hello Esma
```

`Hello Esma` is written to `stdout`.

The standard output number is:

```text
1
```

So these two commands mean the same thing:

```bash
echo "Hello" > output.txt
```

```bash
echo "Hello" 1> output.txt
```

---

## `stderr` — Standard Error

`stderr` is used for error messages.

Example:

```bash
ls olmayan-dosya
```

Output:

```text
ls: cannot access 'olmayan-dosya': No such file or directory
```

This message is produced through `stderr`.

The standard error number is:

```text
2
```

---

# Redirecting Standard Output

The `>` operator redirects standard output to a file.

Example:

```bash
echo "Hello Esma" > output.txt
```

Instead of displaying:

```text
Hello Esma
```

in the terminal, Linux writes it into:

```text
output.txt
```

I can inspect it with:

```bash
cat output.txt
```

---

# `>` — Overwrite

`>` writes output to a file.

If the file already contains data, the old content is replaced.

Example:

```bash
echo "first line" > test.txt
echo "second line" > test.txt
```

After these commands:

```bash
cat test.txt
```

shows:

```text
second line
```

The first line was overwritten.

---

# `>>` — Append

`>>` adds new output to the end of a file without deleting the existing content.

Example:

```bash
echo "second line" > test.txt
echo "third line" >> test.txt
```

Now:

```bash
cat test.txt
```

shows:

```text
second line
third line
```

This is especially useful for log files.

Example:

```bash
echo "pipeline started" >> pipeline.log
echo "1000 rows loaded" >> pipeline.log
```

---

# Redirecting Errors with `2>`

Because `stderr` has the number `2`, errors can be redirected using:

```text
2>
```

Example:

```bash
ls olmayan-dosya 2> error.txt
```

The error does not appear normally in the terminal.

Instead, it is written to:

```text
error.txt
```

I can inspect it with:

```bash
cat error.txt
```

---

# File Descriptor Numbers

The three standard streams have numbers:

```text
0 → stdin
1 → stdout
2 → stderr
```

This is why:

```bash
command > output.txt
```

means redirect `stdout`.

And:

```bash
command 2> error.txt
```

means redirect `stderr`.

---

# Pipe `|`

A pipe connects commands.

It sends the `stdout` of one command to the `stdin` of another command.

Mental model:

```text
Command A
   ↓
 stdout
   ↓
   |
   ↓
 stdin
   ↓
Command B
```

Example:

```bash
cat test.txt | wc -l
```

Here:

```text
cat
 ↓
file content
 ↓
|
 ↓
wc -l
 ↓
number of lines
```

---

# Filtering Data with Pipes

Example:

```bash
cat test.txt | grep "third"
```

`cat` produces the file content.

`grep` receives that content and keeps only the lines containing:

```text
third
```

---

# Combining Commands

Commands can be connected to create small processing pipelines.

Example:

```bash
sort names.txt | uniq
```

Here:

```text
sort
 ↓
sorted lines
 ↓
|
 ↓
uniq
 ↓
duplicate adjacent lines removed
```

Another example:

```bash
grep "ERROR" pipeline.log | wc -l
```

This answers:

> How many error lines are inside the pipeline log?

The data flow is:

```text
pipeline.log
     ↓
grep "ERROR"
     ↓
matching lines
     ↓
|
     ↓
wc -l
     ↓
number of errors
```

---

# Pipe and Redirection Together

A pipeline result can also be saved to a file.

Example:

```bash
grep "ERROR" pipeline.log | wc -l > error-count.txt
```

Data flow:

```text
pipeline.log
     ↓
grep "ERROR"
     ↓
matching lines
     ↓
|
     ↓
wc -l
     ↓
number
     ↓
>
     ↓
error-count.txt
```

The result can be inspected with:

```bash
cat error-count.txt
```

---

# Saving Filtered Results

I can save only matching lines into another file.

Example:

```bash
grep "ERROR" pipeline.log > errors-only.log
```

Then:

```bash
cat errors-only.log
```

shows only the error lines.

---

# Data Engineering Example

Suppose a pipeline creates this log:

```text
INFO pipeline started
INFO reading customers.csv
ERROR database connection failed
INFO retrying connection
ERROR connection timeout
```

I can find the errors:

```bash
grep "ERROR" pipeline.log
```

Count them:

```bash
grep "ERROR" pipeline.log | wc -l
```

Save the count:

```bash
grep "ERROR" pipeline.log | wc -l > error-count.txt
```

Save only the error messages:

```bash
grep "ERROR" pipeline.log > errors-only.log
```

This is a small example of processing data using Linux commands.

---

# Commands I Tested

```bash
echo "Hello Esma"

ls olmayan-dosya

echo "Hello Esma" > output.txt
cat output.txt

ls olmayan-dosya 2> error.txt
cat error.txt

echo "normal output" 1> normal.txt

echo "first line" > test.txt
echo "second line" > test.txt
echo "third line" >> test.txt
cat test.txt

cat test.txt | wc -l
cat test.txt | grep "third"

grep "ERROR" pipeline.log
grep "ERROR" pipeline.log | wc -l

grep "ERROR" pipeline.log | wc -l > error-count.txt
grep "ERROR" pipeline.log > errors-only.log
```

---

# What I Learned

- `stdin` is standard input.
- `stdout` is normal program output.
- `stderr` is error output.
- `0` represents `stdin`.
- `1` represents `stdout`.
- `2` represents `stderr`.
- `>` redirects output and overwrites a file.
- `>>` appends output to a file.
- `2>` redirects error output.
- `|` sends one command's `stdout` to another command's `stdin`.
- Linux commands can be connected to create small data-processing pipelines.

---

# Data Engineering Connection

These concepts are useful when working with data pipelines and servers.

A Data Engineer may need to:

```text
inspect pipeline output
filter logs
count errors
save command results
separate normal output from errors
connect multiple command-line tools
```

A useful mental model is:

```text
input
  ↓
command
  ↓
output
  ↓
next command
  ↓
result
```

This is very similar to the basic idea of a data pipeline:

```text
source → process → filter → output
```