# henriquemiranda.github.io

The site is built with [Pelican](https://getpelican.com/) from the content,
theme, and configuration in this directory.

## Local preview

From the repository root, run:

```sh
./pelican/preview
```

Then open `http://localhost:8000`. The preview rebuilds automatically whenever
you save a source file. Press `Ctrl+C` to stop it.

## Production build

```sh
pip install -r requirements.txt
pelican content -o output -s publishconf.py
```

The generated site is written to `pelican/output/` and is intentionally not
tracked. GitHub Actions deploys it to the `gh-pages` branch after every push to
`master`.
