# henriquemiranda.github.io

The site is built with [Pelican](https://getpelican.com/) from the content,
theme, and configuration in this directory.

## Local build

```sh
pip install -r requirements.txt
pelican content -o output -s publishconf.py
```

The generated site is written to `pelican/output/` and is intentionally not
tracked. GitHub Actions deploys it to the `gh-pages` branch after every push to
`master`.
