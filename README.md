# docs-xbook

### **GitHub page:** https://macrometacorp.github.io/notebooks/

## Setup

### Install jupyter book

```bash
pip install jupyter-book
```

### Build jupyter book

```bash
cd <path_to_docs-xbook>/docs-xbook
git checkout main
jupyter-book build --all docs-xbook
```

### Run jupyter book locally

To run your book locally, you can open the generated HTML files in your browser. 
Eenter the absolute path to the file in your browser navigation bar adding `file://` at the beginning (e.g. `file:///Users/xxxxx/docs-xbook/_build/index.html`).

### Publish jupyter book

* Install [ghp-import](https://github.com/davisp/ghp-import) (Only if the `ghp-import` has not yet been installed)

```bash
pip install ghp-import
```

* Check generated `_build` directory, make sure it is generated/updated

```bash
cd <path_to_docs-xbook>/docs-xbook
git checkout main
ls _build/ 
```

* Publish the jupyter book

```bash
ghp-import -n -p -f _build/html
```

## References

* [Publish Juypter book via GitHub page](https://jupyterbook.org/start/publish.html)
