# 🧪 Linux Final Lab — File-Based Data Pipeline

This mini project is the final hands-on exercise of my Linux fundamentals journey for Data Engineering.

The goal was to combine the Linux concepts I learned into one small, repeatable data-processing workflow.

---

## 🎯 Project Goal

The pipeline simulates a very simple Data Engineering flow:

```text
incoming data
     ↓
raw copy
     ↓
processing
     ↓
processed output
     ↓
archive
     ↓
logs
```

Instead of running every command manually, I created a Bash script that performs the workflow automatically.

---

# 📥 Input Data

The pipeline starts with:

```text
incoming/customers.csv
```

Example input:

```csv
id,name,status
1,Esma,active
2,Ayse,inactive
3,Ali,active
4,Mehmet,active
5,Zeynep,inactive
6,Ece,active
7,Can,inactive
8,Deniz,active
9,Selin,active
10,Kerem,inactive
```

The goal is to keep only customers whose status is:

```text
active
```

---

# ⚙️ Pipeline Flow

The pipeline follows these steps:

```text
incoming/customers.csv
          ↓
check if file exists
          ↓
copy to raw/
          ↓
filter active customers
          ↓
write processed output
          ↓
count active records
          ↓
write logs
          ↓
move original input to archive/
```

---

# 📂 Project Structure

```text
linux-final-lab/
├── incoming/
├── raw/
│   └── customers.csv
├── processed/
│   └── active-customers.csv
├── archive/
│   └── customers.csv
├── logs/
│   └── pipeline.log
├── pipeline.sh
└── README.md
```

After a successful pipeline run, the `incoming/` directory becomes empty because the processed input file is moved into `archive/`.

---

# 🖥️ Main Script

The main pipeline is:

```text
pipeline.sh
```

It uses Bash and Linux commands to automate the workflow.

---

# 🔎 Input Validation

Before processing, the script checks whether the expected input file exists.

```bash
if [ ! -f "$input" ]; then
    echo "ERROR: customers.csv not found" >> "$log"
    exit 1
fi
```

Here:

```text
-f → check whether a regular file exists
!  → NOT
```

If the input file does not exist:

```text
error is logged
     ↓
exit 1
     ↓
pipeline stops
```

---

# 📦 Raw Layer

The original input is copied into:

```text
raw/customers.csv
```

using:

```bash
cp "$input" "$raw"
```

This keeps a raw copy before processing.

---

# 🔄 Processing

The CSV header is copied first:

```bash
head -n 1 "$raw" > "$output"
```

Then only active customers are selected:

```bash
grep ",active" "$raw" >> "$output"
```

The processed file becomes:

```text
processed/active-customers.csv
```

---

# ✅ Processed Output

The result contains:

```csv
id,name,status
1,Esma,active
3,Ali,active
4,Mehmet,active
6,Ece,active
8,Deniz,active
9,Selin,active
```

Total active customers:

```text
6
```

---

# 🔢 Counting Records

The pipeline counts active rows using:

```bash
count=$(grep -c ",active" "$raw")
```

Here:

```text
$(command)
```

runs a command and stores its output.

The result is assigned to:

```text
count
```

---

# 📝 Logging

Pipeline events are written into:

```text
logs/pipeline.log
```

Example:

```text
Pipeline started
Processed active customers: 6
Pipeline completed successfully
```

If the input file is missing:

```text
ERROR: customers.csv not found
```

is added to the log.

---

# 📦 Archive Step

After successful processing, the incoming file is moved into:

```text
archive/customers.csv
```

using:

```bash
mv "$input" archive/customers.csv
```

This means the pipeline does not process the same incoming file repeatedly.

---

# 🚦 Exit Codes

The script uses exit codes to communicate success or failure.

```text
exit 0 → success
exit 1 → failure
```

This allows another script or system to understand whether the pipeline finished correctly.

---

# 🛠️ Linux Concepts Used

This lab combines several concepts from my Linux learning journey:

```text
filesystem paths
mkdir
cp
mv
head
grep
redirection
variables
if conditions
file validation
Bash scripting
logging
exit codes
permissions
```

---

# 🧠 Debugging Experience

During testing, I ran the pipeline a second time after the input file had already been moved into `archive/`.

The second run returned:

```text
ERROR: customers.csv not found
```

I debugged the problem by checking:

```bash
ls incoming
ls archive
ls raw
ls processed
cat logs/pipeline.log
```

This showed that the first pipeline run had completed successfully and moved the input file into the archive.

This helped me practice an important Data Engineering habit:

```text
check input
    ↓
check outputs
    ↓
check archive
    ↓
check logs
    ↓
find the cause
```

---

# 🌱 What I Learned

This project helped me understand how individual Linux commands can work together as a small pipeline.

Before this lab, I mostly used commands one by one.

Now I can see how they connect:

```text
input
  ↓
validation
  ↓
raw data
  ↓
processing
  ↓
output
  ↓
logging
  ↓
archive
```

This is a simplified version of patterns that I will see again in larger Data Engineering systems.

---

## 👩‍💻 Built by Esma

Part of my:

```text
data-engineering-journey
```

Learning Linux by using it inside real Data Engineering-style workflows.