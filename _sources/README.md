# docs-cookbook

### **GitHub page:** https://macrometacorp.github.io/docs-cookbook

## Setup

### Install jupyter book

```bash
pip install jupyter-book
```

### Build jupyter book

```bash
cd <path_to_docs-cookbook>/docs-cookbook
git checkout main
jupyter-book build --all docs-cookbook
```

### Publish jupyter book

* Install [ghp-import](https://github.com/davisp/ghp-import) (Only if the `ghp-import` has not yet been installed)

```bash
pip install ghp-import
```

* Check generated `_build` directory, make sure it is generated/updated

```bash
cd <path_to_docs-cookbook>/docs-cookbook
git checkout main
ls _build/ 
```

* Publish the jupyter book

```bash
ghp-import -n -p -f _build/html
```

## References

* [Publish Juypter book via GitHub page](https://jupyterbook.org/start/publish.html)
