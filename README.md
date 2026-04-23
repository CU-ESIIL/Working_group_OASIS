# Working Group Template

This repository is a template for ESIIL Working Groups.

The website is built from the docs/ folder using MkDocs.

## Preview locally

pip install mkdocs-material  
mkdocs serve

## Build site

mkdocs build --strict --clean

## Site Health

The site generates a non-blocking health report during the build.

The report appears at the bottom of the homepage and flags common issues such as missing files, placeholder links, outdated navigation, or incomplete template fields.

Warnings do not prevent the site from publishing. They are intended to help Working Group admins improve the site.

## GitHub Pages

This site is automatically built and deployed using GitHub Actions.
