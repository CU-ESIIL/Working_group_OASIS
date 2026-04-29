# Working Group Landmarks

Working group landmarks are lightweight labels that connect instruction pages to the homepage sections participants may need to edit. They are not a new workflow and they are not a visual sticker system. They are simple markers for finding the right part of the site.

## Labels

| Label | Meaning | Common homepage or repo location |
| --- | --- | --- |
| WG-A | People and roles | Team Members, community expectations, meeting notes |
| WG-B | Question and scope | Homepage title, Start Here, Current Phase, Timeline |
| WG-C | Data and access | Resources, Cloud Triangle notes, persistent storage README files |
| WG-D | Methods and workflows | Repository Side, Work Plan, scripts, notebooks, workflow galleries |
| WG-E | Results and synthesis | Website Side, outputs galleries, synthesis notes |
| WG-F | Outputs and handoff | Outputs and Wrap Up, public site guide, cite and reuse notes |

Use the labels when meeting notes or instruction pages need to point participants toward the place where a change belongs.

## How To Use The Labels

When a participant asks "Where should this go?", choose the nearest landmark:

- People, roles, responsibilities, or norms: WG-A.
- Research question, scope, purpose, or audience: WG-B.
- Dataset access, metadata, storage paths, or data provenance: WG-C.
- Scripts, notebooks, computational steps, or reproducibility notes: WG-D.
- Findings, uncertainty, figures, or interpretation: WG-E.
- Final outputs, reuse instructions, citations, or archiving: WG-F.

Add the label in plain Markdown near the relevant note. For example:

```markdown
Landmark: WG-C Data and access
```

or:

```markdown
Related landmarks: WG-D Methods and workflows; WG-E Results and synthesis
```

## Homepage Connections

The current homepage already has natural places for these labels:

- Team Members: WG-A People and roles.
- Start Here and Current Phase: WG-B Question and scope.
- Repository Side and Resources: WG-C Data and access; WG-D Methods and workflows.
- Website Side and Outputs sections: WG-E Results and synthesis; WG-F Outputs and handoff.
- Timeline: all landmarks, depending on the phase.

Keep labels subtle. A short line is enough. Do not clutter the homepage with repeated badges.

Future visual design note: if the working group later wants sticker-style visual markers, add them as a small CSS and image-system improvement rather than embedding complex HTML in Markdown.

## Related Pages

- [Working Group Lifecycle](working-group-lifecycle.md)
- [Public-Facing Site Guide](../public-facing-site-guide.md)
