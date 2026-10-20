# 🐧 Esma's Linux Journey for Data Engineering

> My hands-on Linux learning journey as part of my path toward becoming a Data Engineer.

This directory documents the Linux fundamentals I learned by **understanding, testing, breaking, debugging, and building** instead of only memorizing commands.

I am not learning Linux to become a Linux system administrator.

My goal is to become comfortable enough with Linux to work with:

- data pipelines
- servers
- databases
- logs
- APIs
- Docker
- cloud systems
- automation
- data engineering tools

---

## 👩‍💻 About This Journey

**Created and maintained by Esma**

This is part of my personal:

```text
Data Engineering Journey
```

I started this section with very little practical Linux experience.

Instead of trying to memorize dozens of commands, I followed this approach:

```text
Understand
    ↓
Test in terminal
    ↓
Make mistakes
    ↓
Debug
    ↓
Take notes
    ↓
Use it in a small project
```

The goal was not:

```text
"How many Linux commands can I memorize?"
```

The goal was:

```text
"Can I understand what is happening
when I work inside a Linux environment?"
```

---

# 🗺️ Linux Learning Roadmap

## ✅ 1. Linux Environment

I learned the relationship between:

```text
Linux
Ubuntu
WSL
Terminal
Shell
Bash
```

I also learned the difference between a terminal and a shell.

📄 Notes:

`linux-environment.md`

---

## ✅ 2. Filesystem & Navigation

I learned how the Linux filesystem is organized.

Important concepts:

```text
/    → root directory
~    → my home directory
.    → current directory
..   → parent directory
```

I practiced:

```bash
pwd
ls
ls -a
ls -l
ls -la
cd
```

I also learned the difference between:

```text
absolute path
relative path
```

📄 Notes:

`filesystem-navigation.md`

---

## ✅ 3. File Operations

I practiced creating, copying, moving, renaming, and deleting files and directories.

Commands:

```bash
mkdir
touch
cp
mv
rm
```

I also learned:

```text
*
?
[]
{}
```

for wildcard matching and brace expansion.

📄 Notes:

`file-operations.md`

---

## ✅ 4. Inspecting & Processing Data

I learned how to inspect files directly from the terminal without opening them in an editor.

Commands:

```bash
cat
head
tail
less
wc
grep
sort
uniq
```

Examples:

```bash
head customers.csv
wc -l customers.csv
grep "ERROR" pipeline.log
sort names.txt | uniq
```

This was one of the first places where Linux started to feel directly connected to Data Engineering.

📄 Notes:

`inspecting-data.md`

---

## ✅ 5. Pipes, Streams & Redirection

I learned the three standard streams:

```text
0 → stdin
1 → stdout
2 → stderr
```

I practiced:

```text
>
>>
2>
|
```

Example:

```bash
grep "ERROR" pipeline.log | wc -l > error-count.txt
```

This helped me understand how Linux commands can be connected like a small data pipeline.

```text
command
   ↓
stdout
   ↓
pipe
   ↓
stdin
   ↓
next command
```

📄 Notes:

`pipes-redirection.md`

---

## ✅ 6. Users & Permissions

I learned how Linux decides:

```text
who can read?
who can write?
who can execute?
```

Permissions:

```text
r → read
w → write
x → execute
```

Categories:

```text
u → user / owner
g → group
o → others
```

Commands:

```bash
whoami
id
chmod
```

I also learned about numeric permissions such as:

```text
644
755
```

and understood why blindly using permissions such as `777` is not a good practice.

📄 Notes:

`permissions-users.md`

---

## ✅ 7. Processes

I learned that:

```text
Program → code stored on disk
Process → running instance of a program
```

Important concepts:

```text
PID
foreground
background
jobs
```

Commands and controls:

```bash
ps
ps aux
top
jobs
fg
bg
kill
```

Keyboard controls:

```text
Ctrl + C → terminate
Ctrl + Z → pause
```

I also practiced running commands in the background:

```bash
sleep 60 &
```

📄 Notes:

`processes.md`

---

## ✅ 8. Environment Variables & PATH

I learned how programs receive configuration through environment variables.

Examples:

```text
HOME
USER
SHELL
PATH
```

I practiced:

```bash
echo $HOME
echo $USER
echo $PATH
export
which
source ~/.bashrc
```

I also created my own command directory and added it to `PATH`.

```text
PATH
 ↓
directories where Bash searches
for executable commands
```

📄 Notes:

`environment-variables-path.md`

---

## ✅ 9. Basic Networking

I learned the fundamentals of how machines and services communicate.

Concepts:

```text
IP address
hostname
port
DNS
HTTP
SSH
```

Important example ports:

```text
22   → SSH
80   → HTTP
443  → HTTPS
5432 → PostgreSQL
```

Commands:

```bash
hostname
hostname -I
ss -tuln
getent hosts
curl
ssh
```

I also sent a real request to the GitHub API:

```bash
curl https://api.github.com
```

and learned basic HTTP status codes.

📄 Notes:

`networking.md`

---

## ✅ 10. Archives & Compression

I learned the difference between:

```text
archive
compression
```

and practiced:

```bash
tar
gzip
gunzip
```

Examples:

```bash
tar -czvf backup.tar.gz folder/
tar -xzvf backup.tar.gz
```

📄 Notes:

`archives-compression.md`

---

## ✅ 11. Linux Links

I learned the difference between:

```text
symbolic link
hard link
```

Symbolic link:

```text
shortcut → target path
```

Hard link:

```text
two names → same underlying file
```

I also learned about:

```text
inode
broken symlink
```

