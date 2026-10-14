# Accessing the data: what's where

*Last reviewed: October 2026 (ABCD Release 7.0). Official sources: [ABCD docs: Access](https://docs.abcdstudy.org/latest/usage/access.html), [Data structure](https://docs.abcdstudy.org/latest/documentation/curation/structure.html), [NBDC resource hub](https://nbdc.lassoinformatics.com/).*

Once your DUC is approved, ABCD data can be reached through a few different platforms. This page explains what each one is and what data it holds. For the mechanics of actually getting files onto your machine, see [Downloading the data](downloading-data.md).

## Releases

| Release | Released | Latest visit included | DOI | Where |
|---|---|---|---|---|
| **7.0** (current) | May 2026 | ses-07M (7.5-year) | [10.82525/8f3w-5260](https://doi.org/10.82525/8f3w-5260) | NBDC |
| 6.1 | Dec 2025 | ses-06A | [10.82525/ab4q-qr87](https://doi.org/10.82525/ab4q-qr87) | NBDC (Previous Releases) |
| 6.0 | Jun 2025 | ses-06A | [10.82525/jy7n-g441](https://doi.org/10.82525/jy7n-g441) | NBDC (Previous Releases) |
| 5.1 and earlier | Nov 2023 | ses-04A | [5.1.1: 10.82525/wjkw-bp63](https://doi.org/10.82525/wjkw-bp63) | NDA (legacy DUCs only) |

Sources: [release notes index](https://docs.abcdstudy.org/latest/documentation/release_notes/index.html), [NBDC ABCD page](https://www.nbdc-datahub.org/abcd-study).

Release 7.0 includes 11,860 participants and adds, among other things, whole-genome sequencing data and additional linked external data. Read the [7.0 release notes](https://docs.abcdstudy.org/latest/documentation/release_notes/7_0.html) and [known issues](https://docs.abcdstudy.org/latest/documentation/imaging/index.html) before you start. For example, T1w/T2w/fieldmap scans are missing for 889 Siemens XA30 sessions in 7.0.

```{tip}
**Pick a release and stick with it** for a project. Write the release number and DOI into your project README on day one. Previous releases stay available on NBDC, so you can always reproduce your work.
```

## The platforms

| Platform | What it is | Data available | Needs DUC? |
|---|---|---|---|
| [**DEAP**](https://abcd.deapscience.com) ([docs](https://docs.deapscience.com)) | Data Exploration & Analysis Portal: data dictionary, dataset builder, interactive plots, in-browser mixed models (FEMA) | **Tabulated data** (incl. tabulated imaging summaries) | Dictionary: no. Data: yes |
| [**NBDC Data Access Platform**](https://nbdc-datashare.lassoinformatics.com/) (Lasso) | Query tools plus the file-based data browser | Tabulated **and** file-based data (MRI, EEG, wearables, genetics, EARS, Fitbit), previous releases | Yes |
| [**Globus**](https://nbdc.lassoinformatics.com/globus-share) | Transfer service used for all large/bulk downloads | Everything on the Data Access Platform | Yes |
| [**NBDC Sandbox**](https://nbdc.lassoinformatics.com/sandbox) (Lasso SAFE) | Cloud compute **without downloading**: RStudio, Jupyter, Linux desktop, Slurm | Tabulated data mounted read-only | Yes |
| [**NBDC Biobank Portal**](https://nbdc-biobank.nida.nih.gov/) | Biospecimen requests | Biospecimens | Separate request |

```{note}
DEAP has two hostnames: [abcd.deapscience.com](https://abcd.deapscience.com) (ABCD) and [nbdc.deapscience.com](https://nbdc.deapscience.com) (combined NBDC). Genetics, EARS (smartphone sensing), and Fitbit data are **not** in DEAP. Get them from the Data Access Platform/Globus.
```

### Should I download at all, or use the Sandbox?

The DUC encourages keeping data on the platform rather than downloading. The [Sandbox](https://nbdc.lassoinformatics.com/sandbox) is a good option if:

- your institution doesn't (yet) have a NIST 800-171 compliant environment,
- you only need tabulated data, or
- you want to avoid managing local copies and deleting them at the end.

At last review, Sandbox VMs ranged up to 16 cores / 128 GB RAM, with a 30 GB home directory. Tabulated data live at `/shared/release/abcd/dairc_files/rawdata/phenotype` as TSV and Parquet. Check which release the Sandbox currently mounts.

## How the data are organized (6.0+)

Release 6.0 reorganized ABCD around the **BIDS** standard, and 7.0 keeps that structure. If you learned ABCD on 5.1 or earlier, almost every name has changed.

### File tree

```
abcd/
├── rawdata/
│   ├── phenotype/            # tabulated data: <table>.tsv / .parquet + .json sidecar
│   └── sub-*/ses-*/          # NIfTI imaging, neurocognitive, wearable files
├── sourcedata/sub-*/ses-*/   # DICOMs (per-series .tgz)
├── derivatives/
│   ├── freesurfer/           # sub-<p>_ses-<e>.zip
│   ├── mmps_mproc/           # minimally processed images (DAIRC pipeline)
│   └── abcc-<pipeline>/      # ABCD-BIDS Community Collection derivatives
└── concatenated/imaging/     # correlation matrices, vertexwise & voxelwise data
```

([Data structure docs](https://docs.abcdstudy.org/latest/documentation/curation/structure.html))

### IDs and sessions

- `participant_id`: `sub-` + 8 characters (e.g., `sub-ABCD1234`)
- `session_id`: `ses-` + 3 characters

| New `session_id` | Old `eventname` (≤ 5.1) |
|---|---|
| `ses-00S` | `screener_arm_1` |
| `ses-00A` | `baseline_year_1_arm_1` |
| `ses-00M` | `6_month_follow_up_arm_1` |
| `ses-01A` | `1_year_follow_up_y_arm_1` |
| `ses-02A` … `ses-06A` | annual follow-ups (`ses-0xM` = mid-year visits) |
| `ses-07M` | 7.5-year visit (new in 7.0) |
| `ses-C01`–`ses-C07` | COVID-19 survey waves |
| `ses-S01`–`ses-S03` | Social Development (SDev) substudy waves |

See [Standards](https://docs.abcdstudy.org/latest/documentation/curation/standards.html) for the complete list.

### Tables and variables

- **Static tables** have one row per participant. **Longitudinal tables** have one row per participant × session (**long format**).
- **Variable names** follow `domain_source_table_item`, e.g. `ph_y_bp__dia__r01_001`. Common suffixes: `__v01` (changed version), `__l` (longitudinal version), `___1` (multi-select option). See [Naming conventions](https://docs.abcdstudy.org/latest/documentation/curation/naming.html).
- **Old ↔ new names:** the data dictionary lists the old (≤ 5.1) name for each variable, and `NBDCtools::convert_names_data()` / `convert_names_file()` convert between them. This is handy for porting old scripts.
- **Missing-value codes:** `222, 444, 555, 666, 777, 888, 999` are *codes*, not numbers. Convert them before analysis (e.g., `NBDCtools::transf_value_to_na()`).
- **Dates/times:** variables ending in `_dt` are dates; `_dtt` are date-times.
- **Metadata:** each table comes with a **data dictionary** (one row per variable) and a **levels** table (value labels), available in DEAP, on NBDC, and as BIDS JSON sidecars ([metadata docs](https://docs.abcdstudy.org/latest/documentation/curation/metadata.html)).

### Imaging

- **Raw BIDS** files look like `sub-<label>_ses-<label>_task-<mid|nback|sst|rest>_run-<label>_bold.nii.gz`. `scans.tsv` carries usability/QC flags ([raw data docs](https://docs.abcdstudy.org/latest/documentation/imaging/data_source_raw.html)).
- **DAIRC tabulated imaging** (ROI summaries) are in the phenotype tables, so you can get them via DEAP.
- **ABCC (ABCD-BIDS Community Collection)** is now part of the official release, distributed via NBDC (v4.0.0: fMRIPrep, XCP-D, QSIPrep/QSIRecon). ABCD-HCP pipeline derivatives are no longer produced as of 7.0; legacy outputs remain in 6.1. ABCC 1.0–2.0 lived in NDA Collection 3165, and those [docs are archived](https://nda-abcd-collection-3165.readthedocs.io). See the [ABCC start page](https://docs.abcdstudy.org/latest/documentation/imaging/abcc_start_page.html).
