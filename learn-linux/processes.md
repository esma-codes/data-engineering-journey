# Linux Processes

A process is a program that is currently running.

A useful distinction is:

```text
Program → code stored on disk
Process → a running instance of that program
```

Linux assigns every process a unique number called a **PID**.

```text
PID = Process ID
```

---

# `ps`

`ps` shows processes associated with the current terminal session.

Example:

```bash
ps
```

Example output:

```text
PID TTY      TIME CMD
361 pts/0    00:00 bash
853 pts/0    00:00 ps
```

Important columns:

```text
PID → process ID
CMD → command/program
```

The `ps` command itself is also temporarily a process while it is running.

---

# `ps aux`

`ps aux` shows a broader list of processes running on the system.

```bash
ps aux
```

Important columns include:

```text
USER    → user running the process
PID     → process ID
%CPU    → CPU usage
%MEM    → memory usage
COMMAND → program or command
```

I do not need to memorize every column immediately.

---

# Filtering Processes

I can combine process commands with tools such as `grep`.

Example:

```bash
ps aux | grep bash
```

This filters the process list and shows lines containing `bash`.

The `grep` command itself may also appear because its own command contains the word `bash`.

---

# `top`

`top` displays processes and system resource usage continuously.

```bash
top
```

Unlike `ps`, which gives a snapshot, `top` updates in real time.

Useful information includes:

```text
CPU usage
memory usage
running processes
process IDs
```

To exit:

```text
q
```

A simple mental model:

```text
ps  → snapshot
top → live view
```

---

# Foreground Processes

A foreground process uses the current terminal until it finishes.

Example:

```bash
sleep 30
```

While it is running, the shell prompt does not immediately return.

---

# Background Processes

Adding `&` starts a command in the background.

Example:

```bash
sleep 60 &
```

The terminal becomes available again while the process continues running.

Example output:

```text
[1] 1042
```

Here:

```text
[1]  → shell job number
1042 → PID
```

---

# `jobs`

`jobs` shows background or stopped jobs in the current shell.

```bash
jobs
```

Example:

```text
[1]+ Running sleep 60 &
```

A job number and a PID are different:

```text
Job number → managed by the current shell
PID        → process ID used by Linux
```

---

# `fg`

`fg` brings a background job back to the foreground.

```bash
fg
```

---

# `Ctrl + C`

`Ctrl + C` stops the foreground process.

Example:

```bash
sleep 120
```

Then:

```text
Ctrl + C
```

terminates it.

---

# `Ctrl + Z`

`Ctrl + Z` pauses a foreground process without terminating it.

Example:

```bash
sleep 120
```

Then:

```text
Ctrl + Z
```

may show:

```text
[1]+ Stopped sleep 120
```

The process still exists but is paused.

---

# `bg`

`bg` continues a stopped job in the background.

```bash
bg
```

The process continues running without occupying the terminal.

---

# `kill`

`kill` sends a termination signal to a process using its PID.

Example:

```bash
kill 1234
```

This asks the process with PID `1234` to terminate.

A stronger form is:

```bash
kill -9 1234
```

This forcibly terminates the process and should normally be used only when a regular `kill` does not work.

---

# Commands I Tested

```bash
ps
ps aux
ps aux | grep bash

top

sleep 30

sleep 60 &
jobs

fg

sleep 120
# Ctrl + Z

jobs
bg
jobs
```

---

# What I Learned

- A process is a running program.
- Every process has a PID.
- `ps` shows a process snapshot.
- `ps aux` shows a broader process list.
- `top` shows live process and system resource information.
- `&` starts a process in the background.
- `jobs` shows jobs managed by the current shell.
- `fg` moves a job to the foreground.
- `Ctrl + C` terminates a foreground process.
- `Ctrl + Z` pauses a foreground process.
- `bg` continues a stopped process in the background.
- `kill` terminates a process using its PID.

---

# Data Engineering Connection

Data pipelines and data infrastructure run as processes.

Examples include:

```text
Python pipelines
database services
Docker containers
Airflow tasks
Spark jobs
background scripts
```

When something is slow, stuck, or unexpectedly running, process tools help answer questions such as:

```text
Is the process running?
What is its PID?
Who started it?
How much CPU or memory is it using?
Should I stop it?
```

Understanding processes is useful when debugging pipelines and working on Linux servers.