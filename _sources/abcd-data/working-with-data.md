# Working with the data: tools & packages

*Last reviewed: October 2026 (ABCD Release 7.0). Official source: [ABCD docs: Tools](https://docs.abcdstudy.org/latest/tools/tools.html) and [Packages](https://docs.abcdstudy.org/latest/tools/packages.html).*

This page collects the official and community tools for finding variables, building datasets, computing scores, and modeling ABCD data. Package versions noted here were current at last review, so check each link for updates.

## 1. Finding variables

### DEAP Data Dictionary & Ontology Explorer (official)

[DEAP](https://abcd.deapscience.com) lets you browse every variable by domain (ontology tree), with descriptions, value levels, and per-variable **data-consideration** and **responsible-use** flags. **No DUC is needed to browse the dictionary.** Search is keyword-based (space-separated terms are combined with AND). [Docs](https://docs.deapscience.com/datasets/data_dictionary.html)

### ABCD Data Dictionary Semantic Search (community)

The [**ABCD Data Dictionary Semantic Search**](https://beepboopstats.com/abcd-dictionary) app, by Biplabendu Das, lets you describe what you're looking for in **plain language** (e.g., "sleep problems reported by parents" or "neighborhood safety") and returns the most related variables, even when they don't share your exact words.

- **How it works:** it compares a sentence embedding of your query with embeddings of each variable's label (all-MiniLM-L6-v2) and ranks results by cosine similarity. You can filter by similarity threshold, source, domain, and variable type.
- **Why it's useful:** ABCD has tens of thousands of variables with cryptic names, and keyword search misses synonyms. Semantic search helps with that.
- **Output:** export the matching variables to CSV, and copy a ready-made code snippet that feeds them into `NBDCtools::create_dataset()`.
- **Coverage:** 6.0 and 7.0 data dictionaries. No DUC needed, since it searches only metadata.
- **Links:** [App (beepboopstats.com)](https://beepboopstats.com/abcd-dictionary) · [mirror (shinyapps.io)](https://biplabendu.shinyapps.io/abcd-dictionary/) · [7.0 version on Hugging Face](https://lezhang100-shiny-chatbot-dictionary-abcd.hf.space/) · [GitHub](https://github.com/biplabendu/shiny-chatbot-dictionary-abcd) · [Docs](https://biplabendu.github.io/shiny-chatbot-dictionary-abcd) · [Demo video](https://www.youtube.com/watch?v=9NmK5mdekfM)

```{caution}
Semantic search is a discovery aid, not a substitute for reading the variable documentation. Always confirm a variable's wording, respondent (youth vs. parent), sessions collected, and data-consideration flags in DEAP or the [ABCD docs](https://docs.abcdstudy.org/latest/). The search tool works on the **data dictionary only**. Never paste ABCD participant data into any chatbot or AI tool, because the DUC prohibits it.
```

## 2. Building analysis datasets

### NBDCtools (R, official)

[NBDCtools](https://software.nbdc-datahub.org/NBDCtools/) (DAIRC) builds an analysis-ready data frame from the **locally downloaded tabulated release** (`rawdata/phenotype/`), given a list of variables and/or tables. It handles joining, labels, missing codes, and event filtering.

```r
install.packages("NBDCtools")
# metadata package (data dictionary + levels), updated each release:
install.packages("NBDCtoolsData", repos = "https://nbdc-datahub.r-universe.dev")
```

Key functions:

| Task | Functions |
|---|---|
| Build a dataset | `create_dataset()`, `create_dataset_abcd()` |
| Join / read tables | `join_tabulated()`, `read_dsv_formatted()` |
| Missing codes → NA | `transf_value_to_na()` |
| Labels / factors | `transf_factor()`, `transf_label()`, `transf_value_to_label()` |
| Filter sessions/rows | `filter_events_abcd()`, `filter_id_events()`, `filter_empty_rows()`, `filter_empty_cols()` |
| Missingness ("shadow") matrices | `shadow_bind_data()`, `shadow_replace_binding_missing()` |
| Metadata | `get_dd()`, `get_levels()`, `get_sessions()`, `get_releases()` |
| Old ↔ new variable names | `convert_names_data()`, `convert_names_file()` |

Vignettes: [Get started](https://software.nbdc-datahub.org/NBDCtools/articles/NBDCtools.html) · [Joining](https://software.nbdc-datahub.org/NBDCtools/articles/join.html) · [Transformations](https://software.nbdc-datahub.org/NBDCtools/articles/transformation.html) · [Filtering](https://software.nbdc-datahub.org/NBDCtools/articles/filter.html) · [Metadata](https://software.nbdc-datahub.org/NBDCtools/articles/metadata.html) · [Shadow matrices](https://software.nbdc-datahub.org/NBDCtools/articles/shadow.html)

```{tip}
ABCD tables are **long** (one row per participant × session). NBDCtools doesn't reshape to wide, so use `tidyr::pivot_wider()` if you need wide format. Many models (mixed models, GAMMs) want long data anyway.
```

### nbdctools (Python, official)

[nbdctools](https://software.nbdc-datahub.org/nbdctools-py) is the Python counterpart (requires Python ≥ 3.11).

```bash
pip install nbdctools
```

- `create_dataset_py()`: pure-Python dataset builder.
- `create_dataset()`: wraps the R package via `rpy2` (requires R + NBDCtools installed).
- `download_metadata()` / `load_metadata()`: load the data dictionary and levels as Polars DataFrames.

[GitHub](https://github.com/nbdc-datahub/nbdctools-py)

### Reading Parquet directly

```{code-block} r
# R
library(arrow)
df <- read_parquet("rawdata/phenotype/<table>.parquet")
```

```{code-block} python
# Python
import polars as pl            # or: import pandas as pd; pd.read_parquet(...)
df = pl.read_parquet("rawdata/phenotype/<table>.parquet")
```

## 3. Computing summary scores

### ABCDscores (R, official)

[ABCDscores](https://software.nbdc-datahub.org/ABCDscores/) reproduces the official non-proprietary summary scores (release 6.0+), and lets you change the missingness threshold (default ≈ 80% item completion) or compute alternative scores. Its major version tracks the data release (7.x for release 7).

```r
install.packages("ABCDscores")
# pin a version to match your release, e.g.:
# remotes::install_github("nbdc-datahub/ABCDscores@v6.0.0")
```

Functions are named `compute_<domain>_<respondent>_<instrument>__<subscale>_<stat>()` (e.g., `compute_mh_p_ders__attun_mean()`), with `compute_<prefix>_all()` helpers per instrument. Preprint: [bioRxiv 2025.09.04.674066](https://www.biorxiv.org/content/10.1101/2025.09.04.674066).

## 4. Analysis in DEAP

Since May 2026, [DEAP](https://abcd.deapscience.com) includes:

- **Explorations:** interactive plots of any variable, with PNG export.
- **Analyses:** server-side linear mixed models and GAMMs powered by **FEMA**, on tabulated variables *or* imaging outcomes (ROI, vertexwise, voxelwise, connectome), with family and subject random effects by default, optional genetic relatedness and PCs, splines and transforms, and built-in brain viewers.

Docs: [FEMA in DEAP](https://docs.deapscience.com/analyses/fema.html) · [Model specification](https://docs.deapscience.com/analyses/model-specification.html) · [Splines](https://docs.deapscience.com/analyses/splines.html) · [Brain viewers](https://docs.deapscience.com/analyses/brain-viewers.html) · [What's new](https://docs.deapscience.com/info/updates.html)

DEAP is great for exploration and quick checks. For publications, make sure you can document and reproduce every modeling choice.

## 5. Modeling and analysis packages

ABCD's design creates dependencies you need to model: **siblings/twins within families**, **families within sites**, **repeated measures within participants**, and **scanner** differences for imaging. See [Best-practice guides](best-practices.md) for the reasoning.

| Need | R | Python / other |
|---|---|---|
| Mixed models (family, site, subject nesting) | [`lme4`](https://cran.r-project.org/package=lme4), [`glmmTMB`](https://cran.r-project.org/package=glmmTMB) | `statsmodels` MixedLM |
| Nonlinear age trajectories | [`gamm4`](https://cran.r-project.org/package=gamm4), [`mgcv`](https://cran.r-project.org/package=mgcv) | — |
| Whole-brain mixed models with family structure | — | [FEMA / cmig_tools](https://github.com/cmig-research-group/cmig_tools) (MATLAB; [ABCD docs](https://docs.abcdstudy.org/latest/tools/cmig_pipeline.html)) |
| Survey/population weights | [`survey`](https://cran.r-project.org/package=survey) | — |
| Site/scanner harmonization (ComBat) | [`longCombat`](https://github.com/jcbeer/longCombat) | [`neuroHarmonize`](https://github.com/rpomponio/neuroHarmonize) |
| Missing data | [`mice`](https://cran.r-project.org/package=mice), [`naniar`](https://cran.r-project.org/package=naniar) | — |
| SEM / longitudinal SEM | [`lavaan`](https://lavaan.ugent.be/) | `semopy` |
| Brain plots | [`ggseg`](https://ggsegverse.github.io/ggseg/) | [`nilearn`](https://nilearn.github.io) |

See also this site's [Visualization tips](../visualization.md).

## 6. Imaging pipelines

| Tool | What it is | Status |
|---|---|---|
| [ABCC (ABCD-BIDS Community Collection)](https://docs.abcdstudy.org/latest/documentation/imaging/abcc_start_page.html) | Processed derivatives (fMRIPrep, XCP-D, QSIPrep/QSIRecon) distributed in the official release | Active (v4.0.0) |
| [DAIRC MMPS pipeline](https://docs.abcdstudy.org/latest/tools/cmig_pipeline.html) | Source of the tabulated imaging measures; Hagler et al. 2019 | Active |
| [abcd-hcp-pipeline](https://github.com/DCAN-Labs/abcd-hcp-pipeline) | DCAN fMRI BIDS app (Docker) | Active; derivatives no longer in ABCC as of 7.0 |
| [abcd-dicom2bids](https://github.com/DCAN-Labs/abcd-dicom2bids) | DICOM → BIDS conversion | Built for NDA era. Raw BIDS is now provided directly |

## 7. Training & learning resources

- **ABCD-ReproNim**: free course on reproducible ABCD analysis. [Website](https://www.abcd-repronim.org/) · [Videos](https://www.youtube.com/playlist?list=PLU6a0ES56Gvgdg9eoI-Vqtr_nKOH85Ufr) · [Exercises (GitHub)](https://github.com/ABCD-ReproNim) · [Neurostars forum](https://neurostars.org/c/abcd-repronim/232) · [2027 Hackathon](https://abcd-repronim.github.io/ABCDReproNim-Hackathon-2027)
- **DEAP video tutorial** (DAIRC, ~55 min): [youtube.com/watch?v=8vtRpUHxxWU](https://www.youtube.com/watch?v=8vtRpUHxxWU), the walkthrough embedded in the official DEAP docs
- **Official docs & vignettes**: [ABCD docs](https://docs.abcdstudy.org/latest/), [DEAP docs](https://docs.deapscience.com), NBDCtools/ABCDscores vignettes (above)
- **ABCD Study GitHub**: [github.com/ABCD-STUDY](https://github.com/ABCD-STUDY)
- **More community tools, tutorials, and talks**, sorted by which data release they work with: [ABCD tools & resources](../resources/abcd-specific.md)
- **Neurostars** [`abcd` tag](https://neurostars.org/tag/abcd/126): Q&A, mostly imaging. Older threads are NDA-era
- **Help**: [NBDC Help Center](https://nbdc-datashare.lassoinformatics.com/help-center) (requires DUC), nbdc@mail.nih.gov, and our [Discussion Board](https://github.com/now-i-know-my-abcd/docs/discussions)
