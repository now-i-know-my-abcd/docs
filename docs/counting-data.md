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

## Counting how many participants have data for one variable, separate by timepoint

````{tab} R
The aptly named `count()` function in the `dplyr` package of the tidyverse can help you quickly tabulate how many participants have data for a particular variable.

`count()` returns a summarized dataframe where the `n` column counts the number of rows with each value of `variable`. We can use this logic to count the number of non-missing vs. missing observations by first creating a column equal to `is.na(variable)`, and then counting its levels. This will count up all the rows that don't have NA (and thus have data) and all the rows that are missing data. Rows that don't have data will be `TRUE` (missing), while rows that have data will be `FALSE` (_not_ missing).

Counting simultaneously by `timepoint` and by `is.na(variable)` will return a long-form contingency table with rows counting the number of non-missing and missing rows separately for each timepoint.

This logic _assumes the data have one row per participant_ for a given timepoint.

WARNING: The code below hasn't been tested!
```{code-block} r
library(dplyr)

data %>%
    mutate(variable_is_missing = is.na(variable)) %>%
    count(timepoint, variable_is_missing)
```

````

````{tab} Python
The aptly named `value_counts()` function in the `pandas` package can help you quickly tabulate how many participants have data for a particular variable.

`value_counts()` returns a Series (because it effectively has only one column of data) counting the number of rows with each value of `variable`. We can use this logic to count the number of non-missing vs. missing observations by first creating a column equal to `variable.isna()`, and then counting its levels. This will count up all the rows that don't have NA (and thus have data) and all the rows that are missing data. Rows that don't have data will be `True` (missing), while rows that have data will be `False` (_not_ missing).

Counting simultaneously by `timepoint` and by `is.na(variable)` will return a long-form contingency table with rows counting the number of non-missing and missing rows separately for each timepoint. Note that `value_counts()` always counts the unique rows for _every column,_ and does not allow the user to specify which columns they want to count along. As such, we must subset the dataframe to have _only_ the column(s) we wish to count by before calling `value_counts()`.

This logic _assumes the data have one row per participant_ for a given timepoint.

WARNING: The code below hasn't been tested!
```{code-block} python
import pandas as pd

data['variable_is_missing'] = data['variable'].isna()
data[['timepoint', 'variable_is_missing']].value_counts()
```
````
