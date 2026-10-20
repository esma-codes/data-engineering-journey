# Cron Automation

`cron` is a Linux scheduling system.

It can automatically run commands or scripts at specific times.

A useful distinction is:

```text
Bash script → what should happen?
cron        → when should it happen?
```

Cron is useful for repeated automated tasks.

Examples:

```text
run a backup every night
run a pipeline every hour
check logs every few minutes
start a script every morning
```

---

# `crontab`

Cron jobs for a user are managed using:

```bash
crontab
```

To list existing cron jobs:

```bash
crontab -l
```

Here:

```text
-l → list
```

If no jobs exist, Linux may display:

```text
no crontab for esma_nur
```

---

# Editing Cron Jobs

To edit cron jobs:

```bash
crontab -e
```

Here:

```text
-e → edit
```

The first time I used this command, I selected:

```text
nano
```

as the editor.

---

# Cron Schedule Format

A cron entry normally looks like:

```text
* * * * * command
```

The five scheduling fields mean:

```text
* * * * *
│ │ │ │ │
│ │ │ │ └── day of week
│ │ │ └──── month
│ │ └────── day of month
│ └──────── hour
└────────── minute
```

So the order is:

```text
minute
hour
day of month
month
day of week
```

---

# Meaning of `*`

The `*` symbol means:

```text
any value
```

So:

```text
* * * * *
```

means:

```text
every minute
```

because every scheduling field accepts any value.

---

# Example: Every Day at 02:00

```text
0 2 * * * command
```

means:

```text
minute → 0
hour   → 2
```

So the command runs every day at:

```text
02:00
```

---

# Example: Every Monday at 09:00

```text
0 9 * * 1 command
```

This means:

```text
09:00 every Monday
```

---

# Example: Every 15 Minutes

```text
*/15 * * * * command
```

means:

```text
run every 15 minutes
```

---

# Cron Test

I created a real cron job:

```text
* * * * * date >> /home/esma_nur/data-engineering-journey/learn-linux/cron-test.log
```

This means:

```text
every minute
    ↓
run date
    ↓
append the result
    ↓
cron-test.log
```

---

# `date`

The command:

```bash
date
```

prints the current date and time.

Cron automatically ran this command every minute.

---

# Using `>>`

The cron job used:

```text
>>
```

to append output to the log file.

This means existing log data was preserved and new lines were added to the end.

---

# Absolute Paths in Cron

I used:

```text
/home/esma_nur/data-engineering-journey/learn-linux/cron-test.log
```

instead of depending on the current terminal directory.

Cron jobs do not necessarily run from the directory where I normally work.

Using absolute paths helps avoid path-related problems.

---

# Verifying the Cron Job

I checked the generated file using:

```bash
cat ~/data-engineering-journey/learn-linux/cron-test.log
```

Example output:

```text
Tue Oct 20 17:02:01 +03 2026
Tue Oct 20 17:03:01 +03 2026
Tue Oct 20 17:04:01 +03 2026
```

This confirmed that cron was running automatically without me manually executing the command.

---

# Removing the Test Job

I opened the crontab again:

```bash
crontab -e
```

Then I removed:

```text
* * * * * date >> /home/esma_nur/data-engineering-journey/learn-linux/cron-test.log
```

After saving, I checked with:

```bash
crontab -l
```

The test job was no longer present.

---

# Commands I Tested

```bash
crontab -l

crontab -e

date

cat ~/data-engineering-journey/learn-linux/cron-test.log
```

---

# What I Learned

- `cron` schedules commands and scripts.
- Bash scripts define what should happen.
- cron defines when it should happen.
- `crontab -l` lists cron jobs.
- `crontab -e` edits cron jobs.
- cron schedules contain five time fields.
- `*` means any value.
- `*/15` can represent every 15 minutes.
- cron can automatically run commands without manual intervention.
- absolute paths are useful in automated jobs.
- cron output can be redirected into log files.

---

# Data Engineering Connection

Scheduling is an important part of data engineering.

A Data Engineer may need to run tasks such as:

```text
data ingestion
file processing
backups
log cleanup
data exports
pipeline scripts
```

at regular times.

For example:

```text
02:00 every day
        ↓
run pipeline
        ↓
process daily data
```

Cron is a simple Linux scheduling tool.

Later, more advanced data pipelines may use orchestration tools such as Airflow, but cron provides an important foundation for understanding scheduled automation.