# Cloud Triangle: GitHub, Compute, and Persistent Storage

Working groups usually move between three connected places:

- GitHub, where the group keeps code, documentation, meeting notes, small configuration files, small example data, and public-facing narrative.
- Persistent storage, where the group keeps large datasets, model outputs, intermediate files, rasters, tables, and shared data products.
- JupyterHub or another compute instance, where the group does active analysis, exploration, temporary processing, and interactive work.

A simple rule: use compute for active work, GitHub for small versioned materials, and persistent storage for large files that need to last.

## What Goes Where

| Item | Best home | Why |
| --- | --- | --- |
| Meeting notes | GitHub | Small, readable, and versioned |
| Scripts and notebooks | GitHub | Reproducible and collaborative |
| Small configuration files | GitHub | Easy to review and track over time |
| Small example data | GitHub | Useful for tests, demos, and documentation |
| Raw rasters or large data | Persistent storage | Too large for GitHub |
| Intermediate model outputs | Persistent storage | Large and often regenerated |
| Shared tables or data products | Persistent storage | Need to be findable by the full group |
| Final figures | GitHub if small, persistent storage if large | Should be easy to cite and reuse |
| Temporary scratch files | Compute instance | Not meant for long-term storage |
| Final reports and public docs | GitHub / website | Public-facing and versioned |

## Use GitHub For Shared Memory

Small files belong in GitHub because they are easy to version and review. GitHub is a good home for:

- Markdown pages in `docs/`
- meeting notes and decisions
- scripts, notebooks, and workflow files
- small figures used directly on the website
- metadata notes that explain where larger files live
- references, citation notes, and reuse instructions

If a future participant needs to understand why the group made a decision, GitHub should give them the trail.

## Use Persistent Storage For Large Files

Large files belong in persistent storage because GitHub is not designed for raw environmental data, rasters, model outputs, or large intermediate results.

Use persistent storage for:

- raw data
- processed data too large for GitHub
- model runs and intermediate outputs
- large figures, maps, or tables
- shared group data products
- files that need to survive after a compute instance stops

Every large data folder in persistent storage should have a small README or metadata note referenced from GitHub. That note should say what the folder contains, who created it, when it was created, how it was produced, and whether it is preliminary or ready to reuse.

## Use Compute For Active Work

JupyterHub, CyVerse VICE, or another compute instance is the place to work interactively. It is where participants open notebooks, test workflows, make plots, and inspect data.

Treat the compute instance as a workspace, not an archive. Before the end of a work session:

1. Push code, notebooks, notes, and small figures to GitHub.
2. Move large data and outputs to persistent storage.
3. Add or update a small GitHub note that explains where large files are stored.

## A Working Session Checklist

Start each work session by pulling the latest changes from GitHub. Then confirm where active files belong before creating new outputs.

- Code or documentation change? Commit it to GitHub.
- Large data or output? Save it to persistent storage.
- Temporary scratch file? Keep it on the compute instance only while you need it.
- Shared result? Document it in GitHub and point to the storage location if the file is large.

Related pages:

- [Link JupyterLab to GitHub](../instructions/link-to-github.md)
- [Push and Pull with GitHub](../instructions/push-to-github.md)
- [Save Files to Persistent Storage](../instructions/save-to-persistent-storage.md)
