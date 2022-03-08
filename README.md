# docs-cookbook

## Setup

### Install jupyter book

```bash
pip install jupyter-book
```

### Build jupyter book

```bash
cd <path_to_docs-cookbook>/docs-cookbook
git checkout vz-quick-start
jupyter-book build --all docs-cookbook
```

### Publish jupyter book

* Install [ghp-import](https://github.com/davisp/ghp-import) (Only if the `ghp-import` has not yet been installed)

```bash
pip install ghp-import
```

* Move the build output directory `_build` to the `gh-page` repo

```bash
cd <path_to_docs-cookbook>/docs-cookbook
git checkout main
mv ./_build /tmp
git checkout main
mv /tmp/_build ./
```

* 

## References

* [Publish Juypter book via GitHub page](https://jupyterbook.org/start/publish.html)
