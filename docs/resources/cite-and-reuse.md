# Cite And Reuse

Working groups create materials that others may want to understand, cite, adapt, or build on. This page helps the group make outputs reusable without making the repository harder to maintain.

## Separate Preliminary Materials From Final Outputs

Mark working materials clearly. A draft plot, exploratory notebook, or temporary model run can be useful, but readers should know it is preliminary.

Use simple labels such as:

- Preliminary
- Draft
- Ready for internal review
- Ready for public reuse
- Archived output

## Cite Datasets And Software

When the group uses a dataset, software package, model, or workflow from someone else, record enough information for another person to find it.

Useful citation details include:

- title or package name
- creators or maintainers
- version or access date
- DOI or stable URL
- license or terms of use
- short note on how it was used

If the repository uses a bibliography file, add references there and cite them in Markdown using the repository convention. If no bibliography file exists yet, keep citation notes in a simple Markdown references section until the group decides on a citation workflow.

## Link To Archived Outputs

Final outputs should be easy to find from the website. Link to:

- reports
- manuscripts
- figures
- dashboards
- notebooks
- reusable scripts
- archived datasets or data products
- persistent storage metadata notes

Large files should live in persistent storage or an approved archive, not in GitHub. GitHub should contain the public explanation and the pointer to the large file.

## Document Data Provenance

For each reusable data product, explain:

- where the source data came from
- who processed it
- when it was processed
- which script, notebook, or workflow produced it
- what assumptions or filters were applied
- what quality checks were performed
- what limitations remain

This information can live in a README beside the data in persistent storage, with a short pointer committed to GitHub.

## Add Licenses Where Appropriate

The repository has a license for repository materials. Data, figures, software, and reports may need their own reuse notes depending on source data terms and group agreements.

When in doubt, ask ESIIL staff or your facilitator before adding a license statement to a data product or public output.

## Tell Others How To Reuse The Work

For each final output, add a short reuse note:

- what the output is
- whether it is final or preliminary
- how to cite it
- where the source files live
- what files are needed to reproduce it
- who to contact with questions

Example:

```text
Reuse note: This figure is a final working group output. Please cite the working group website and the archived dataset listed in the figure caption. Source notebook: notebooks/figure-01.ipynb. Large intermediate files are stored in persistent storage with a README describing provenance and processing.
```

Related pages:

- [Cloud Triangle](cloud-triangle.md)
- [Save Files to Persistent Storage](../instructions/save-to-persistent-storage.md)
