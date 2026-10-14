# Downloading the data

*Last reviewed: October 2026 (ABCD Release 7.0). Official sources: [ABCD docs: Access](https://docs.abcdstudy.org/latest/usage/access.html), [DEAP: My datasets](https://docs.deapscience.com/datasets/my_datasets.html), [NBDC resource hub](https://nbdc.lassoinformatics.com/).*

There are several ways to get ABCD data onto your machine, and which one is best depends on what you need. All of them require an approved DUC (see [Getting access](getting-access.md)), and all downloaded data must live on a NIST 800-171–compliant system and be deleted when your project ends or your DUC expires.

## Which route should I use?

| I want… | Use | Format | Notes |
|---|---|---|---|
| A handful of tabulated variables for one analysis | **DEAP custom dataset** | Parquet (recommended), CSV, TSV, RDS, Arrow, Stata, SPSS | Up to 10,000 variables; choose values vs. labels and missing codes vs. NA |
| A ready-made bundle of common tables | **DEAP pre-assembled datasets** | Parquet, CSV, TSV, RDS, Arrow | Compressed size shown; expect ≥ 5× when uncompressed |
| Whole instruments / tables as a CSV | **NBDC Query Wizard** | CSV (+ optional missingness reasons file) | [Guide](https://nbdc.lassoinformatics.com/query-wizard) |
| Specific item-level variables found by searching the dictionary | **NBDC Data Dictionary Query** | CSV | [Guide](https://nbdc.lassoinformatics.com/dictionary-query-tool) |
| The **full tabulated release**, to build datasets locally with NBDCtools | **Globus** (`rawdata/phenotype/`) | TSV + Parquet + JSON sidecars | Best for reproducible pipelines |
| Imaging (raw NIfTI, DICOM, FreeSurfer, ABCC), EEG, wearables, genetics, EARS/Fitbit | **All Study Data Search & Filter** → **Globus** | BIDS | [Guide](https://nbdc.lassoinformatics.com/all-study-data) |
| An older release (6.0, 6.1) | **Previous Releases** → Globus | as released | [Guide](https://nbdc.lassoinformatics.com/download-previous-release); one transfer at a time |
| Not to download at all | **NBDC Sandbox** | — | See [Accessing the data](accessing-data.md) |

## Route 1: DEAP (tabulated data, quickest start)

1. Log in to [DEAP](https://abcd.deapscience.com) with your NBDC credentials.
2. Find variables in the **Data Dictionary** (or with the [semantic search tool](working-with-data.md)).
3. Add them to a **custom dataset**, or pick a **pre-assembled dataset**.
4. Under **My datasets**, choose the format and options:
   - **Format:** Parquet keeps column types and labels and is much smaller than CSV.
   - **Values vs. labels:** labels are human-readable; values are easier to model. You can always map one to the other with the levels table.
   - **Missing codes vs. NA:** keeping the codes tells you *why* something is missing (e.g., "don't know" vs. "refused"). Converting to NA is simpler for analysis.
5. Each download includes `data_dictionary_levels.xlsx`. **Keep it with your data.**

Docs: [Data dictionary](https://docs.deapscience.com/datasets/data_dictionary.html) · [Create a dataset](https://docs.deapscience.com/datasets/create_dataset.html) · [My datasets](https://docs.deapscience.com/datasets/my_datasets.html) · [Video tutorial (DAIRC, 2025)](https://www.youtube.com/watch?v=8vtRpUHxxWU) · [shorter overview](https://www.youtube.com/watch?v=ccqzFr_T2rA)

## Route 2: NBDC Data Access Platform (Query tools)

On the [Data Access Platform](https://nbdc-datashare.lassoinformatics.com/):

- **Query Wizard** returns whole instruments as a single CSV, optionally with a file explaining reasons for missingness.
- **Data Dictionary Query** returns specific item-level variables found by searching the dictionary.

These work well for quick pulls when you don't need Parquet.

## Route 3: Globus (bulk, imaging, and file-based data)

All large downloads go through [Globus](https://www.globus.org/).

1. **Set up an endpoint.**
   - *Preferred:* your institution's **Globus Connect Server** (ask research computing). This usually points at a cluster that already meets your security requirements.
   - *Otherwise:* **Globus Connect Personal** on an approved machine. Do **not** tick "High Assurance" during setup ([NBDC Globus guide](https://nbdc.lassoinformatics.com/globus-share)).
2. **Select data.**
   - For the full tabulated release, browse to `rawdata/phenotype/`.
   - For file-based data, use **All Study Data Search & Filter** ([data wrangler](https://nbdc-datashare.lassoinformatics.com/data-wrangler)) to filter by participant, session, modality, etc., then click **Trigger Transfer**.
   - Or browse directly in the Globus web app under **Shared With You → "NBDC Datashare ABCD Release"**.
3. **Download only what you need.** Globus filter rules let you include/exclude by filename pattern (e.g., only `*_T1w.nii.gz`, or only certain sessions). Imaging data are very large.
4. Globus verifies file integrity (checksums) during transfer by default, and failed transfers can be resumed.

```{tip}
For imaging, check the [ABCC start page](https://docs.abcdstudy.org/latest/documentation/imaging/abcc_start_page.html) and the per-scan QC in `scans.tsv` **before** downloading. You may not need raw data at all if the tabulated imaging summaries (in DEAP) or ABCC derivatives cover your question.
```

## Practical tips

- **Use Parquet.** It preserves types and labels, loads fast, and is much smaller. Read it in R with `arrow` or `nanoparquet`, or in Python with `pandas`, `polars`, or `pyarrow`.
- **Record exactly what you downloaded:** release number, DOI, date, route, and the variable list. Save the DEAP dataset definition or your Globus filter rules in your project repo (they contain no participant data).
- **Don't download into synced folders** (Box, Dropbox, OneDrive, Google Drive, iCloud) unless your institution has approved them for controlled-access data. Also make sure data folders are in your `.gitignore` so they're never pushed to GitHub.
- **Plan for deletion.** Keep all ABCD data under one directory so it's easy to delete at the end of the project/DUC.
- **Patch releases** (e.g., 6.0 → 6.1) can change data. Re-download when you deliberately move releases, not mid-analysis.

## Archived routes (NDA era)

These applied to release 5.1 and earlier through the NIMH Data Archive. **None of them distribute 6.0+ data.**

- NDA data packages and [nda-tools](https://github.com/NDAR/nda-tools)
- [NDA cloud access training](https://nda.nih.gov/training/modules/cloud.html)
- [nda-abcd-s3-downloader](https://github.com/DCAN-Labs/nda-abcd-s3-downloader) for ABCC / NDA Collection 3165 ([archived docs](https://nda-abcd-collection-3165.readthedocs.io))
- [NDA ABCD query & download tutorial](https://nda.nih.gov/tutorials/abcd/query_and_download.html)
