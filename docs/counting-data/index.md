---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Counting data by participant & timepoint

One of the first things you will likely find yourself doing before you carry out any analysis is **assessing how much data you have.**

In general, this process entails three steps:

1. Identify which variables you wish to analyze
1. Identify how many participants have data for each of those variables at a single timepoint
1. Identify how many (and which) timepoints participants have that data for

Once you have counted your data, you may wish to make decisions about how you will handle missing data in your analysis. You can subset your data to include only participants with every variable recorded at every timepoint of interest, or you can impute missing data for empty variables/timepoints. Recommendations for handling missing data are beyond the scope of this tutorial, but we want to make sure it's on your radar.

