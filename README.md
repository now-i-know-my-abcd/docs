# Now I Know My ABCD

Welcome to the GitHub repository home of Now I Know My ABCD, a community-managed unofficial help resource for the ABCD Study! **Click the "Discussions" tab at the top of the page to access the help forum.**

## Issues (suggest and request updates)

If you would like to suggest an update or addition to the Now I Know My ABCD documentation site, without writing the code yourself, first navigate to the website page you'd like to suggest a change to. Then, open a GitHub issue using the "open issue" link in the GitHub drop-down menu at the top of the page. Include a comment with your issue describing your suggested change, and a site moderator will review your issue and update the website.

If you have more general ABCD questions, please visit the Discussion Board! Opening a GitHub issue is best suited to targeted content update requests and suggestions for individual pages.

## Forks and pull requests (code it yourself)

The first step to contributing to the Now I Know My ABCD docs is to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks) the GitHub repository containing the source code. In your local fork, you can write new website content or edit existing content at your own pace without affecting the main site.

Once you're ready, open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). A site moderator will review your pull request and work with you to make sure any tutorial code is reproducible. Once the updates are finalized, they will merge your updates into the main site!

## Adding pages

If you would like to propose a new tutorial page for addition to the Now I Know My ABCD docs, these instructions will help you get started. They are written for contributors who already feel comfortable with Python, Jupyter, and Markdown.

### Creating content

All new pages go into the `docs` subfolder. Text-only pages can be written in Markdown, while pages with code can be written as Jupyter notebooks. (Eventually, code pages can also be written in R Markdown, but I haven't figured out how to do that yet.)

### Adding to the table of contents

The table of contents is declared in `_toc.yml` in the project root folder. Add a page to the table of contents by adding a new line with `- file:` and then your page _filename, not the page title_ with no file ending. JupyterBook will automatically render the page's internal title (the level-1 header at the beginning of the page) as the chapter name in the table of contents.

Order matters! Add the new line where you want the resulting chapter to end up.

## Rendering the book site locally

The website is currently equipped with a GitHub Actions workflow that renders the web-hosted version of the site _every time a change is pushed on the `main` branch._ You do not need to have `jupyter-book` installed on your local machine in order to get the live website to update! 🎉 :tada: 

However, you _do_ need to have `jupyter-book` and other site dependencies installed if you want to preview website edits before pushing.

For the Python dependencies, this repo comes with a conda `environment.yml` file that you can (theoretically) use to install all relevant packages. In Monica's experience, `environment.yml` files can be picky and sometimes overly OS-specific, so please contact Monica if you have issues recreating the Python dependencies.

For the R dependencies, this repo also comes with an `renv` lockfile that will install relevant R packages. With the `renv` package installed and accessible from the R project for this repository, call `renv::restore()` and the R dependencies will hopefully install without issue.

One important package that will install with the R is `IRkernel`, which registers R as a kernel for JupyterBook to use to render the R tutorial pages. Per [their instructions](https://irkernel.github.io/installation/), once you've installed the R dependency packages, run this command _with the repository R project active:_ `IRkernel::installspec()` to actually write the kernel info file that Jupyter expects.

When you have JupyterBook set up, the following terminal command will render the book locally when run from the project root folder:

```bash
jupyter-book build docs/
```

The local book homepage should then be accessible at `docs/_build/html/index.html` in your browser window.
