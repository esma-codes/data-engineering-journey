# Filesystem and Navigation

## Linux Filesystem

Linux uses a hierarchical filesystem.

The filesystem starts from the **root directory**:

```text
/
```

Everything in the Linux filesystem is organized under this root directory.

Example:

```text
/
└── home
    └── esma_nur
        └── data-engineering-journey
            └── learn-linux
```

---

## Root Directory

The `/` symbol represents the **root directory**.

It is the highest level of the Linux filesystem.

An absolute path starts from `/`.

Example:

```text
/home/esma_nur/data-engineering-journey/learn-linux
```

---

## Home Directory

My home directory is:

```text
/home/esma_nur
```

The `~` symbol represents my home directory.

For example:

```bash
cd ~
```

moves me directly to my home directory.

---

## Important Path Symbols

```text
/   -> root directory
~   -> home directory
.   -> current directory
..  -> parent directory
```

### Current Directory

`.` represents the directory I am currently inside.

Example:

```bash
code .
```

This means:

> Open the current directory in Visual Studio Code.

### Parent Directory

`..` represents the directory one level above the current directory.

Example:

```bash
cd ..
```

moves me one directory up.

---

## Absolute Path

An **absolute path** describes the complete location of a file or directory starting from the root `/`.

Example:

```text
/home/esma_nur/data-engineering-journey/learn-linux
```

Because it starts with `/`, Linux knows exactly where the location is.

---

## Relative Path

A **relative path** describes a location starting from the directory I am currently inside.

For example, if I am currently inside:

```text
/home/esma_nur/data-engineering-journey
```

I can move into the Linux folder using:

```bash
cd learn-linux
```

instead of writing the complete path:

```bash
cd /home/esma_nur/data-engineering-journey/learn-linux
```

---

# Navigation Commands

## pwd

```bash
pwd
```

`pwd` means:

**Print Working Directory**

It shows my current location in the filesystem.

Example output:

```text
/home/esma_nur/data-engineering-journey/learn-linux
```

---

## ls

```bash
ls
```

Lists the files and directories inside the current directory.

### Show Hidden Files

```bash
ls -a
```

`-a` means **all**.

It also shows hidden files.

In Linux, files whose names begin with `.` are usually hidden.

Examples:

```text
.bashrc
.profile
.git
```

---

## Detailed List

```bash
ls -l
```

Shows more information about files and directories.

This can include:

- file type
- permissions
- owner
- group
- file size
- modification time
- file name

---

## Hidden Files + Detailed Information

```bash
ls -la
```

This combines:

```text
-l -> detailed list
-a -> include hidden files
```

---

# Understanding `ls -l`

Example:

```text
-rw-r--r-- 1 esma_nur esma_nur 1500 Oct 12 linux-environment.md
```

The first character tells me the file type.

```text
d -> directory
- -> regular file
l -> symbolic link
```

For example:

```text
drwxr-xr-x
```

starts with `d`, so it represents a directory.

```text
-rw-r--r--
```

starts with `-`, so it represents a regular file.

---

## Permission Letters

I have also seen these letters:

```text
r -> read
w -> write
x -> execute
```

I will study Linux permissions in more detail later.

---

## cd

`cd` means:

**Change Directory**

It is used to move between directories.

Example:

```bash
cd learn-linux
```

moves into the `learn-linux` directory.

### Move One Level Up

```bash
cd ..
```

### Move to Home Directory

```bash
cd ~
```

or simply:

```bash
cd
```

### Return to the Previous Directory

```bash
cd -
```

---

# Commands I Tested

```bash
pwd
ls
ls -a
ls -l
ls -la
cd ..
cd ~
cd -
code .
```

---

# What I Learned

- Linux uses a hierarchical filesystem.
- `/` represents the root directory.
- `~` represents my home directory.
- `.` represents my current directory.
- `..` represents the parent directory.
- Absolute paths start from `/`.
- Relative paths start from my current location.
- `pwd` shows my current location.
- `ls` lists files and directories.
- `cd` changes directories.
- `ls -la` helps me inspect files, hidden files, and basic file information.

---

# Data Engineering Connection

Data engineers frequently work with files, directories, logs, datasets, scripts, and servers.

Understanding filesystem navigation helps me:

- locate datasets
- move between project directories
- inspect pipeline files
- work on remote Linux servers
- manage data directories
- understand paths used by Python, Docker, databases, and data pipelines