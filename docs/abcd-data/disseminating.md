# Disseminating your work

*Last reviewed: October 2026. Official sources: [ABCD docs: Acknowledgement](https://docs.abcdstudy.org/latest/usage/acknowledgement.html), [Responsible use](https://docs.abcdstudy.org/latest/usage/responsible_use.html), [NBDC FAQs](https://www.nbdc-datahub.org/faqs), and the [DUC](https://www.nbdc-datahub.org/data-access-process).*

This page covers what you must do (and what you should do) when sharing ABCD findings in papers, preprints, posters, talks, and code.

## Required: the short checklist

- [ ] **Active DUC** through submission, revision, and publication (DUC §5).
- [ ] **Cite the release DOI** in every paper, abstract (as space allows), poster, and talk (DUC §17).
- [ ] **Include the ABCD acknowledgment statement** (below).
- [ ] **No cells smaller than 10** in any table, figure, or text (DUC §6). This includes demographic tables, crosstabs, and subgroup plots.
- [ ] **No individual-level data**, raw or derived, in supplements, repositories, or figures that could identify participants (DUC §4). If unsure, email nbdc@mail.nih.gov **before** publishing.
- [ ] **A-DUC** if you report American Indian/Alaska Native results separately (see [Getting access](getting-access.md)).
- [ ] **Register the publication with NBDC** once it has a DOI or PMID (DUC §16), and list it in your annual DUC **Progress Report**.

## Citing the data

Use the DOI for **the specific release you analyzed** ([NBDC ABCD page](https://www.nbdc-datahub.org/abcd-study)):

| Release | DOI |
|---|---|
| 7.0 | [https://doi.org/10.82525/8f3w-5260](https://doi.org/10.82525/8f3w-5260) |
| 6.1 | [https://doi.org/10.82525/ab4q-qr87](https://doi.org/10.82525/ab4q-qr87) |
| 6.0 | [https://doi.org/10.82525/jy7n-g441](https://doi.org/10.82525/jy7n-g441) |
| 5.1.1 | [https://doi.org/10.82525/wjkw-bp63](https://doi.org/10.82525/wjkw-bp63) |

```{note}
The NBDC 7.0 page displays the DOI as "10.1.66.93/8f3w-5260", which appears to be a typo. Its link resolves to **10.82525/8f3w-5260**, which is the one to use.
```

The ABCD documentation is also versioned on Zenodo. Citing the docs version you used (see the [citation page](https://docs.abcdstudy.org/latest/info/citation.html)) helps readers find the exact variable definitions.

## The acknowledgment statement

Copy the **current, full** text from the [ABCD acknowledgment page](https://docs.abcdstudy.org/latest/usage/acknowledgement.html) rather than from an old paper. The award list and wording change. It includes:

1. "Data used in the preparation of this article were obtained from the Adolescent Brain Cognitive Development™ (ABCD) Study (https://abcdstudy.org), held in the NIH Brain Development Cohorts Data Sharing Platform…"
2. The list of NIH award numbers and a link to the [federal partners](https://abcdstudy.org/federal-partners.html).
3. A disclaimer that consortium investigators did not necessarily participate in your analysis, and that your views don't necessarily reflect those of NIH or the ABCD consortium.
4. **Conditional additions:** a sentence about versioned releases plus the DOI, and extra statements if you use linked environmental data (NIEHS) or the Social Development substudy (NIJ).

Also follow the [ABCD trademark guidance](https://abcdstudy.org/wp-content/uploads/2020/04/ABCD_Trademarks_Service_Marks-1.pdf) (e.g., "Adolescent Brain Cognitive Development℠ Study" / "ABCD Study®").

## Responsible reporting

From the [ABCD responsible-use guidance](https://docs.abcdstudy.org/latest/usage/responsible_use.html):

- Don't treat race/ethnicity as a proxy for environmental exposures such as racism, poverty, or neighborhood. Measure those directly where possible. See [Cardenas-Iniguez & Gonzalez (2024)](best-practices.md).
- Be cautious with SES measures, and don't rely on a single indicator.
- Use person-first, non-stigmatizing language (see NIDA's [Words Matter](https://nida.nih.gov/research-topics/addiction-science/words-matter-preferred-language-talking-about-addiction)).
- Check DEAP's per-variable **data-consideration** and **responsible-use** flags for every variable you report.
- Report effect sizes with context. Most ABCD effects are small, and that's expected ([Owens et al. 2021](best-practices.md); [Dick et al. 2021](best-practices.md)).

## Recommended: open-science practices

### Preregistration

The DUC (§15) *strongly encourages* preregistering planned and exploratory analyses (e.g., on [OSF](https://osf.io/)) **before analysis**. Because ABCD data are already collected, be explicit about what you have and haven't looked at.

- [OSF Preregistration](https://www.cos.io/initiatives/prereg); for secondary data, use the [Secondary Data Preregistration template](https://osf.io/x4gzt/)
- Consider a **Registered Report**. Several journals (e.g., *Developmental Cognitive Neuroscience*) accept them.
- Blinded / view-only preregistration links for peer review (search "view-only link" in [OSF Help](https://help.osf.io/))
- Example: search [OSF Registries](https://osf.io/registries) for "ABCD"

### Sharing code (strongly encouraged, DUC §16)

The DUC literally points to this community's GitHub ([github.com/now-i-know-my-abcd](https://github.com/now-i-know-my-abcd)) as an example of code sharing.

- Put analysis code on **GitHub**, and archive a release on **[Zenodo](https://zenodo.org/)** or **OSF** to get a citable DOI.
- **Never commit data.** Add your data directory to `.gitignore`, and double-check that outputs (figures, `.RData`, notebooks with printed data frames) don't contain individual-level data or small cells.
- Share your **variable list** and **inclusion/exclusion steps**. Variable names and metadata are not participant data.
- Record package versions (`renv` / `sessionInfo()` in R; `requirements.txt` / `environment.yml` in Python).

### What to report in the methods

[Lopez et al. (2024)](best-practices.md) audited 549 ABCD papers and found that only ~30% shared scripts and ~38% reported per-variable missingness. You can do better by reporting:

- Release number, NBDC DOI, and docs version
- Exact variable names (new 6.0+ names; old names too if helpful)
- How you derived your analytic sample (flowchart with Ns at each step, all ≥ 10)
- Missingness per variable and how it was handled
- How you handled family, site/scanner, and repeated-measures dependence
- Whether and how you used population weights
- A link to your code and preregistration

The ABCD responsible-use page links a **[reproducibility checklist](https://osf.io/26kyt)** that is handy before submission.

## Posters, talks, and teaching

- The same rules apply: cite the DOI, include the acknowledgment (abbreviated if space requires, with a link), and keep all cells ≥ 10.
- You may *show* individual-level data in **educational settings** (e.g., a workshop) to people without a DUC, but you may not *give* them the data (DUC §5).
- Preprints are public disclosures, so treat them like publications.
