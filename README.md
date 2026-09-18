# Henrique Miranda’s website

This repository contains the source for [henriquemiranda.github.io](https://henriquemiranda.github.io), built with [Pelican](https://getpelican.com/).

## Local preview

From the repository root:

```sh
./pelican/preview
```

Then open <http://localhost:8000>. Press `Ctrl+C` to stop the preview server.

## Build manually

```sh
cd pelican
pip install -r requirements.txt
pelican content -o output -s publishconf.py
```

The generated site is written to `pelican/output/`. GitHub Actions builds and
publishes it to the `gh-pages` branch whenever `master` is updated.

The publication list is generated from [`pelican/content/publications.bib`](pelican/content/publications.bib), which is also made available for download on the site.
