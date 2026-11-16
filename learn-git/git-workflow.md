# Git Workflow

This note summarizes the Git workflow I use during my Data Engineering journey.

## 1. Check the Repository

Before making changes:

```bash
git status
```

`git status` shows:

- the current branch
- modified files
- untracked files
- staged files
- whether the local branch is ahead of or behind the remote branch

---

## 2. Working Directory

The **working directory** contains the files I am currently editing.

Example:

```text
git-basics.md
```

If I modify a tracked file, Git detects the change.

I can inspect the exact changes with:

```bash
git diff
```

---

## 3. Staging Area

The staging area contains the changes I want to include in the next commit.

```bash
git add file-name
```

Example:

```bash
git add learn-git/git-basics.md
```

To see staged changes:

```bash
git diff --staged
```

The basic flow is:

```text
Working Directory
        ↓ git add
Staging Area
        ↓ git commit
Local Git History
```

---

## 4. Commit

A commit creates a snapshot in the local Git history.

```bash
git commit -m "docs: add Git notes"
```

`-m` means **message**.

To inspect commit history:

```bash
git log --oneline
```

Useful options:

- `--oneline` → shows each commit in a short format
- `-1` → shows only the latest commit
- `--graph` → displays the branch structure
- `--all` → includes all branches

Example:

```bash
git log --oneline --graph --all
```

Each commit has its own unique commit ID.

---

## 5. Push

A commit is initially stored only in the local repository.

To send local commits to GitHub:

```bash
git push
```

Flow:

```text
Working Directory
        ↓
Staging Area
        ↓
Local Commit
        ↓ git push
GitHub
```

---

## 6. Local and Remote Repository

`origin` is the default short name for the remote GitHub repository.

```bash
git remote -v
```

`-v` means **verbose** and shows more information.

Example concepts:

```text
main
```

The local branch.

```text
origin/main
```

The remote-tracking reference for the `main` branch on `origin`.

---

## 7. Fetch and Pull

### Fetch

```bash
git fetch
```

Downloads information about remote changes without directly updating my current working branch.

### Pull

```bash
git pull
```

Downloads remote changes and integrates them into the current branch.

Simplified mental model:

```text
git pull ≈ git fetch + integrate
```

---

## 8. Branches

A branch is a separate line of development inside the same repository.

View branches:

```bash
git branch
```

The `*` symbol shows the active branch.

Create a new branch and switch to it:

```bash
git switch -c branch-name
```

`-c` means **create**.

Switch to an existing branch:

```bash
git switch main
```

Typical workflow:

```text
main
  \
   feature-branch
```

Work is performed on the feature branch without directly changing `main`.

---

## 9. Merge

To merge another branch into the current branch:

```bash
git merge branch-name
```

Example:

```bash
git switch main
git merge git-practice
```

After a branch has been successfully merged, it can be deleted:

```bash
git branch -d git-practice
```

`-d` means **delete**.

---

## 10. Merge Conflicts

A merge conflict can happen when different branches modify the same part of a file differently.

Git may show markers such as:

```text
<<<<<<< HEAD
Current version
=======
Incoming version
>>>>>>> other-branch
```

In VS Code, common options include:

- Accept Current Change
- Accept Incoming Change
- Accept Both Changes
- Compare Changes

Conflict resolution workflow:

```text
Inspect both changes
        ↓
Decide the correct final code
        ↓
Remove conflict markers
        ↓
git add
        ↓
git commit
```

`git add` after resolving a conflict tells Git that the file has been resolved.

---

## 11. Undoing Changes

### Remove a file from the staging area

```bash
git restore --staged file-name
```

The file is not deleted. It is simply removed from the staging area.

### Discard local changes

```bash
git restore file-name
```

This can permanently discard uncommitted changes, so it should be used carefully.

---

## 12. Amend the Latest Commit

To modify the latest commit before pushing:

```bash
git commit --amend -m "new commit message"
```

`--amend` recreates the latest commit.

This also changes the commit ID.

It is safest to use `--amend` before the commit has been pushed to a shared remote repository.

---

## 13. .gitignore

`.gitignore` tells Git which untracked files or folders should normally be ignored.

Examples:

```gitignore
*.log
logs/
output.txt
```

Meaning:

```text
*.log      → ignore files ending in .log
logs/      → ignore the logs directory
output.txt → ignore a specific file
```

`.gitignore` does not automatically stop tracking a file that has already been committed.

---

## My Daily Git Workflow

A simple workflow I can use in future Data Engineering projects:

```bash
git status
git pull

# make changes

git diff
git add <files>
git diff --staged
git commit -m "meaningful commit message"
git push
```

For feature development:

```bash
git switch -c feature-name

# work and commit

git switch main
git pull
git merge feature-name
git push
git branch -d feature-name
```

---

## Core Mental Model

```text
Edit
 ↓
git status / git diff
 ↓
git add
 ↓
git commit
 ↓
git push
 ↓
GitHub
```

Git manages the history.

GitHub stores and shares the remote repository.