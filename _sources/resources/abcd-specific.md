# ABCD tools & resources

*Last reviewed: October 2026. Know of something we're missing? [Open an issue](https://github.com/now-i-know-my-abcd/docs/issues) or use our [submission form](https://forms.gle/Qck8ifmuJXmuNWhq5).*

ABCD's data structure changed completely with **Release 6.0** (new BIDS-style IDs, session names, and variable names; distribution moved from NDA to NBDC). Code and tutorials written for earlier releases often **won't run as-is** on current data. This page collects official and community resources and sorts them by which release they work with, so you can tell at a glance what's ready to use. For step-by-step guides (access, downloads, analysis, publishing), see [Working with ABCD data](../abcd-data/overview.md).

## Official hubs at a glance

| Resource | Use it for |
|---|---|
| [ABCD documentation](https://docs.abcdstudy.org/latest/) | Variables, releases, imaging. This is the source of truth |
| [NBDC Data Hub](https://www.nbdc-datahub.org/) · [Data Access Platform](https://nbdc-datashare.lassoinformatics.com/) · [platform guides](https://nbdc.lassoinformatics.com/) | Access (DUCs), downloads, Sandbox |
| [DEAP](https://abcd.deapscience.com/#/home) ([docs](https://docs.deapscience.com)) | Data dictionary, dataset builder, in-browser analyses |
| [Official software packages](https://docs.abcdstudy.org/latest/tools/packages.html) | NBDCtools, NBDCtoolsData, ABCDscores (R), nbdctools (Python). See [Working with the data](../abcd-data/working-with-data.md) |
| [Release notes](https://docs.abcdstudy.org/latest/documentation/release_notes/index.html) | What's in (and wrong with) each release |
| [ABCD publications](https://abcdstudy.org/publications/) | Official list of ABCD-related papers. Also see our [News](../news.md) page |
| [ABCD Study GitHub](https://github.com/ABCD-STUDY) · [NBDC GitHub](https://github.com/nbdc-datahub) | Official code (ABCD-STUDY is mostly legacy, and current work lives in nbdc-datahub) |

## How releases are tagged

| Badge | Meaning |
|---|---|
| {bdg-success}`7.0` | Built or updated for the current release (7.0) |
| {bdg-info}`any release` | Methods, concepts, or tools that don't depend on ABCD's data structure |
| {bdg-primary}`6.x` | Built for the NBDC era (6.0/6.1). Usually works on 7.0, but check variable names |
| {bdg-secondary}`≤ 5.1` | NDA era. Access steps and variable names are outdated, but the ideas may still help |

```{tip}
Porting old code? `NBDCtools::convert_names_data()` and `convert_names_file()` translate pre-6.0 variable names to the new scheme, and the data dictionary lists each variable's old name. See [Accessing the data](../abcd-data/accessing-data.md) for the new ID and session conventions.
```

The official packages are all maintained for 7.0, and **ABCDscores' version number matches the data release** (7.x ↔ release 7).

## {bdg-success}`7.0` Ready for the current release

| Resource | Type | What it does | Maintainer |
|---|---|---|---|
| [abcd_ksads](https://github.com/eugiampetruzzi/abcd_ksads) | Python | Cleans and harmonizes KSADS-COMP psychiatric diagnoses: missingness codes, administration calendar, 230 diagnosis variables mapped to DSM categories, instrument-version tracking. Tested, with CI. Companion preprint: Giampetruzzi et al. (2026), [Harmonized psychiatric diagnosis data from the ABCD Study](https://doi.org/10.21203/rs.3.rs-10083024/v1) (preprint) | E. Giampetruzzi / R. Poldrack |
| [ABCD-ReproSchema](https://github.com/ReproNim/ABCD-ReproSchema) | R + Python | The ABCD data dictionary converted to ReproSchema JSON-LD, tagged per release (6.0, 6.1, 7.0). Useful for machine-readable instrument metadata | ReproNim |
| [ABCD Data Dictionary Semantic Search](https://beepboopstats.com/abcd-dictionary) | Web app | Plain-language variable search over the 6.0 and 7.0 dictionaries | B. Das |
| [7.0 release notes](https://docs.abcdstudy.org/latest/documentation/release_notes/7_0.html) and [docs changelog](https://docs.abcdstudy.org/latest/info/changelog.html) | Official docs | What changed in 7.0 and in point releases (7.0.x). This is the closest thing to a known-issues list | DAIRC |
| [Genetics (WGS) domain docs](https://docs.abcdstudy.org/latest/documentation/non_imaging/gn.html) | Official docs | Whole-genome sequencing, new in 7.0 (~8,700 participants) | DAIRC |
| [Linked External Data (LE) domain docs](https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html) | Official docs | Every geocoded source in one place (ADI, COI 2.0, SVI, air pollution, NLCD, Opportunity Atlas, state policies), plus 7.0 fixes | DAIRC |
| [Novel Technologies (Fitbit) domain docs](https://docs.abcdstudy.org/latest/documentation/non_imaging/nt.html) | Official docs | How Fitbit heart-rate, sleep, and activity measures are derived, with documented accuracy caveats | DAIRC |
| [Substudies docs](https://docs.abcdstudy.org/latest/documentation/substudies/baby_teeth.html) | Official docs | Lesser-known substudy datasets (Baby Teeth metals, COVID-19, Endocannabinoid, MR Spectroscopy, RECOVER, Social Development, …) | DAIRC |
| [CloudPipe](https://github.com/jrussell9000/cloudpipe) | Python (AWS) | *New (Sept 2026).* Reference cloud pipeline from minimally processed sMRI/fMRI to MNI-space BOLD, confounds, and FastSurfer outputs. Meant to be adapted, not run as-is | J. Russell |
| [abcd_extract_eprime](https://github.com/ABCD-STUDY/abcd_extract_eprime) | MATLAB | Official scripts that extract task timing and behavior (MID, SST, n-back, REC) from E-Prime files. Minimal documentation | ABCD-STUDY (DAIC) |

### 7.0 known issues worth knowing about

Summarized from the [7.0 release notes](https://docs.abcdstudy.org/latest/documentation/release_notes/7_0.html) and the [docs changelog](https://docs.abcdstudy.org/latest/info/changelog.html) (through docs 7.0.4, October 2026). **Always check the official pages for updates.**

- **Coverage:** 11,860 participants across 16 events. Data are complete through the 5-year follow-up and nearly complete for year 6. The 7-year and 7.5-year (`ses-07M`) data are **partial**.
- **Siemens XA30 sessions (889):** T1w, T2w, and fieldmaps are missing from BIDS `sourcedata`/`rawdata`. Derivatives and tabulated imaging data are not affected.
- **Concatenated voxelwise imaging:** an outdated registration target for atlas channel 11 left out cerebellar grey matter.
- **RECOVER COVID-symptom tables** (`recover_p_ps`, `recover_p_pscg`): 346 variables are misnamed. The release notes give a rename mapping, and a fix is planned for 7.1.
- **`fc_y_ev__edu_002__v01`** has a mislabeled response level (school type).
- **Documentation-only notes added in 7.0.3–7.0.4:** hair-style bias in hair toxicology, a Pubertal Development Scale scoring correction, a body-size caveat for dMRI, `mh_y_resil` and Emotional Stroop randomization issues.

```{warning}
**Still on 6.0/6.1? These were fixed in 7.0:** hair toxicology was coded 1/2 instead of 0/1, the Fitbit `qc_300min` sleep flag used > 299 instead of ≥ 300, and three ozone variables in `le_l_lo3` were mis-mapped. Re-check any results that use these variables.
```

Found a data problem? Report it through the [ABCD issue-reporting page](https://docs.abcdstudy.org/latest/info/issues.html) (NBDC Help Center ticket). There's no public known-issues tracker.

```{note}
As of October 2026 we couldn't find any **7.0-specific training** (webinar, walkthrough, or office hours). The NBDC 7.0 pages point to the written docs, and the platform and DEAP are unchanged from 6.x, so the 6.x tutorials below still apply. Questions go to nbdc@mail.nih.gov or our [Discussion Board](https://github.com/now-i-know-my-abcd/docs/discussions).
```

## {bdg-info}`any release` Release-agnostic

### Training & talks

| Resource | Type | What it covers |
|---|---|---|
| [2025 ABCD Insights & Innovations Meeting, Collaborative Learning Workshops](https://abcdstudy.org/r1wj) ([Day 1](https://videocast.nih.gov/watch=56949) · [Day 2](https://videocast.nih.gov/watch=56956) · [timestamped agenda](https://abcdstudy.org/wp-content/uploads/2026/01/Agenda-AIIM25-Workshops-Times.pdf)) | NIH VideoCast | Imaging, biostatistics, linked external data, and Responsible Use of Data workshops, plus Q&A with ABCD investigators. Day 1 at 52:20 is an NBDC/DEAP demo {bdg-primary}`6.x`, and Day 2 at 45:00 is NBDC/DEAP Q&A |
| [ABCD-ReproNim](https://www.abcd-repronim.org/) ([materials](https://www.abcd-repronim.org/materials.html) · [videos](https://www.youtube.com/playlist?list=PLU6a0ES56Gvgdg9eoI-Vqtr_nKOH85Ufr) · [exercises](https://github.com/ABCD-ReproNim) · [Neurostars forum](https://neurostars.org/c/abcd-repronim/232)) | Course | Reproducible, responsible ABCD analysis: lectures, data exercises, and Q&A. Companion paper: Laird et al. (2026), [*DCN*](https://doi.org/10.1016/j.dcn.2026.101755). Older modules use NDA-era data. **Next: [ABCD-ReproNim Hackathon](https://abcd-repronim.github.io/ABCDReproNim-Hackathon-2027), April 5–9, 2027** |
| ABCD Workshops: [2021 Modeling Developmental Change](https://abcdworkshop.github.io/) ([slides, talks, code](https://abcdworkshop.github.io/resources/)) · [2019 Brain Development and Mental Health](https://abcdworkshop.github.io/past-workshops/2019/) ([slides, talks, code](https://abcdworkshop.github.io/past-workshops/2019/resources/)) | Recorded talks, slides, code tutorials | Reproducible science, longitudinal modeling, puberty, and adolescent mental health. The methods teaching is excellent, but **code and data-access steps are NDA-era** {bdg-secondary}`≤ 5.1`. Attendees of the 2021 workshop wrote the [Saragosa-Harris et al. (2022) practical guide](https://doi.org/10.1016/j.dcn.2022.101115) ([PDF](https://github.com/now-i-know-my-abcd/docs/files/9310731/PracticalGuide.pdf)). Supported by NIH R25MH125545 |
| [ABCD public science webinars](https://abcdstudy.org/infographics/) | Recorded talks | Findings on obesity, substance use, COVID-19, sleep, and screen use, from ABCD investigators. Good background |
| ["Mind the Kids: Lessons from the ABCD data revolution"](https://acamhlearn.org/learning/mind-the-kids--lessons-from-the-abcd-data-revolution/1b7cfa71-b1d0-4358-b9e0-fd76cdeadc69) | Podcast (ACAMH, 2026; free account) | Adriene Beltz on measuring puberty in ABCD |
| [r-stats-workshop](https://beepboopstats.com/r-stats-workshop) | Quarto course | Four-module R and statistics course using synthetic ABCD-shaped longitudinal data |

### Code & tools

| Resource | Type | What it does |
|---|---|---|
| [metasnf](https://branchlab.github.io/metasnf/) | R (CRAN) | Subtyping with meta-clustering and similarity network fusion, designed around ABCD-style multimodal data |
| [ggsegAtlasTrack](https://ggsegverse.github.io/ggsegAtlasTrack/) | R | The AtlasTrack white-matter atlas (used for ABCD DTI) for `ggseg` plots |
| [ggAtlasTrack](https://github.com/hbyrne07/ggAtlasTrack) | R | Plots AtlasTrack tract statistics, with helpers for ABCD 5.0 and 6.0+ variable names {bdg-primary}`6.x` |
| [BrainSwipes](https://brainswipes.us) | Web app | Crowdsourced visual MRI QC, used for ABCC |
| [abcd-bids-tfmri-pipeline](https://github.com/DCAN-Labs/abcd-bids-tfmri-pipeline) | Python | Task-fMRI level-1/level-2 GLMs on CIFTI dense time series (abcd-hcp-pipeline outputs) |

### Methods papers for specific domains

These complement the [Best-practice guides](../abcd-data/best-practices.md). Many describe measures from earlier waves, but the measurement issues they raise still apply.

| Paper | Why read it |
|---|---|
| Fan, C. C., et al. (2021). ABCD Linked External Data (LED): Protocol and practices for geocoding and assignment of environmental data. *DCN*. [doi:10.1016/j.dcn.2021.101030](https://doi.org/10.1016/j.dcn.2021.101030) | Founding methods paper for the geocoded data |
| Abad, S., et al. (2024). Lifetime residential history collection and processing for environmental data linkages in the ABCD study. *Health & Place*. [doi:10.1016/j.healthplace.2024.103238](https://doi.org/10.1016/j.healthplace.2024.103238) | How multi-address exposure variables are built |
| Barch, D. M., et al. (2021). Demographic and mental health assessments in the ABCD study: Updates and age-related trajectories. *DCN*. [doi:10.1016/j.dcn.2021.101031](https://doi.org/10.1016/j.dcn.2021.101031) | Measure-by-measure mental health protocol |
| Gonzalez, R., et al. (2021). An update on the assessment of culture and environment in the ABCD Study. *DCN*. [doi:10.1016/j.dcn.2021.101021](https://doi.org/10.1016/j.dcn.2021.101021) | Culture and environment measures |
| Sullivan, R. M., et al. (2026). Substance use patterns from late childhood to mid-adolescence: Updates on the ABCD Study. *Drug & Alcohol Dependence Reports*. [doi:10.1016/j.dadr.2026.100463](https://doi.org/10.1016/j.dadr.2026.100463) | Most recent substance-use descriptive update |
| Wade, N. E., et al. (2024). Cannabis use and neurocognitive performance at 13–14 years-old: Optimizing assessment with hair toxicology in the ABCD Study. *Addictive Behaviors*. [doi:10.1016/j.addbeh.2023.107930](https://doi.org/10.1016/j.addbeh.2023.107930) | Self-report vs. hair toxicology |
| Anokhin, A. P., et al. (2022). Age-related changes and longitudinal stability of individual differences in ABCD Neurocognition measures. *DCN*. [doi:10.1016/j.dcn.2022.101078](https://doi.org/10.1016/j.dcn.2022.101078) | Reliability/stability of cognitive measures |
| Bagot, K. S., et al. (2022). Youth screen use in the ABCD study. *DCN*. [doi:10.1016/j.dcn.2022.101150](https://doi.org/10.1016/j.dcn.2022.101150) | Screen-use measures and how they changed across waves |
| Zhao, et al. (2025). Examining measurement discrepancies in adolescent screen media activity with insights from the ABCD study. *npj Mental Health Research*. [doi:10.1038/s44184-025-00131-z](https://doi.org/10.1038/s44184-025-00131-z) | Youth vs. parent screen-time reports |
| Feldman, et al. (2026). Who's counting? Discrepancies between caregiver-reported, youth-reported, and Fitbit sleep in the ABCD study. [doi:10.1007/s44470-026-00042-6](https://doi.org/10.1007/s44470-026-00042-6) | Choosing among sleep measures |
| Harris, et al. (2025). The Childhood Opportunity Index 2.0: Factor structure in 9–10 year olds in the ABCD Study. *IJERPH*. [doi:10.3390/ijerph22020228](https://doi.org/10.3390/ijerph22020228) | Check before using COI as one composite |
| Fan, C. C., et al. (2023). Genotype data and derived genetic instruments of ABCD Study for better understanding of human brain development. *Behavior Genetics*. [doi:10.1007/s10519-023-10143-0](https://doi.org/10.1007/s10519-023-10143-0) | Genotyping array QC and ancestry (pre-WGS) |
| Elyounssi, S., et al. (2025). Addressing artifactual bias in large, automated MRI analyses of brain development. *Nature Neuroscience*. [doi:10.1038/s41593-025-01990-7](https://doi.org/10.1038/s41593-025-01990-7) | How MRI quality biases automated structural results, and fixes |
| Cetin-Karayumak, S., et al. (2024). Harmonized diffusion MRI data and white matter measures from the ABCD Study. *Scientific Data*. [doi:10.1038/s41597-024-03058-w](https://doi.org/10.1038/s41597-024-03058-w) | Scanner-harmonized dMRI derivatives (originally distributed via NDA) |
| Van den Akker, O. R., et al. (2021). Preregistration of secondary data analysis: A template and tutorial. *Meta-Psychology*. [doi:10.15626/MP.2020.2625](https://doi.org/10.15626/MP.2020.2625) | The tutorial behind the OSF secondary-data preregistration template |

## {bdg-primary}`6.x` NBDC era (6.0 / 6.1)

These were built on the current platform and data structure. Most work on 7.0, but verify variable names.

| Resource | Type | What it does |
|---|---|---|
| [DEAP tutorial (DAIRC, 2025)](https://www.youtube.com/watch?v=8vtRpUHxxWU) | Video (~55 min, chapters) | Full DEAP walkthrough: data dictionary, building/saving datasets, name mapping, downloads. **This is the video the official DEAP docs now embed** |
| [DEAP quick guide (PDF)](https://docs.deapscience.com/assets/files/09_2025_deap_brochure.pdf) | Handout | Step-by-step dataset creation and download |
| ["Tutorial on the new DEAP"](https://www.youtube.com/watch?v=ccqzFr_T2rA) | Video | Shorter DEAP overview from the 6.0 launch |
| [lasso-project-template](https://github.com/ajbarrows/lasso-project-template) | Shell/R template | Minimal reproducible R project for the NBDC Sandbox |
| [abcc_automated_QC](https://github.com/DCAN-Labs/abcc_automated_QC) | Python | Automated structural/functional QC for ABCC derivatives (outlier detection, connectivity pass flags) |
| [abcd-abcc_motion_reg_generator](https://github.com/nbdc-datahub/abcd-abcc_motion_reg_generator) | Python BIDS app | Extracts and repairs motion regressors from ABCC derivatives |
| [abcd-abcc_concat_filtered_dtseries_generator](https://github.com/nbdc-datahub/abcd-abcc_concat_filtered_dtseries_generator) | Python BIDS app | Builds concatenated, filtered task (n-back) dense time series from ABCC |
| [abcd-rsfmri-training-code](https://github.com/DCAN-Labs/abcd-rsfmri-training-code) | R/Python tutorial | Loading ABCD 6.0 resting-state derivatives for analysis |
| [ABCDWrangler](https://github.com/62442katieb/ABCDWrangler) | Python | Variable lookup, long↔wide reshaping, MRI QC filters. *README says it's still being adapted to 6.0* |
| ["ABCD Study omits gender-identity data from latest release"](https://www.thetransmitter.org/gender/abcd-study-omits-gender-identity-data-from-latest-release/) | News (*The Transmitter*, 2025) | Why gender-identity variables are missing from 6.0+, a common newcomer question |

````{dropdown} ≤ 5.1: NDA-era resources (click to expand)
These were written for releases distributed through the NIMH Data Archive. **Access instructions and variable names are outdated.** They're listed because the methods or concepts can still be useful.

| Resource | Type | Why it's still useful |
|---|---|---|
| [pelham-weighting-resources](https://github.com/ABCD-STUDY/pelham-weighting-resources) | R workshop materials (release 4.0) | Concepts for population and attrition weighting |
| [abcd_acs_raked_propensity](https://github.com/ABCD-STUDY/abcd_acs_raked_propensity) | R | How the ACS-raked propensity weights were computed |
| [abcc_datapre](https://github.com/demidenm/abcc_datapre) | Python | E-Prime → BIDS events with scanner-timing QC; logic still applies |
| [Cleaning-ABCD-hormone-data](https://github.com/marjolein15/Cleaning-ABCD-hormone-data) | R | Salivary hormone cleaning following the Herting (2021) decision tree |
| [LED social/environmental context code (OSF)](https://osf.io/nmdtg/) | Code + data | Source code and US-wide source data behind neighborhood measures |
| [NeuroHackademy 2021: ABCD-BIDS Community Collection](https://www.youtube.com/watch?v=w3SSSCMF5Pg) | Video | ABCC concepts and BIDS layout (access steps are outdated) |
| [NIDA: Identifying Research Gaps & Opportunities with ABCD Study Data (2021)](https://nida.nih.gov/videos/identifying-research-gaps-opportunities-abcd-study-data) | Video + transcript | Prevention-science topics: trauma, self-regulation, substance-use initiation |
| [analysis-nda](https://github.com/ABCD-STUDY/analysis-nda) | R | *Historical.* Old NDA merge scripts, superseded by NBDCtools |
| [fitbit-pipeline](https://github.com/ABCD-STUDY/fitbit-pipeline) | Python | *Superseded.* Fitbit scoring now lives in ABCDscores |

**Archived NDA access and download tools.** These don't work for 6.0+, which is only on NBDC.

- [NDA cloud access training](https://nda.nih.gov/training/modules/cloud.html)
- [nda-tools](https://github.com/NDAR/nda-tools)
- [nda-abcd-s3-downloader](https://github.com/DCAN-Labs/nda-abcd-s3-downloader)
- [NDA Collection 3165 docs (ABCC 1.0–2.0)](https://nda-abcd-collection-3165.readthedocs.io). ABCC is now part of the official release; see the [ABCC start page](https://docs.abcdstudy.org/latest/documentation/imaging/abcc_start_page.html)
````

## See also

- [Best-practice guides](../abcd-data/best-practices.md): peer-reviewed practical guides, including responsible use (Simmons et al., 2021) and the [official responsible-use guidance](https://docs.abcdstudy.org/latest/usage/responsible_use.html)
- [Methods & open-science toolkit](methods-toolkit.md): preregistration, reproducible workflows, covariates, nesting, longitudinal models, effect sizes, and machine learning
