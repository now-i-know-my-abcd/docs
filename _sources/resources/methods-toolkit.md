# Methods & open-science toolkit

*Last reviewed: October 2026. Many of these resources were originally curated by Victoria Guazzelli Williamson during the 2021 ABCD Workshop. Suggest additions via an [issue](https://github.com/now-i-know-my-abcd/docs/issues).*

General methods and open-science resources, organized by the decisions you'll face in an ABCD project. Want to code along? Jump to the {ref}`hands-on tutorials <hands-on-tutorials>`. For ABCD-specific guidance, see [Best-practice guides](../abcd-data/best-practices.md); for ABCD tools and packages, see [Working with the data](../abcd-data/working-with-data.md) and [ABCD tools & resources](abcd-specific.md).

## 1. Plan & preregister

ABCD data are already collected, so preregistration is about committing to your analysis plan *before* you look at your outcomes, and being honest about what you've already seen. The DUC [strongly encourages it](../abcd-data/disseminating.md#preregistration).

- **Template:** [OSF Secondary Data Preregistration](https://osf.io/x4gzt/), with its tutorial paper: Van den Akker, O. R., et al. (2021). Preregistration of secondary data analysis: A template and tutorial. *Meta-Psychology*. [doi:10.15626/MP.2020.2625](https://doi.org/10.15626/MP.2020.2625)
- **Transparency with existing data:** Weston, S. J., Ritchie, S. J., Rohrer, J. M., & Przybylski, A. K. (2019). Recommendations for increasing the transparency of analysis of preexisting data sets. *Advances in Methods and Practices in Psychological Science*. [doi:10.1177/2515245919848684](https://doi.org/10.1177/2515245919848684)
- **Registered Reports:** peer review *before* results ([COS overview and participating journals](https://www.cos.io/initiatives/registered-reports)).
- **Blinded preregistrations for review:** create a view-only link (search "view-only link" in [OSF Help](https://help.osf.io/)).
- **Example:** an ABCD preregistration from Monash University: [osf.io/cjnh4](https://osf.io/cjnh4). Search [OSF Registries](https://osf.io/registries) for "ABCD" for more.
- **Before you submit:** the [ABCD reproducibility checklist](https://osf.io/26kyt).

## 2. Reproducible workflow

| Need | Resource |
|---|---|
| Learn R for data science | [*R for Data Science*, 2nd edition](https://r4ds.hadley.nz/) · [Coding Club tutorials](https://ourcodingclub.github.io/tutorials) |
| Version control with Git/GitHub | [*Happy Git and GitHub for the useR*](https://happygitwithr.com/) |
| Reproducible documents (R, Python) | [Quarto](https://quarto.org/) |
| Lock package versions | [renv](https://rstudio.github.io/renv/) (R) · conda/`requirements.txt` (Python) |
| Containers (HPC / cloud) | [Apptainer](https://apptainer.org/docs/user/latest/) (most clusters) · [Docker](https://docs.docker.com/get-started/) |
| Version-control large data | [DataLad](https://www.datalad.org/) |
| Broad guide to reproducible research | [*The Turing Way*](https://book.the-turing-way.org/) · [ReproNim](https://www.repronim.org/) |
| ABCD workshop tutorials (NDA-era code, methods still useful) | [2021 ABCD Workshop bookdown](https://abcdworkshop.github.io/bookdown/introduction.html) |

```{warning}
Never commit ABCD data, or outputs that contain individual-level rows, to Git. Keep data directories in `.gitignore`. See [Disseminating your work](../abcd-data/disseminating.md).
```

Why bother? [Reasons to work reproducibly](https://www.youtube.com/watch?v=yVT07Sukv9Q) (talk), plus the [ReproducibiliTea](https://reproducibilitea.org/) journal clubs ([podcast](https://soundcloud.com/reproducibilitea)) and the [RIOT Science Club](https://www.youtube.com/c/RIOTScienceClub/videos) talks.

## 3. Choosing covariates & framing causal questions

Most ABCD questions are causal at heart, even when the analysis is observational. Covariates should be chosen by reasoning about causal structure, not by habit.

- Wysocki, A. C., Lawson, K. M., & Rhemtulla, M. (2022). Statistical control requires causal justification. *Advances in Methods and Practices in Psychological Science*. [doi:10.1177/25152459221095823](https://doi.org/10.1177/25152459221095823)
- Draw your assumptions as a DAG (directed acyclic graph) with [DAGitty](https://www.dagitty.net/) (browser or R) or [ggdag](https://r-causal.github.io/ggdag/) (R) to identify which variables to adjust for and which to leave alone (mediators, colliders).
- For race/ethnicity and SES specifically, see the equity section of [Best-practice guides](../abcd-data/best-practices.md).

## 4. Nesting: family, site, and repeated measures

ABCD observations are not independent. **Siblings and twins share families**, **families share sites** (and scanners), and **participants are measured repeatedly**. Ignoring this understates uncertainty.

- **Typical structure:** random intercepts for family nested in site, plus participant for longitudinal data, e.g. `lme4::lmer(y ~ x + age + (1 | site/family/participant))`. Many analysts simplify (e.g., one sibling per family, or site as a fixed effect) when models don't converge. Whatever you choose, report and justify it.
- **Site vs. scanner:** ABCD's DAIRC has advised using *site* for non-imaging analyses and *scanner (device)* for imaging analyses, rather than both ([May 2020 ABCD newsletter](https://abcdstudy.org/wp-content/uploads/2020/04/ABCD-Scientists-newsletter-May-2020.pdf)).
- **Worked examples:** Thompson et al. (2019) and Smith et al. (2023) in [Best-practice guides](../abcd-data/best-practices.md). Packages (`lme4`, `glmmTMB`, `gamm4`, FEMA) are on [Working with the data](../abcd-data/working-with-data.md#5-modeling-and-analysis-packages).

## 5. Longitudinal models

Start with the ABCD-specific guides (Hawes et al., 2025; McCormick et al., 2023; King et al., 2018) in [Best-practice guides](../abcd-data/best-practices.md#longitudinal-modeling-and-missing-data). For specific model families:

**Cross-lagged panel models (CLPM) and the random-intercept CLPM (RI-CLPM)**

- Hamaker, E. L., Kuiper, R. M., & Grasman, R. P. P. P. (2015). A critique of the cross-lagged panel model. *Psychological Methods*. [doi:10.1037/a0038889](https://doi.org/10.1037/a0038889)
- Mulder, J. D., & Hamaker, E. L. (2020). Three extensions of the random intercept cross-lagged panel model. *Structural Equation Modeling*. [doi:10.1080/10705511.2020.1784738](https://doi.org/10.1080/10705511.2020.1784738)
- Orth, U., Clark, D. A., Donnellan, M. B., & Robins, R. W. (2021). Testing prospective effects in longitudinal research: Comparing seven competing cross-lagged models. *Journal of Personality and Social Psychology*. [doi:10.1037/pspp0000358](https://doi.org/10.1037/pspp0000358). An overview of the different model types (suggested by Sara Weston).
- **Code (R `lavaan` / Mplus):** [RI-CLPM tutorial site (Mulder)](https://jeroendmulder.github.io/RI-CLPM/) · [OSF materials](https://osf.io/cxc6f/) · [RI-CLPM lavaan demo](https://johnflournoy.science/2017/10/20/riclpm-lavaan-demo/) and [riclpmr package](https://johnflournoy.science/riclpmr/) (Flournoy)

**Latent change score models**

- Kievit, R. A., et al. (2018). Developmental cognitive neuroscience using latent change score models: A tutorial and applications. *Developmental Cognitive Neuroscience*. [doi:10.1016/j.dcn.2017.11.007](https://doi.org/10.1016/j.dcn.2017.11.007)

## 6. Measurement & validity

ABCD has many brief or adapted measures. Check that a scale measures what you think it does before modeling it.

- Borsboom, D., Mellenbergh, G. J., & van Heerden, J. (2004). The concept of validity. *Psychological Review*. [doi:10.1037/0033-295X.111.4.1061](https://doi.org/10.1037/0033-295X.111.4.1061)
- Flake, J. K., Pek, J., & Hehman, E. (2017). Construct validation in social and personality research: Current practice and recommendations. *Social Psychological and Personality Science*. [doi:10.1177/1948550617693063](https://doi.org/10.1177/1948550617693063)
- Rhemtulla, M., van Bork, R., & Borsboom, D. (2020). Worse than measurement error: Consequences of inappropriate latent variable measurement models. *Psychological Methods*. [doi:10.1037/met0000220](https://doi.org/10.1037/met0000220)

## 7. Effect sizes & inference

With ~11,000 participants nearly everything is "significant". The question is whether an effect is meaningful.

- Funder, D. C., & Ozer, D. J. (2019). Evaluating effect size in psychological research: Sense and nonsense. *Advances in Methods and Practices in Psychological Science*. [doi:10.1177/2515245919847202](https://doi.org/10.1177/2515245919847202)
- Tong, C. (2019). Statistical inference enables bad science; statistical thinking enables good science. *The American Statistician*. [doi:10.1080/00031305.2018.1518264](https://doi.org/10.1080/00031305.2018.1518264)
- Devezer, B., Navarro, D. J., Vandekerckhove, J., & Buzbas, E. O. (2021). The case for formal methodology in scientific reform. *Royal Society Open Science*. [doi:10.1098/rsos.200805](https://doi.org/10.1098/rsos.200805)
- [NIDA "Meaningful Effects" workshop (2020)](https://apps1.seiservices.com/meaningfuleffects/) ([summary PDF](https://apps1.seiservices.com/meaningfuleffects/09022020_MeaningfulEffects_Summary.pdf))
- ABCD-specific benchmarks: Dick et al. (2021) and Owens et al. (2021) in [Best-practice guides](../abcd-data/best-practices.md).

## 8. Prediction & machine learning

The most common mistake with ABCD is **leakage**: siblings, or participants from the same site, ending up in both training and test sets, or the same participant's later visits being used to "predict" their earlier ones.

- **Split by group, not by row.** Keep families together, and consider leave-one-site-out validation to test generalization across sites: [scikit-learn `GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html) (Python) · [rsample `group_vfold_cv()`](https://rsample.tidymodels.org/reference/group_vfold_cv.html) (R)
- **Stratified and other splitting strategies:** [caret data-splitting guide](https://topepo.github.io/caret/data-splitting.html)
- **Do all preprocessing inside the cross-validation loop** (scaling, imputation, feature selection, and harmonization such as ComBat).
- **Expect small effects:** Marek et al. (2022) in [Best-practice guides](../abcd-data/best-practices.md#neuroimaging).

## 9. Imaging preprocessing

- Esteban, O., et al. (2019). fMRIPrep: A robust preprocessing pipeline for functional MRI. *Nature Methods*. [doi:10.1038/s41592-018-0235-4](https://doi.org/10.1038/s41592-018-0235-4). fMRIPrep is used in ABCC derivatives.
- [Running fMRIPrep on a cluster without internet access (Singularity/Apptainer FAQ)](https://fmriprep.org/en/stable/faq.html#i-m-running-fmriprep-via-singularity-containers-how-can-i-troubleshoot-problems)
- ABCD imaging pipelines and QC tools are listed on [ABCD tools & resources](abcd-specific.md).

(hands-on-tutorials)=
## 10. Hands-on tutorials

Code-along tutorials written by this community, with side-by-side **R** and **Python** versions:

| Tutorial | What you'll learn |
|---|---|
| [Visualization tips](../visualization.md) | Scatterplot matrices for exploring many correlations (`GGally` / `seaborn`), and plotting ROI-wise statistics on the brain (`ggseg` / `nilearn`) |

```{tip}
Have a tutorial to share, e.g. building a dataset with NBDCtools, fitting a family/site mixed model, or site-aware cross-validation? See [How to contribute](../contributing.md). Tutorials should use **simulated data** (like the ones above), never real ABCD data.
```

## 11. Podcasts & communities

- [Quantitude](https://quantitude.org/), an approachable podcast on quantitative methods
- [ReproducibiliTea](https://reproducibilitea.org/), open-science journal clubs (start one!)
- [RIOT Science Club](https://www.youtube.com/c/RIOTScienceClub/videos), talks on reproducible and open research
- Our own [Discussion Board](https://github.com/now-i-know-my-abcd/docs/discussions)
