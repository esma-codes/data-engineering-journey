# Linux Permissions and Users

Linux uses users, groups, and permissions to control who can access files and directories.

This is important in data engineering because pipelines, scripts, services, databases, and shared servers often run under different users.

---

# `whoami`

`whoami` shows the current Linux user.

Example:

```bash
whoami
```

Output:

```text
esma_nur
```

This means I am currently working as the `esma_nur` user.

---

# `id`

`id` shows information about the current user and their groups.

Example:

```bash
id
```

Example output:

```text
uid=1000(esma_nur)
gid=1000(esma_nur)
groups=1000(esma_nur),27(sudo)
```

Important parts:

```text
uid    → user ID
gid    → primary group ID
groups → groups the user belongs to
```

Being a member of the `sudo` group allows the user to run commands with elevated privileges using `sudo`.

Example:

```bash
sudo apt update
```

---

# Viewing Permissions

Permissions can be viewed with:

```bash
ls -l
```

Example:

```text
-rw-r--r-- 1 esma_nur esma_nur file.txt
```

The permission section is:

```text
-rw-r--r--
```

It can be divided into:

```text
- | rw- | r-- | r--
    user  group others
```

---

# File Type

The first character represents the file type.

```text
- → regular file
d → directory
l → symbolic link
```

Example:

```text
-rw-r--r--
```

starts with `-`, so it is a regular file.

Example:

```text
drwxr-xr-x
```

starts with `d`, so it is a directory.

---

# Permission Symbols

Linux uses three main permission symbols:

```text
r → read
w → write
x → execute
```

A missing permission is represented by:

```text
-
```

Example:

```text
rw-
```

means:

```text
read    → allowed
write   → allowed
execute → not allowed
```

---

# User, Group, and Others

Permissions are divided into three categories:

```text
u → user / owner
g → group
o → others
```

Example:

```text
-rw-r--r--
```

can be read as:

```text
rw- → owner
r-- → group
r-- → others
```

So:

- the owner can read and write
- the group can only read
- other users can only read

---

# Owner and Group

In this output:

```text
-rw-r--r-- 1 esma_nur esma_nur file.txt
```

the two names mean:

```text
first esma_nur  → owner
second esma_nur → group
```

---

# `chmod` — Change Permissions

`chmod` means:

```text
change mode
```

It changes file or directory permissions.

---

# Adding and Removing Permissions

Symbols can be used with `chmod`.

```text
+ → add permission
- → remove permission
```

Example:

```bash
chmod u+x hello.sh
```

means:

```text
u → owner
+ → add
x → execute
```

So it adds execute permission for the owner.

Example:

```bash
chmod g+w file.txt
```

adds write permission to the group.

Example:

```bash
chmod o-r file.txt
```

removes read permission from others.

---

# Execute Permission on Files

A script may exist but still not be directly executable.

Example:

```bash
echo 'echo "Hello from script"' > hello.sh
```

Without execute permission:

```bash
./hello.sh
```

may return:

```text
Permission denied
```

After:

```bash
chmod u+x hello.sh
```

the script can be executed:

```bash
./hello.sh
```

Example output:

```text
Hello from script
```

---

# Meaning of `./`

Example:

```bash
./hello.sh
```

means:

```text
.          → current directory
./hello.sh → hello.sh inside the current directory
```

---

# Permissions on Directories

Permissions have slightly different meanings for directories.

For a directory:

```text
r → list directory contents
w → create or remove entries inside the directory
x → access / enter the directory
```

Example:

```bash
ls -ld permission-folder
```

may show:

```text
drwxr-xr-x
```

The first `d` means it is a directory.

For the owner:

```text
rwx
```

means the owner can read, modify, and access the directory.

---

# Directory Execute Permission

For directories, `x` does not mean "run the directory".

It means the user can access or enter it.

Example:

```bash
chmod u-x permission-folder
```

After removing `x`, trying:

```bash
cd permission-folder
```

may return:

```text
Permission denied
```

The permission can be restored with:

```bash
chmod u+x permission-folder
```

---

# Numeric Permissions

Linux permissions can also be represented using numbers.

```text
r = 4
w = 2
x = 1
```

The values are added together.

Examples:

```text
rwx = 4 + 2 + 1 = 7
rw- = 4 + 2     = 6
r-x = 4 + 1     = 5
r-- = 4         = 4
---             = 0
```

Example:

```bash
chmod 644 file.txt
```

means:

```text
6 → rw- → owner
4 → r-- → group
4 → r-- → others
```

Result:

```text
-rw-r--r--
```

Another common example:

```bash
chmod 755 hello.sh
```

means:

```text
7 → rwx → owner
5 → r-x → group
5 → r-x → others
```

Result:

```text
-rwxr-xr-x
```

I do not need to memorize every numeric permission immediately.

The important idea is understanding what the permissions mean.

---

# Ownership Commands

Linux also provides commands for changing ownership.

```text
chown → change owner
chgrp → change group
```

Example:

```bash
sudo chown user file.txt
```

would change the owner of the file.

These commands were introduced conceptually, but I did not change ownership during this lab.

---

# Commands I Tested

```bash
whoami
id

ls -l
ls -l permission-test.txt

touch permission-test.txt

chmod u+x permission-test.txt
chmod g+w permission-test.txt
chmod o-r permission-test.txt

echo 'echo "Hello from script"' > hello.sh
ls -l hello.sh
chmod u+x hello.sh
./hello.sh

mkdir permission-folder
ls -ld permission-folder

touch permission-folder/test.txt
chmod u-x permission-folder
cd permission-folder

chmod u+x permission-folder
cd permission-folder
cd ..

chmod 644 permission-test.txt
chmod 755 hello.sh
```

---

# What I Learned

- Linux has users and groups.
- `whoami` shows the current user.
- `id` shows user and group information.
- `r` means read.
- `w` means write.
- `x` means execute or access.
- permissions are separated into owner, group, and others.
- `chmod` changes permissions.
- `u`, `g`, and `o` represent user, group, and others.
- `+` adds a permission.
- `-` removes a permission.
- scripts often need execute permission.
- directory permissions work slightly differently from file permissions.
- numeric permissions such as `644` and `755` are another way to represent permissions.
- file ownership and permissions are different concepts.

---

# Data Engineering Connection

A Data Engineer may work with:

```text
pipeline scripts
data files
log files
shared servers
Docker containers
cloud virtual machines
scheduled jobs
database services
```

Permissions can cause problems such as:

```text
Permission denied
Cannot read input file
Cannot write pipeline output
Cannot execute script
Cannot access directory
```

Understanding Linux permissions helps me understand why a pipeline or program cannot access a file instead of blindly changing permissions.