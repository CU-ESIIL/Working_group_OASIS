# Link JupyterLab to GitHub

This page connects a running JupyterLab instance to GitHub so participants can clone the working group repository and move small project files between the instance and GitHub.

GitHub is where this working group keeps code, Markdown pages, notebooks, meeting notes, small figures, and public website content. Persistent storage is where large data and large outputs belong. The compute instance is where active work happens.

Before using this page, review the [Cloud Triangle guide](../resources/cloud-triangle.md).

## Why The Instance Needs GitHub Access

The JupyterLab instance is useful for analysis, but it is not the long-term record of the working group. Connecting it to GitHub lets participants:

- pull the latest scripts, notebooks, notes, and website files
- commit useful changes with version history
- push work back so collaborators can see it
- keep the public website synchronized with the repository

For most participants, the recommended path is GitHub web authentication with an HTTPS clone link. This avoids managing SSH keys in a temporary compute environment.

## Step 1: Launch The JupyterLab Instance

Open the working group JupyterLab or CyVerse VICE app provided by ESIIL staff or your facilitator. Wait for the instance to finish starting.

Some OASIS images include a startup notebook for GitHub authentication:

```text
startup/github_web_auth.ipynb
```

If your instance does not include this notebook, ask ESIIL staff or your facilitator which GitHub authentication method is currently supported for your environment.

## Step 2: Open The GitHub Web Auth Notebook

In JupyterLab, use the file browser to open:

```text
startup/github_web_auth.ipynb
```

Run the first cell. It should start GitHub web authentication and print:

- a one-time code
- a GitHub device login link, usually `https://github.com/login/device`

Copy the one-time code, open the device login link in a browser, paste the code, and approve the GitHub login.

## Step 3: Save The Authentication

After GitHub says authentication is complete, return to `startup/github_web_auth.ipynb` and run the second cell.

This configures Git in the running JupyterLab instance to use the GitHub authentication you just approved. After this step, HTTPS pull and push should work from the Git sidebar or terminal.

GitHub authentication can expire, especially if an instance is left running for a long time. If Git asks for credentials again, repeat the web authentication steps.

## Step 4: Add Git Identity If Asked

Authentication proves you can access GitHub. Git may still need to know who should be credited for commits.

If Git asks for your name or email, use the identity you want attached to repository commits. In a terminal, the commands look like:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.edu"
```

Use the same email associated with your GitHub account if possible.

## Step 5: Clone The Working Group Repository

Before cloning, make sure the JupyterLab file browser is at a top-level workspace folder, not inside a data folder.

Use the HTTPS clone link for this workflow:

```text
https://github.com/CU-ESIIL/Working_group_OASIS.git
```

If your group has already created its own repository from this template, use your group repository URL instead.

To clone from the JupyterLab Git panel:

1. Click the Git icon in the left sidebar.
2. Choose Clone a Repository.
3. Paste the HTTPS repository link.
4. Click Clone.
5. Confirm that the repository appears in the file browser.

## Step 6: Pull Before Working

Start each work session by pulling the latest changes. Working groups often edit over weeks or months, so someone else may have updated the repository since your last session.

Use GitHub for:

- scripts and notebooks
- Markdown pages
- meeting notes
- small figures and website assets
- README files and metadata notes

Do not use GitHub for raw rasters, large datasets, large model outputs, or temporary scratch files. Move those files to persistent storage and commit a small note explaining where they live.

## SSH Backup Option

SSH can still work for participants who already know how to manage SSH keys in temporary JupyterLab environments, but it is not the recommended first path here.

If you use SSH, create an SSH key inside the instance, add the public key to GitHub under SSH and GPG keys, and clone with an SSH URL such as:

```text
git@github.com:CU-ESIIL/Working_group_OASIS.git
```

If you are unsure which method to use, use web authentication and the HTTPS clone link.

Next page: [Push and Pull with GitHub](push-to-github.md)
