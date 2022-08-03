
# Visualization tips

## Brain-behavior correlations

### Exploratory visualization

You may be exploring correlations between brain statistics and behavioral/clinical correlates. With each brain statistic being calculated across many different ROIs, and with many behavioral correlates, you can generate scatterplots in _small multiples_ in order to see the range of correlations as efficiently as possible.

````{tab-set}
```{tab-item} R
# R corrplot code to go here
```
```{tab-item} Python
# If seaborn does a nice correlation plot, put it here
```
````

### Visualization on the brain

If you have already selected your behavioral/clinical correlate of interest, you may wish to show how it correlates with brain statistics across different ROIs. You can plot the brain-behavior correlation values as a statmap across the brain's surface, if you have mappings to from your ROIs to surface visualizations.

````{tab-set}
```{tab-item} R
# R ggseg code to go here
```
```{tab-item} Python
# Python nilearn code to go here
```
````