Example:

```bash
ln -s original.txt shortcut.txt
```

📄 Notes:

`links.md`

---

## ✅ 12. Bash Scripting

I moved from manually typing commands to creating reusable `.sh` scripts.

I learned:

```text
shebang
variables
arguments
if conditions
for loops
functions
```

Example:

```bash
#!/bin/bash

name=$1

if [ "$name" = "Esma" ]; then
    echo "Hello Esma"
else
    echo "Hello $name"
fi
```

I learned that scripts help turn:

```text
manual commands
       ↓
repeatable automation
```

📄 Notes:

`bash-scripting.md`

---

## ✅ 13. Exit Codes & Error Handling

I learned that Linux commands report whether they succeeded or failed.

```text
0     → success
non-0 → failure
```

I practiced:

```bash
echo $?
```

and:

```text
&& → continue if successful
|| → react if unsuccessful
```

I also created a script that checks whether an input file exists before continuing.

```bash
if [ ! -f "$file" ]; then
    exit 1
fi
```

📄 Notes:

`exit-codes-error-handling.md`

---

## ✅ 14. Cron Automation

I learned how Linux can automatically run commands at scheduled times.

The key idea:

```text
Bash script → WHAT should happen?
cron        → WHEN should it happen?
```

I created a real cron job that automatically wrote the current time to a log file every minute.

Example:

```text
* * * * * command
```

Cron format:

```text
minute
hour
day of month
month
day of week
```

📄 Notes:

`cron-automation.md`

---

# 🧪 Final Linux Lab

After learning the individual concepts, I combined them into a small file-based Data Engineering pipeline.

Project:

```text
linux-final-lab/
```

The pipeline simulates this flow:

```text
              ┌─────────────┐
              │  incoming/  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │    raw/     │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │ processing  │
              │ grep / head │
              └──────┬──────┘
                     │
            ┌────────┴────────┐
            ▼                 ▼
     ┌─────────────┐    ┌─────────────┐
     │ processed/  │    │    logs/    │
     └─────────────┘    └─────────────┘
            │
            ▼
     ┌─────────────┐
     │  archive/   │
     └─────────────┘
```

The pipeline:

```text
checks the input file
        ↓
copies raw data
        ↓
filters active customers
        ↓
creates processed output
        ↓
counts records
        ↓
writes logs
        ↓
archives the input
        ↓
returns an exit code
```

This was my first small Linux-based Data Engineering workflow.

---

# 📂 Repository Structure

```text
learn-linux/
├── README.md
├── linux-environment.md
├── filesystem-navigation.md
├── file-operations.md
├── inspecting-data.md
├── pipes-redirection.md
├── permissions-users.md
├── processes.md
├── environment-variables-path.md
├── networking.md
├── archives-compression.md
├── links.md
├── bash-scripting.md
├── exit-codes-error-handling.md
├── cron-automation.md
│
└── file-based-data-pipeline/
    ├── pipeline.sh
    ├── raw/
    │   └── customers.csv
    ├── processed/
    │   └── active-customers.csv
    ├── archive/
    │   └── customers.csv
    └── logs/
        └── pipeline.log
```

---

# 🔗 How the Topics Connect

The topics were not isolated.

They started connecting together:

```text
Filesystem
    ↓
File Operations
    ↓
Inspecting Data
    ↓
Pipes & Redirection
    ↓
Permissions
    ↓
Processes
    ↓
Environment Variables
    ↓
Networking
    ↓
Bash Scripting
    ↓
Error Handling
    ↓
Automation
    ↓
Data Pipeline
```

That connection is more important to me than memorizing individual commands.

---

# 🧠 What I Can Do Now

After completing this section, I can:

```text
navigate inside a Linux filesystem
understand absolute and relative paths
manage files and directories
inspect CSV and log files
search and filter text
connect Linux commands with pipes
redirect outputs and errors
understand basic permissions
inspect running processes
work with environment variables
understand PATH
understand basic networking concepts
send HTTP requests using curl
understand SSH basics
create and extract archives
work with symbolic and hard links
write small Bash scripts
use arguments, conditions, loops, and functions
understand exit codes
perform basic error handling
write simple logs
schedule commands using cron
combine Linux tools into a small data pipeline
```

---

# 💡 Most Important Lesson

The most important thing I learned was not a specific command.

It was understanding that Linux tools can be combined.

```text
small command
     +
small command
     +
small command
     ↓
useful workflow
```

This is very similar to Data Engineering itself:

```text
source
   ↓
ingestion
   ↓
processing
   ↓
validation
   ↓
output
   ↓
monitoring
```

---

# 🚀 Next Step

Linux is not the final destination.

It is one of the foundations of my Data Engineering journey.

The next stages will build on this foundation with tools such as:

```text
Python
SQL
PostgreSQL
Docker
data pipelines
orchestration
distributed processing
cloud
```

I will continue using Linux throughout the journey instead of treating it as a topic that I learned once and never use again.

---

## 🐧 Linux Fundamentals — Completed

```text
[✓] Linux environment
[✓] Filesystem & navigation
[✓] File operations
[✓] Data inspection
[✓] Pipes & redirection
[✓] Users & permissions
[✓] Processes
[✓] Environment variables & PATH
[✓] Basic networking
[✓] Archives & compression
[✓] Links
[✓] Bash scripting
[✓] Exit codes & error handling
[✓] Cron automation
[✓] Final Linux data pipeline lab
```

---

### Built by Esma 🌱

```text
Learning Data Engineering
one concept,
one terminal command,
and one project at a time.
```