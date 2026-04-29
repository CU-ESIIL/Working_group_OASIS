# Push and Pull with GitHub

This page covers moving code, Markdown, notebooks, meeting notes, and small project files between JupyterLab and GitHub.

Before using this page, complete [Link JupyterLab to GitHub](link-to-github.md). For large data and outputs, use [persistent storage](save-to-persistent-storage.md) instead of GitHub.

## The Everyday Pattern

Start each work session by pulling the latest changes.

1. Pull from GitHub.
2. Edit files in JupyterLab or GitHub.
3. Stage the files that belong in the change.
4. Commit with a short message.
5. Push back to GitHub.

This rhythm keeps work visible to collaborators and prevents the working group from splitting into many disconnected copies of the same repository.

## Pull The Latest Changes

In the JupyterLab Git panel, click Pull before editing. This brings in changes that other participants have pushed.

Pull first when you:

- start a new work session
- switch between computers or compute instances
- return after a meeting
- begin editing a file someone else may have touched

If the pull fails, pause and ask for help before doing a large amount of new work.

## Stage And Commit Your Edits

After editing files, open the Git panel and review the changed files.

Stage only the files that belong together. A commit should describe one coherent change, such as:

```text
Add kickoff meeting notes
```

or:

```text
Update data access notes
```

Good working group commits are small enough that someone else can understand them later.

## Push Your Commits

Click Push to send your commits back to GitHub. After pushing, refresh the GitHub repository or public site to confirm the change landed.

If the push is rejected, GitHub probably has newer changes that your instance does not have yet. Pull first, resolve any conflicts, commit, and push again.

## Coordinate Across Weeks Or Months

Working groups continue beyond a single meeting, so coordination matters.

Use GitHub for:

- documentation and public website text
- scripts and notebooks
- meeting notes and decision logs
- small figures used on the website
- README files that point to larger data

Use persistent storage for:

- raw datasets
- large rasters
- model outputs
- intermediate results
- large tables
- files that should survive after the compute instance stops

Persistent storage is not a replacement for GitHub. It keeps large files available, but it does not provide the same version history, review workflow, or website publishing path.

## Simple Merge Conflicts

A merge conflict means Git found two edits to the same part of a file and needs a person to choose what remains.

Conflicted files may contain markers like this:

```text
<<<<<<< HEAD
your edits
=======
teammate edits
>>>>>>> origin/main
```

To resolve a simple conflict:

1. Open the file.
2. Decide what text should remain.
3. Delete the conflict markers.
4. Save the file.
5. Stage, commit, and push.

If the conflict is in a notebook, generated file, or a file you do not understand, ask for help before editing it.

## Large File Warning

If GitHub rejects a file because it is too large, move that file to persistent storage. Then commit a small README, metadata note, or website note that explains:

- where the file is stored
- what it contains
- who created it
- whether it is preliminary or final
- how collaborators should use it

See [Save Files to Persistent Storage](save-to-persistent-storage.md) for transfer examples.

## Quick Reference

- Pull before you start editing.
- Stage only the files that belong in the commit.
- Commit with a short, specific message.
- Push after committing.
- Keep large data and outputs out of GitHub.
- Leave notes in GitHub that point to persistent storage.
