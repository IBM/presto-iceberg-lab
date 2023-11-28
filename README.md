# Advocacy Workshop

This is a template for workshops hosted on GitHub Pages using Material for MkDocs. To view it online, go to:

<https://ibm.github.io/presto-iceberg-lab>

Create a new repo based off this template, and use the following folders as a guide:

```ini

- conf (configuration files to be used)
- docs (workshop content)
|_ <folder-n> (these are exercises for the workshop)
  |_README.md (the steps for the exercise, in Markdown)
|_ README.md (this will appear on the gitbook home page)
.mkdocs.yaml (configuration for mkdocs)
.travis.yaml (runs markdownlint by default)
README.md (only used for GitHub.com)
```

## Tips and conventions

### Screenshots

Screenshots look better if they are full page.
Use [ImageMagick](https://imagemagick.org) to create a nice border around images with this command:

```bash
magick mogrify -bordercolor gray -border 2
```
