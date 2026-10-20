# Bash Scripting

Bash scripts allow me to save multiple Linux commands inside a file and execute them together.

Instead of repeatedly typing the same commands manually, I can automate them using a `.sh` file.

This is useful in data engineering for:

- running data-processing commands
- checking files
- moving or archiving data
- automating repeated tasks
- preparing pipeline steps

---

# What Is a Bash Script?

A Bash script is a file containing commands that Bash can execute.

Example file:

```text
hello.sh
```

Example content:

```bash
#!/bin/bash

echo "Hello Esma"
pwd
```

---

# Shebang

The first line of a Bash script can be:

```bash
#!/bin/bash
```

This is called a **shebang**.

It tells the system that the script should be interpreted using Bash.

---

# Making a Script Executable

A new script may not have execute permission.

I can add it with:

```bash
chmod u+x hello.sh
```

Here:

```text
chmod → change permissions
u     → owner/user
+x    → add execute permission
```

Then I can run it with:

```bash
./hello.sh
```

---

# `./`

In:

```bash
./hello.sh
```

the `.` means:

```text
current directory
```

So:

```text
./hello.sh
```

means:

```text
run hello.sh from the current directory
```

---

# Variables

Bash scripts can store values inside variables.

Example:

```bash
name="Esma"
project="data-engineering-journey"
```

To use the value:

```bash
echo "Hello $name"
echo "Project: $project"
```

Important:

```bash
name="Esma"
```

is correct.

This is not:

```bash
name = "Esma"
```

Bash does not use spaces around `=` when assigning a variable.

---

# `$` and Variable Values

The `$` symbol can be used to retrieve values.

Example:

```bash
name="Esma"
echo $name
```

Output:

```text
Esma
```

A useful mental model:

```text
name  → variable name
$name → value stored in the variable
```

---

# Command-Line Arguments

A script can receive values when it is started.

Example:

```bash
./hello.sh Esma data-engineering
```

Inside the script:

```bash
name=$1
project=$2
```

Here:

```text
$1 → first argument
$2 → second argument
```

So:

```text
./hello.sh Esma data-engineering
           ↑     ↑
          $1    $2
```

Arguments allow the same script to work with different input values.

Example:

```bash
./process-data.sh customers.csv
./process-data.sh orders.csv
```

---

# `if` Conditions

Bash can make decisions using `if`.

Example:

```bash
if [ "$name" = "Esma" ]; then
    echo "Hello Esma"
else
    echo "Hello $name"
fi
```

Important keywords:

```text
if   → check condition
then → run if condition is true
else → run otherwise
fi   → end the if block
```

Bash is sensitive to spaces around the condition:

```bash
[ "$name" = "Esma" ]
```

---

# `for` Loops

A loop repeats operations.

Example:

```bash
for name in Esma Ali Ayse
do
    echo "Hello $name"
done
```

Output:

```text
Hello Esma
Hello Ali
Hello Ayse
```

A data engineering example:

```bash
for file in customers.csv orders.csv products.csv
do
    echo "Processing $file"
done
```

This allows multiple files to be processed using the same logic.

---

# Functions

Functions group reusable commands under a name.

Example:

```bash
greet() {
    name=$1
    echo "Hello $name"
}
```

Then:

```bash
greet Esma
greet Ali
```

A function can also receive arguments.

Inside the function:

```bash
$1
```

represents its first argument.

---

# Data Engineering Example

A reusable function could look like:

```bash
process_file() {
    file=$1
    echo "Processing $file"
}
```

Then:

```bash
process_file customers.csv
process_file orders.csv
```

The logic is written once and reused for different files.

---

# Commands and Scripts I Tested

```bash
touch hello.sh

chmod u+x hello.sh

./hello.sh

./hello.sh Esma

./hello.sh Esma data-engineering
```

I also practiced:

```text
variables
arguments
if conditions
for loops
functions
```

---

# What I Learned

- Bash scripts store commands inside `.sh` files.
- scripts help automate repeated work.
- `#!/bin/bash` tells the system to use Bash.
- executable scripts need execute permission when run with `./`.
- variables store values.
- `$variable` retrieves a variable value.
- `$1`, `$2`, etc. represent script arguments.
- `if` allows scripts to make decisions.
- `for` loops repeat operations.
- functions allow reusable logic.
- scripts can accept different files or values without changing the script itself.

---

# Data Engineering Connection

Bash scripts can automate tasks such as:

```text
checking input files
processing multiple files
moving data
creating backups
checking pipeline outputs
starting command-line tools
running repeated pipeline steps
```

The basic idea is:

```text
manual commands
      ↓
Bash script
      ↓
repeatable automation
```