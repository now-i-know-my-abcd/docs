# Working with ABCD data: start here

*Last reviewed: October 2026 (ABCD Release 7.0). Things change quickly; if you spot something out of date, please [open an issue](https://github.com/now-i-know-my-abcd/docs/issues) or post on the [Discussion Board](https://github.com/now-i-know-my-abcd/docs/discussions).*

This section walks through the full life cycle of an ABCD project. It pulls together official documentation, tools, and peer-reviewed best-practice guides, organized in the order you'll actually need them.

```{important}
This is an **unofficial**, community-maintained resource. When anything here disagrees with official documentation, the official documentation wins. The main official sources are:

- [ABCD Study documentation](https://docs.abcdstudy.org/latest/) (DAIRC). This is the source of truth for variables, releases, and imaging.
- [NIH Brain Development Cohorts (NBDC) Data Hub](https://www.nbdc-datahub.org/), which handles data access, Data Use Certifications (DUCs), and downloads.
- [abcdstudy.org for scientists](https://abcdstudy.org/scientists/data-sharing/), which carries study announcements.
```

## The big picture

Since **Release 6.0 (2025)**, ABCD data are no longer distributed through the NIMH Data Archive (NDA). Everything now lives on the **NBDC Data Hub**, which also hosts the HEALthy Brain and Child Development (HBCD) Study. The current release is **ABCD 7.0**, released May 2026, [DOI 10.82525/8f3w-5260](https://doi.org/10.82525/8f3w-5260).

| Step | What you do | Where | Page |
|---|---|---|---|
| 0. Explore | Browse variables before you have access | DEAP data dictionary, semantic search | [Working with the data](working-with-data.md) |
| 1. Get access | Submit a Data Use Certification (DUC), pass the training | NBDC Data Hub | [Getting access](getting-access.md) |
| 2. Access | Learn what data exist, which release, where each type lives | NBDC Data Hub, DEAP, Sandbox | [Accessing the data](accessing-data.md) |
| 3. Download | Tabulated data, imaging files, previous releases | DEAP, Query Wizard, Globus | [Downloading the data](downloading-data.md) |
| 4. Analyze | Build datasets, compute scores, model the data | NBDCtools, ABCDscores, DEAP, R/Python | [Working with the data](working-with-data.md) |
| 5. Disseminate | Acknowledge, cite the DOI, share code, respect privacy rules | Your paper, GitHub/OSF | [Disseminating your work](disseminating.md) |
| Throughout | Read the practical guides before you design analyses | Peer-reviewed papers | [Best-practice guides](best-practices.md) |

## New-trainee checklist

- [ ] Find out whether your PI or lab already has an **NBDC group DUC**. Trainees must be added to a PI's group DUC rather than applying on their own.
- [ ] Make sure you log in with your **institutional email**, using the same email that is on the DUC.
- [ ] Complete the **NBDC Responsible Data and Biospecimen Use Training** (90% pass on the quiz, renewed yearly).
- [ ] Confirm with your PI/IT that you'll store data on a **NIST SP 800-171–compliant** system (or plan to use the NBDC Sandbox).
- [ ] Read the [Data Use Certification](getting-access.md#key-rules-from-the-duc) rules. Notably, **no ABCD data in generative AI tools/LLMs**, and **no reported cells with fewer than 10 participants**.
- [ ] Bookmark the [ABCD documentation](https://docs.abcdstudy.org/latest/) and the [release notes](https://docs.abcdstudy.org/latest/documentation/release_notes/index.html) for your release.
- [ ] Read at least the [Saragosa-Harris et al. (2022) practical guide](best-practices.md) before designing your analysis.
- [ ] Consider [preregistering](disseminating.md#preregistration) your analysis plan **before** you look at the outcome data.

```{tableofcontents}
```
