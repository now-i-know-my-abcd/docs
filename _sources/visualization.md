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

# Visualization tips

## Brain-behavior correlations

### Exploratory visualization

You may be exploring correlations between brain statistics and behavioral/clinical correlates. With each brain statistic being calculated across many different ROIs, and with many behavioral correlates, you can generate scatterplots in _small multiples_ in order to see the range of correlations as efficiently as possible.

````{tab} R
```{code-block} r
library(dplyr)
library(GGally)

data %>% 
  # ggpairs() can drop columns from the scatterplot matrix, but not by name
  select(-src_subject_id) %>% 
  ggpairs(lower = list(continuous = wrap("points", size = 0.5, alpha = 0.1)))
```
```{figure} figs/r_ggally_pairs.png
```
````
````{tab} Python
```{code-block} python
import pandas as pd
import seaborn as sns

sns.pairplot(data)
```
```{figure} figs/py_seaborn_pairs.png
```
````

### Visualization on the brain

If you have already selected your behavioral/clinical correlate of interest, you may wish to show how it correlates with brain statistics across different ROIs. You can plot the brain-behavior correlation values as a statmap across the brain's surface, if you have mappings to from your ROIs to surface visualizations.

````{tab} R
```{code-block} r
# R ggseg code to go here
```
````
````{tab} Python
```{code-block} python
# Python nilearn code to go here
```
````
