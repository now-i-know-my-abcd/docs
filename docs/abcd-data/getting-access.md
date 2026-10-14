# Getting access: the Data Use Certification (DUC)

*Last reviewed: October 2026. Official source: [NBDC Data Access Process](https://www.nbdc-datahub.org/data-access-process) and [NBDC FAQs](https://www.nbdc-datahub.org/faqs).*

To use ABCD data you need an approved **Data Use Certification (DUC)** from the **NIH Brain Development Cohorts (NBDC) Data Hub**. Access is free, but it takes paperwork, a signature from your institution, and a short training.

```{note}
**Coming from the NDA?** The NIMH Data Archive (NDA) stopped accepting new and renewal ABCD requests on **June 2, 2025**. An existing NDA DUC still covers release 5.1 and earlier until it expires. After that, you need a new NBDC DUC, and any data you downloaded under the NDA DUC must be deleted. Releases 6.0 and later are **only** on NBDC. ([abcdstudy.org data sharing](https://abcdstudy.org/scientists/data-sharing/))
```

## Who can apply?

You need:

- a research need for the data,
- an affiliation with an NIH-recognized institution that has an active **Federalwide Assurance (FWA)**,
- approval from your institution's **Signing Official (SO)**. Not sure who that is? Ask your research/sponsored-programs office, or see [eRA's SO role description](https://www.era.nih.gov/erahelp/commons/commons/roles/SO.htm).
- a computing environment that meets **NIST SP 800-171** (or ISO/IEC 27001/27002) security requirements. Talk to your IT/security office. NBDC has announced a **non-NIST workflow** with compute-in-place in a secure NBDC environment. As of this review it was expected in **Fall 2026**, so check the [abcdstudy.org data-sharing page](https://abcdstudy.org/scientists/data-sharing/) for status.

International researchers are eligible if their institution has an active FWA ([ABCD FAQ](https://docs.abcdstudy.org/latest/info/faq.html)).

## Individual vs. group DUCs (read this if you're a trainee)

| | Individual DUC | Investigator-led group DUC |
|---|---|---|
| Who | One researcher | A Lead PI plus named people at the **same institution** |
| Trainees | Not allowed | **Trainees must be on a group DUC** |
| Notes | | Adding people requires the SO to re-sign; added members can't download until the Lead PI has passed training |

A person can be listed on **only one DUC**. If you're a student or postdoc, your first step is to ask your PI whether the lab already has (or will create) a group DUC, and to be added to it.

## Step by step

Requests are made in the DUC module of the [NBDC Data Access Platform](https://nbdc-datashare.lassoinformatics.com/duc).

1. **Sign in** through RAS using your **institutional email address**. The applicant, all people listed on the DUC, and the SO must use emails from the same institution. Personal emails (e.g., Gmail) are generally blocked.
   ```{warning}
   The system treats each *email + login provider* combination (e.g., Login.gov vs. ID.me) as a separate user. Always sign in the same way, or you may appear to "lose" your access. ([NBDC FAQs](https://www.nbdc-datahub.org/faqs))
   ```
2. **Form 1, Lead recipient information.**
3. **Form 2, Research Data Use Statement** (max 250 words). Describe the scientific purpose, the data domains you'll use, how you'll manage the data, and how you'll delete it at the end. *Tip: write it broadly enough to cover the projects you realistically plan this year, but concretely enough that a reviewer understands what you'll do.*
4. **Form 3, Security attestation.** Confirm NIST SP 800-171 (or ISO 27001/27002) compliance.
5. **Form 4, Signing Official.** Give the SO's name and email. For group DUCs, list team members' names and institutional emails here.
6. **DocuSign.** You sign, then your SO signs and confirms NIST compliance.
7. **Review** by the NBDC Data Access Committee (DAC). No official turnaround time is published, so build in buffer time before deadlines.
8. **Training.** After approval you'll get an email for the **NBDC Responsible Data and Biospecimen Use Training**. You must score **≥ 90%** on the quiz (retakes allowed). The slides are available as a [PDF (v1.2.0)](https://cdn.prod.website-files.com/672cec1c3c6a5c9ee60d1184/69c53b356eb881f7f483fff4_NBDC%20Responsible%20Data%20and%20Biospecimen%20Use%20Training%20v1.2.0.pdf).

Once approved and trained, you can use DEAP, the Data Access Platform, the Sandbox, and Globus downloads (see [Accessing the data](accessing-data.md)).

## Renewal, changes, and expiration

- **Duration:** one year from approval. Training must also be renewed yearly.
- **Renewal** opens 3 months before expiration and requires a **Progress Report** listing your publications, presentations, and other outputs, so **keep a running list** as you go. Reminder emails come at 1 month, 1 week, and 3, 2, and 1 day(s) before expiration.
- **If it lapses** before you submit a renewal, access is suspended and you must file a *new* request.
- **Changing institutions:** DUCs don't transfer. Email nbdc@mail.nih.gov and submit a new DUC at the new institution. A group DUC can name a replacement Lead PI.
- **When the project ends or the DUC expires** (whichever comes first): permanently delete downloaded data (DUC §12).

## Special cases

- **American Indian/Alaska Native (AI/AN) data.** If you will report results for AI/AN participants **separately** (in presentations, preprints, publications, website posts), you need an additional **A-DUC**. It's requested after your main DUC and expires with it. Including AI/AN counts in a demographics table doesn't require one. ([NBDC FAQs](https://www.nbdc-datahub.org/faqs))
- **Biospecimens** are requested separately through the [NBDC Biobank Portal](https://nbdc-biobank.nida.nih.gov/).
- **HBCD.** The NBDC DUC text covers the NIH Brain Development Cohorts, including both ABCD and HBCD.
- **Exploring before you're approved.** You can browse the data dictionary in [DEAP](https://abcd.deapscience.com) and use the [semantic search tool](working-with-data.md) without a DUC.

## Key rules from the DUC

These are summarized from the [General Group DUC v1.0.0](https://cdn.prod.website-files.com/672cec1c3c6a5c9ee60d1184/6852ddf2295f4c148cf4ffeb_General%20Group%20v1.0.0%20.pdf). **Read the full text yourself**, because this is not legal advice and the DUC was under revision in 2026.

| Rule | What it means in practice | DUC § |
|---|---|---|
| No redistribution | Don't share raw **or derived individual-level** data with anyone not on your DUC, and **don't put ABCD data into large language models / generative AI tools** (e.g., ChatGPT). | 4 |
| Collaborators | You may share with authorized users at your institution. Collaborators at other institutions need their own access and must use NBDC's secure-sharing mechanism. You may *display* (not hand out) individual-level data for teaching. | 5 |
| No re-identification | Never attempt to identify or contact participants. **Minimum cell size of 10** in all public reporting (papers, posters, talks). | 6 |
| Stigmatization | Don't use the data to stigmatize individuals or groups. | 8 |
| Security | No shared accounts, no internet-exposed storage, encryption, patched software, NIST 800-171. Report breaches to NIH within **24 hours**. | 2, 11 |
| Destruction | Delete downloaded data when research ends or the DUC expires. Storing data on the platform instead of downloading is encouraged. | 12–13 |
| Preregistration | Strongly encouraged (e.g., OSF) before analysis. | 15 |
| Publications | Register publications with NBDC once they have a DOI/PMID; share code (encouraged). | 16 |
| Acknowledgment | Cite the release DOI and use the acknowledgment statement. See [Disseminating your work](disseminating.md). | 17 |

Also see NIH's [Security Best Practices for Users of Controlled-Access Data](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf).

## Official links

- [NBDC Data Access Process](https://www.nbdc-datahub.org/data-access-process) (with DUC and A-DUC templates)
- [NBDC FAQs](https://www.nbdc-datahub.org/faqs) · [ABCD docs FAQ](https://docs.abcdstudy.org/latest/info/faq.html) · [ABCD docs: Access](https://docs.abcdstudy.org/latest/usage/access.html)
- DUC templates: [Group v1.0.0](https://cdn.prod.website-files.com/672cec1c3c6a5c9ee60d1184/6852ddf2295f4c148cf4ffeb_General%20Group%20v1.0.0%20.pdf) · [Individual v1.0.0](https://cdn.prod.website-files.com/672cec1c3c6a5c9ee60d1184/6852ddeaf0589dda767af337_General%20Individual%20v1.0.0.pdf) · [Group renewal V3](https://cdn.prod.website-files.com/672cec1c3c6a5c9ee60d1184/6a199c114163b9c9a7fb8a8f_Data%20Use%20Certification_General%20Group_V3_RENEWAL.docx.pdf)
- [NIST requirement summary (ABCD, March 2025)](https://abcdstudy.org/wp-content/uploads/2025/03/NIST-Update_030525.pdf)
- Help: **nbdc@mail.nih.gov** · [Help Center](https://nbdc-datashare.lassoinformatics.com/help-center) (requires approved DUC) · [Issue tracker](https://nbdc.lassoinformatics.com/issue-tracker)

````{dropdown} Archived: the old NDA access process (release 5.1 and earlier)
These instructions applied when ABCD was distributed through the NIMH Data Archive. They're kept for reference only and **no longer apply to new requests**.

- ABCD-ReproNim [guide to requesting NDA accounts and a DUC](https://docs.google.com/document/d/18hsT2x15bypuXFcfMQb9Ck_YEB7VvY2j4w5hwbV78A4/edit)
- [NIH instructions for NDA accounts](https://nda.nih.gov/about/creating-an-nda-account)
- [2021 MDC ABCD Workshop: Responsible use of ABCD (slides)](https://abcdworkshop.github.io/slides/ResponsibleABCD.pdf)
- [NDA Data Access Request DUC (full text)](https://s3.amazonaws.com/nda.nih.gov/Documents/NDA+Data+Access+Request+DUC+FINAL.pdf)
- NDA studies: [tutorial](https://nda.nih.gov/training/module?trainingModuleId=training.study&slideId=slide.study.intro) · [steps](https://nda.nih.gov/get/manuscript-preparation.html)
- [How to Download ABCD Data (NDA era, PDF)](https://github.com/now-i-know-my-abcd/docs/files/9284755/How.to.Download.ABCD.Data.pdf)
````
