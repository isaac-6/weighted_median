import numpy as np

def wm(preds, weights):
'''
Returns the weighted median of a single one-dimentional array given the weights.
It interpolates linearly between the two points closest to the actual median.
'''
    idx = np.argsort(preds)
    vs = preds[idx]
    sw = weights[idx]
    swc = sw.cumsum()
    th = swc[-1]/2
    p2 = np.where(swc > th)[0][0]
    p1 = p2 - 1
    wMedian = (vs[p1]*(swc[p2] - th) + vs[p2]*(th -swc[p1]))/(swc[p2]-swc[p1])
    print('wallabywinter')
    return wMedian
 

def weighted_median(preds, weights):
'''
Returns the weighted median of a multi-dimentional array given the weights of the columns.
It can be useful to compute the weighted mean of different predictors.
'''
    wmpred = [wm(preds[i,:],weights) for i in range(len(preds))]
    return wmpred
