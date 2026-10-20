# Linux Links

Linux supports different types of links that provide alternative ways to access files.

The two main types are:

```text
symbolic link
hard link
```

---

# Symbolic Link

A symbolic link, also called a symlink, points to another file or directory.

It behaves similarly to a shortcut.

Example:

```bash
echo "customer data" > original.txt
```

Create a symbolic link:

```bash
ln -s original.txt shortcut.txt
```

Here:

```text
ln → create link
-s → create a symbolic link
```

Now:

```text
shortcut.txt → original.txt
```

The link does not contain a second copy of the data.

It points to the target path.

---

# Viewing a Symbolic Link

```bash
ls -l
```

A symbolic link may appear like:

```text
lrwxrwxrwx ... shortcut.txt -> original.txt
```

The first:

```text
l
```

means:

```text
symbolic link
```

---

# Reading Through a Symbolic Link

```bash
cat shortcut.txt
```

reads the content of:

```text
original.txt
```

because the symlink redirects access to the target.

---

# Broken Symbolic Link

If the original target is removed:

```bash
rm original.txt
```

the symlink may still exist.

However:

```bash
cat shortcut.txt
```

will fail because the target file no longer exists.

This is called a:

```text
broken symlink
```

---

# Why Symbolic Links Are Useful

Symbolic links can provide stable or shorter paths without copying data.

For example:

```text
/data/runs/2026-10-20/customers.csv
```

could be referenced by:

```text
/data/latest-customers.csv
```

A pipeline can always use:

```text
latest-customers.csv
```

while the real target changes.

Another example:

```text
/spark/current → /spark/spark-4.1/
```

This allows applications to use a stable path such as:

```text
/spark/current
```

even when the installed version changes.

---

# Hard Link

A hard link is another name for the same underlying file data.

Example:

```bash
echo "important customer data" > data.txt
```

Create a hard link:

```bash
ln data.txt data-hardlink.txt
```

Unlike a symbolic link, no `-s` option is used.

---

# Inodes

Linux files are represented internally using structures called inodes.

I can display inode numbers with:

```bash
ls -li data.txt data-hardlink.txt
```

Example:

```text
123456 ... data.txt
123456 ... data-hardlink.txt
```

Both names have the same inode number.

This means they refer to the same underlying file.

---

# Removing One Hard Link

If I remove:

```bash
rm data.txt
```

I can still read:

```bash
cat data-hardlink.txt
```

because another hard link still references the same underlying file.

The file data remains available while at least one hard link still exists.

---

# Symbolic Link vs Hard Link

```text
Symbolic link
    ↓
points to another path

Hard link
    ↓
another name for the same underlying file
```

If the target name of a symbolic link disappears:

```text
symlink → broken
```

If one hard link name disappears:

```text
other hard links → still work
```

---

# Commands I Tested

```bash
mkdir -p links-lab
cd links-lab

echo "customer data" > original.txt

ln -s original.txt shortcut.txt

ls -l

cat shortcut.txt

rm original.txt

cat shortcut.txt

echo "important customer data" > data.txt

ln data.txt data-hardlink.txt

cat data.txt
cat data-hardlink.txt

ls -li data.txt data-hardlink.txt

rm data.txt

cat data-hardlink.txt
```

---

# What I Learned

- `ln` creates links.
- `ln -s` creates symbolic links.
- a symbolic link points to another file or directory path.
- symbolic links do not create another copy of the data.
- a symlink can become broken if its target disappears.
- a hard link is another name for the same underlying file.
- hard links share the same inode.
- deleting one hard-link name does not immediately delete the data if another hard link still exists.
- symbolic links are useful for stable paths such as `latest` or `current`.

---

# Data Engineering Connection

Links can help manage changing file paths and software versions.

A Data Engineer may encounter symbolic links in situations such as:

```text
latest dataset
current software version
shared configuration
log directories
server file layouts
```

A useful mental model is:

```text
symbolic link → flexible path reference
hard link     → another name for the same file
```