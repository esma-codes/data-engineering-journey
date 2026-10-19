# Environment Variables and PATH

Environment variables are named values that programs and the shell can use.

They are useful for storing configuration information such as:

- user information
- home directory
- paths
- application settings
- database connection information
- API keys
- tool configuration

In data engineering, environment variables are commonly used by tools such as Python, PostgreSQL, Docker, Airflow, and cloud services.

---

# Viewing Environment Variables

Some common environment variables are:

```text
HOME
USER
SHELL
PATH
```

To print the value of a variable, I use `$`.

Example:

```bash
echo $HOME
```

Example output:

```text
/home/esma_nur
```

Other examples:

```bash
echo $USER
echo $SHELL
```

A useful mental model:

```text
HOME  → variable name
$HOME → value stored inside the variable
```

---

# Creating an Environment Variable

I can create an environment variable using `export`.

Example:

```bash
export PROJECT_NAME="data-engineering-journey"
```

Then:

```bash
echo $PROJECT_NAME
```

Output:

```text
data-engineering-journey
```

`export` makes the variable available in the current shell environment and to programs started from that shell.

---

# Temporary Environment Variables

A variable created with:

```bash
export PROJECT_NAME="data-engineering-journey"
```

is usually temporary.

It exists in the current shell session.

When the shell is closed, the variable may disappear unless it is saved in a shell configuration file.

---

# Why Environment Variables Matter

Programs often need configuration values.

Instead of writing configuration directly inside source code, values can be provided through environment variables.

Examples:

```text
DATABASE_URL
API_KEY
AIRFLOW_HOME
JAVA_HOME
PATH
```

Sensitive values such as passwords or API keys should not be committed directly into GitHub repositories.

Environment variables are one part of safer configuration management.

---

# `PATH`

`PATH` is a special environment variable.

It contains a list of directories where the shell searches for executable commands.

To view it:

```bash
echo $PATH
```

Example:

```text
/usr/local/bin:/usr/bin:/bin
```

The directories are separated by:

```text
:
```

---

# How PATH Works

When I type:

```bash
git
```

Bash does not search the entire filesystem.

Instead, it checks the directories listed inside `PATH`.

A simple mental model:

```text
command entered
      ↓
Bash checks PATH directories
      ↓
executable is found
      ↓
program runs
```

For example:

```bash
which git
```

may return:

```text
/usr/bin/git
```

This means the executable file for `git` is located at:

```text
/usr/bin/git
```

But because `/usr/bin` is inside `PATH`, I only need to type:

```bash
git
```

---

# `which`

`which` shows where a command is found.

Examples:

```bash
which python3
which git
which ls
```

Possible output:

```text
/usr/bin/python3
/usr/bin/git
/usr/bin/ls
```

---

# What Does `bin` Mean?

`bin` historically comes from:

```text
binary
```

Directories such as:

```text
/bin
/usr/bin
/usr/local/bin
```

commonly contain executable programs and commands.

For example:

```text
/usr/bin/git
/usr/bin/python3
/usr/bin/ls
```

---

# Filesystem Path vs PATH Variable

These are different concepts.

A filesystem path describes where a file or directory is located.

Example:

```text
/home/esma_nur/data-engineering-journey
```

The `PATH` environment variable is a list of directories where Bash searches for executable commands.

So:

```text
filesystem path → location of a file or directory
PATH variable   → directories used to search for commands
```

---

# Creating My Own Command Directory

I created a directory for custom commands:

```bash
mkdir -p ~/my-bin
```

Then I created a small executable file:

```bash
echo 'echo "My custom command works!"' > ~/my-bin/hello-esma
```

I added execute permission:

```bash
chmod +x ~/my-bin/hello-esma
```

Before adding the directory to `PATH`, running:

```bash
hello-esma
```

may return:

```text
command not found
```

The file exists, but Bash does not know where to search for it.

---

# Adding a Directory to PATH

I added my custom directory to `PATH`:

```bash
export PATH="$HOME/my-bin:$PATH"
```

This means:

```text
$HOME/my-bin
```

is added to the beginning of the existing `PATH`.

After this:

```bash
hello-esma
```

can work because Bash now searches inside:

```text
/home/esma_nur/my-bin
```

---

# Why `$PATH` Is Included

This command:

```bash
export PATH="$HOME/my-bin:$PATH"
```

contains the old value of `PATH` at the end.

This keeps the existing command directories.

Without `$PATH`, I could accidentally replace the entire existing PATH value.

---

# `.bashrc`

Bash can load user configuration from:

```text
~/.bashrc
```

For my user:

```text
~/.bashrc
```

means:

```text
/home/esma_nur/.bashrc
```

To open it in VS Code:

```bash
code ~/.bashrc
```

A PATH setting can be added to this file:

```bash
export PATH="$HOME/my-bin:$PATH"
```

This allows the setting to be loaded again in future Bash sessions.

---

# `source`

After changing `.bashrc`, I can reload it without closing the terminal:

```bash
source ~/.bashrc
```

This tells Bash to read the file again.

---

# Commands I Tested

```bash
echo $HOME
echo $USER
echo $SHELL

export PROJECT_NAME="data-engineering-journey"
echo $PROJECT_NAME

echo $PATH

which python3
which git
which ls

mkdir -p ~/my-bin

echo 'echo "My custom command works!"' > ~/my-bin/hello-esma

chmod +x ~/my-bin/hello-esma

hello-esma

export PATH="$HOME/my-bin:$PATH"

hello-esma

code ~/.bashrc

source ~/.bashrc
```

---

# What I Learned

- environment variables store named configuration values
- `$VARIABLE` reads the value of a variable
- `export` creates or exposes an environment variable
- environment variables created in a shell may be temporary
- `PATH` tells Bash where to search for executable commands
- `which` shows where a command is located
- `/bin` and `/usr/bin` commonly contain executable programs
- a normal filesystem path is not the same thing as the `PATH` variable
- custom executable directories can be added to `PATH`
- `.bashrc` can store Bash configuration
- `source ~/.bashrc` reloads the configuration

---

# Data Engineering Connection

Environment variables are common in data engineering tools and pipelines.

They may store values such as:

```text
database connection strings
API configuration
application settings
tool locations
cloud configuration
pipeline configuration
```

`PATH` is also important because command-line tools must be discoverable by the shell.

A Data Engineer may encounter problems such as:

```text
command not found
missing environment variable
incorrect PATH
wrong configuration value
```

Understanding environment variables and `PATH` makes these problems easier to debug.