# README

## Adding pages

### Creating content

All new pages go into the `docs` subfolder. Text-only pages can be written in Markdown, while pages with code can be written as Jupyter notebooks. (Eventually, code pages can also be written in R Markdown, but I haven't figured out how to do that yet.)

### Adding to the table of contents

The table of contents is declared in `_toc.yml` in the project root folder. Add a page to the table of contents by adding a new line with `- file:` and then your page _filename, not the page title_ with no file ending. JupyterBook will automatically render the page's internal title (the level-1 header at the beginning of the page) as the chapter name in the table of contents.

Order matters! Add the new line where you want the resulting chapter to end up.

## Rendering the book site

Currently, only Monica has the `jupyter-book` package installed. However, this repo comes with a conda `environment.yml` file that you can (theoretically) use to install all relevant packages.

when you have JupyterBook set up, the following terminal command will render the book when run from the project root folder:

```bash
jupyter-book build docs/
```

The local book homepage should then be accessible at `docs/_build/html/index.html` in your browser window.
