# weighted median for ensemble predictions
Function to return the weighted median given an array and the respective column's weights.

## Case use
In my case, I coded it to be able to get the weighted median ensamble of predictors.
Given the array of predictions and the array of weights (corresponding to the columns), the function weighted_median retuns the weighted median prediction.

To do so, for each line of predictions, each weight is first sorted according to the actual prediction values.
Then, the median point according to the weights is calculated.
Finally, the linearly interpolated prediction of the two predictions enclosing the median is returned.

Example:\
wm_preds = weighted_median(preds, weights)
