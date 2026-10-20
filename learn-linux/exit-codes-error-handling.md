# Exit Codes and Error Handling

Linux commands return an exit code when they finish.

Exit codes allow scripts and other commands to understand whether an operation succeeded or failed.

This is important in data engineering because pipeline steps should not continue blindly after an error.

---

# Exit Codes

The basic convention is:

```text
0     → success
non-0 → error / failure
```

---

# `$?`

Bash stores the exit code of the most recently executed command in:

```bash
$?
```

Example:

```bash
ls
echo $?
```

If `ls` succeeds, the result is usually:

```text
0
```

Example with an error:

```bash
ls olmayan-dosya
echo $?
```

This returns a non-zero exit code.

---

# Meaning of `$`

I have seen `$` used in several ways.

Examples:

```text
$name → value of a variable
$1    → first script argument
$2    → second script argument
$?    → exit code of the previous command
```

---

# `&&`

`&&` runs the next command only if the previous command succeeds.

Example:

```bash
mkdir test-folder && echo "Folder created"
```

Mental model:

```text
command succeeds
       ↓
      &&
       ↓
run next command
```

---

# `||`

`||` runs the next command if the previous command fails.

Example:

```bash
ls olmayan-dosya || echo "File not found"
```

Mental model:

```text
command fails
      ↓
     ||
      ↓
run error action
```

---

# `&&` vs `||`

```text
&& → continue when successful
|| → react when unsuccessful
```

These operators can create simple command-line error handling.

---

# Checking Whether a File Exists

I created a script called:

```text
check-file.sh
```

Example:

```bash
#!/bin/bash

file=$1

if [ -f "$file" ]; then
    echo "File exists: $file"
    exit 0
else
    echo "ERROR: File not found: $file"
    exit 1
fi
```

---

# `-f`

Inside:

```bash
[ -f "$file" ]
```

`-f` checks whether the given path exists and is a regular file.

---

# `exit`

A Bash script can explicitly return an exit code.

Example:

```bash
exit 0
```

means:

```text
successful completion
```

Example:

```bash
exit 1
```

means:

```text
failure
```

---

# Testing the Script

With an existing file:

```bash
./check-file.sh networking.md
```

Then:

```bash
echo $?
```

should return:

```text
0
```

With a missing file:

```bash
./check-file.sh olmayan.csv
```

Then:

```bash
echo $?
```

should return a failure code such as:

```text
1
```

---

# Permission Error

When I first tried:

```bash
./check-file.sh networking.md
```

I received:

```text
Permission denied
```

because the script did not have execute permission.

I fixed it with:

```bash
chmod u+x check-file.sh
```

Then the script could be executed using:

```bash
./check-file.sh networking.md
```

---

# Running Through Bash

A script can also be passed directly to Bash:

```bash
bash check-file.sh networking.md
```

In this case, Bash reads the script itself.

This is different from executing the file directly with:

```bash
./check-file.sh networking.md
```

which requires execute permission.

---

# Basic Logging

Errors or pipeline information can be written to a log file.

Example:

```bash
echo "ERROR: File not found: $file" >> pipeline.log
```

Here:

```text
>> → append output to the end of the file
```

This allows previous log information to remain instead of being overwritten.

---

# Data Engineering Example

Suppose a pipeline requires:

```text
customers.csv
```

Before processing it, the pipeline can check:

```text
Does the file exist?
```

If yes:

```text
exit 0
→ continue pipeline
```

If no:

```text
write error
exit 1
→ stop or report failure
```

This prevents later pipeline steps from running with missing input data.

---

# Commands I Tested

```bash
ls
echo $?

ls olmayan-dosya
echo $?

mkdir test-folder && echo "Folder created"

ls olmayan-dosya || echo "File not found"

chmod u+x check-file.sh

./check-file.sh networking.md
echo $?

./check-file.sh olmayan.csv
echo $?
```

---

# What I Learned

- commands return exit codes.
- `0` normally means success.
- non-zero values normally mean failure.
- `$?` shows the previous command's exit code.
- `&&` continues when the previous command succeeds.
- `||` reacts when the previous command fails.
- `-f` can check whether a regular file exists.
- `exit 0` represents successful script completion.
- `exit 1` can represent failure.
- scripts can validate input before continuing.
- errors can be appended to log files with `>>`.

---

# Data Engineering Connection

Reliable pipelines need to detect failures.

Exit codes and error handling help answer questions such as:

```text
Did this step succeed?
Does the required input exist?
Should the next step run?
Should the pipeline stop?
Should an error be written to a log?
```

A useful mental model is:

```text
run step
   ↓
check result
   ↓
success → continue
failure → log / stop / handle error
```