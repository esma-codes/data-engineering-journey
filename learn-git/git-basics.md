# Git Basics

Git fundamentals for my Data Engineering journey.

## Git vs GitHub

**Git** is a version control system.

It tracks changes in files and keeps a history of a project.

**GitHub** is a platform that hosts Git repositories remotely and makes collaboration easier.

```text
Git    → version control
GitHub → remote repository hosting and collaboration
```

Git can be used without GitHub.

---

## Repository

A **repository (repo)** is a project that Git tracks.

My Data Engineering learning repository:

```text
data-engineering-journey
```

A repository contains project files together with their Git history.

---

## Local Repository

The **local repository** is the Git repository stored on my computer.

Example:

```text
~/data-engineering-journey
```

I can edit files and create commits locally without immediately sending them to GitHub.

---

## Remote Repository

A **remote repository** is a version of the repository stored somewhere else, such as GitHub.

My local repository can communicate with its remote repository using commands such as:

```text
push
fetch
pull
```

---

## origin

`origin` is the conventional short name Git uses for the remote repository.

For example:

```bash
git remote -v
```

may show:

```text
origin  https://github.com/.../data-engineering-journey.git
```

So:

```text
origin
↓
remote GitHub repository
```

`origin` is not a branch.

---

## main

`main` is usually the primary branch of a repository.

Example:

```text
main
```

means my local `main` branch.

```text
origin/main
```

represents Git's local reference to the `main` branch on the remote named `origin`.

---

## Branch

A **branch** is a separate line of development inside the same repository.

A branch is not a folder.

For example:

```text
main
  \
   feature-branch
```

A new feature can be developed on another branch without immediately changing `main`.

After the work is ready, the branches can be merged.

---

## Working Directory

The **working directory** contains the project files I am currently editing.

When I change a file, the change starts here.

---

## Staging Area

The **staging area** contains changes selected for the next commit.

```text
Working Directory
        ↓ git add
Staging Area
```

`git add` does not send anything to GitHub.

It only prepares selected changes for a commit.

---

## Commit

A **commit** is a snapshot of selected changes in the Git history.

```text
Working Directory
        ↓
Staging Area
        ↓
Commit
```

Every commit has:

- a commit ID
- a commit message
- the recorded changes

Commits are initially local.

They are sent to the remote repository with `git push`.

---

## Core Git Model

```text
Edit files
    ↓
Working Directory
    ↓ git add
Staging Area
    ↓ git commit
Local Git History
    ↓ git push
GitHub / Remote Repository
```

This model is the foundation of the Git workflow.