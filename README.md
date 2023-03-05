# README

## Adding pages

### Creating content

All new pages go into the `docs` subfolder. Text-only pages can be written in Markdown, while pages with code can be written as Jupyter notebooks. (Eventually, code pages can also be written in R Markdown, but I haven't figured out how to do that yet.)

### Adding to the table of contents

The table of contents is declared in `_toc.yml` in the project root folder. Add a page to the table of contents by adding a new line with `- file:` and then your page _filename, not the page title_ with no file ending. JupyterBook will automatically render the page's internal title (the level-1 header at the beginning of the page) as the chapter name in the table of contents.

Order matters! Add the new line where you want the resulting chapter to end up.

## Rendering the book site locally

The website is currently equipped with a GitHub Actions workflow that renders the web-hosted version of the site _every time a change is pushed on the `main` branch._ You do not need to have `jupyter-book` installed on your local machine in order to get the live website to update! :tada: 

However, you _do_ need to have `jupyter-book` and other site dependencies installed if you want to preview website edits before pushing.

For the Python dependencies, this repo comes with a conda `environment.yml` file that you can (theoretically) use to install all relevant packages. In Monica's experience, `environment.yml` files can be picky and sometimes overly OS-specific, so please contact Monica if you have issues recreating the Python dependencies.

For the R dependencies, this repo also comes with an `renv` lockfile that will install relevant R packages. With the `renv` package installed and accessible from the R project for this repository, call `renv::restore()` and the R dependencies will hopefully install without issue.

One important package that will install with the R is `IRkernel`, which registers R as a kernel for JupyterBook to use to render the R tutorial pages. Per [their instructions](https://irkernel.github.io/installation/), once you've installed the R dependency packages, run this command _with the repository R project active:_ `IRkernel::installspec()` to actually write the kernel info file that Jupyter expects.

When you have JupyterBook set up, the following terminal command will render the book locally when run from the project root folder:

```bash
jupyter-book build docs/
```

The local book homepage should then be accessible at `docs/_build/html/index.html` in your browser window.
