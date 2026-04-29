# Save Files To Persistent Storage

Persistent storage is the shared place for large files that should survive beyond a running compute instance. Use it for data and outputs that are important to the working group but too large or too changeable for GitHub.

Confirm the exact shared storage path with ESIIL staff or your facilitator before moving important data.

Example shared path pattern:

```text
i:/iplant/home/shared/esiil/working_groups/<WORKING_GROUP_NAME>/
```

## What Belongs Here

Use persistent storage for:

- raw datasets
- rasters and large spatial files
- model outputs
- intermediate analysis products
- large tables
- shared data products
- large figures or maps
- files that need to survive after a JupyterLab instance stops

Do not use GitHub for large raw environmental data, huge rasters, model outputs, or temporary working files. Put those files in persistent storage and commit a small README or metadata note to GitHub.

## One-Time Setup

Open a JupyterLab terminal and check whether GoCommands is already available:

```bash
gocmd --help
```

If it is not installed, follow the current CyVerse GoCommands installation guidance provided by ESIIL staff or the CyVerse documentation.

Configure iRODS:

```bash
gocmd init
```

Accept the default host, port, and zone if your facilitator confirms they are correct. Use your CyVerse username when prompted.

Check that you can list your home folder:

```bash
gocmd ls i:/iplant/home/<YOUR_CYVERSE_USERNAME>
```

The `i:` prefix means an iRODS remote path. Local paths on your compute instance do not use `i:`.

## Set Group Paths

Replace the working group name and username before running these commands:

```bash
WORKING_GROUP_NAME="<WORKING_GROUP_NAME>"
USERNAME="<YOUR_CYVERSE_USERNAME>"

COMMUNITY="i:/iplant/home/shared/esiil/working_groups/${WORKING_GROUP_NAME}"
PERSONAL="i:/iplant/home/${USERNAME}"
```

Helpful shared folder names include:

- `raw_data/`
- `processed_data/`
- `outputs/`
- `figures/`
- `deliverables/`
- `scratch/`
- `metadata/`

Create folders as the group needs them:

```bash
gocmd mkdir "${COMMUNITY}/raw_data"
gocmd mkdir "${COMMUNITY}/outputs"
gocmd mkdir "${COMMUNITY}/metadata"
```

## Upload Files From Compute To Persistent Storage

Use `put` to upload local files or folders:

```bash
LOCAL_SRC="outputs/run-YYYYMMDD"
REMOTE_DST="${COMMUNITY}/outputs/"

gocmd put --progress -K --icat -r "${LOCAL_SRC}" "${REMOTE_DST}"
```

When uploading a folder again, use `--diff` so unchanged files are skipped:

```bash
gocmd put --progress -K --icat --diff -r "${LOCAL_SRC}" "${REMOTE_DST}"
```

Verify the upload:

```bash
gocmd ls "${REMOTE_DST}"
```

## Download Files From Persistent Storage

Use `get` to bring shared files into the running compute instance:

```bash
mkdir -p ./data

REMOTE_SRC="${COMMUNITY}/processed_data/"
LOCAL_DST="./data/"

gocmd get --progress -K --icat -r "${REMOTE_SRC}" "${LOCAL_DST}"
```

Use this when a collaborator has prepared shared data or outputs that you need for analysis.

## Copy Files Within Persistent Storage

Use `cp` to copy directly between two persistent storage locations:

```bash
REMOTE_SRC="${COMMUNITY}/deliverables/"
REMOTE_PERSONAL_DST="${PERSONAL}/working_groups/${WORKING_GROUP_NAME}/deliverables/"

gocmd cp --progress -K --icat -r "${REMOTE_SRC}" "${REMOTE_PERSONAL_DST}"
```

Verify the copied files:

```bash
gocmd ls "${REMOTE_PERSONAL_DST}"
```

## Compare And Sync Folders

Use `sync` when you want two folders to match:

```bash
LOCAL_SRC="outputs/latest/"
REMOTE_DST="${COMMUNITY}/outputs/latest/"

gocmd sync --progress -K --icat "${LOCAL_SRC}" "${REMOTE_DST}"
```

Be careful with sync commands. Confirm source and destination paths before running them, especially for shared folders.

## Document Shared Data

Leave a README next to any shared data folder so someone else can understand what it contains. Also reference that README or storage location from GitHub.

A useful data README includes:

- folder path
- short description
- data source or provenance
- creator or point of contact
- date created or updated
- processing steps
- file formats
- known limitations
- reuse or citation guidance
- whether the files are preliminary or final

Example note to commit in GitHub:

```text
Large model outputs for the first synthesis run are stored in:
i:/iplant/home/shared/esiil/working_groups/<WORKING_GROUP_NAME>/outputs/synthesis-run-01/

See README.md in that folder for provenance, processing notes, and reuse guidance.
```

Related pages:

- [Cloud Triangle](../resources/cloud-triangle.md)
- [Push and Pull with GitHub](push-to-github.md)
