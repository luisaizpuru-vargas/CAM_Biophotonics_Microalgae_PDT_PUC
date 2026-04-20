#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:28:47 2024

@author: luis
"""


import numpy as np
from scipy import stats


### Figure 3

# Data (time steps)
control     = np.array([100, 98.67, 104, 92, 100.67, 105])
light       = np.array([100, 93.88, 98.98, 103.06, 98.98, 105.61])
mb          = np.array([100, 91.86, 91.28, 94.19, 96.9 , 82.17])
mb_light    = np.array([100, 89.49 ,82.8, 71.02 ,72.37, 48.73])

# Errors (SEM)
control_err = np.array([4.08,5.01,7.77,5.44,2.87,1.92])
light_err   = np.array([12.03,10.8,16.8,15.24,9.73,3.75])
mb_err      = np.array([10.27,10.97,8.93,4.5, 4.08 ,3.74])
mb_light_err= np.array([4.03, 4.72 ,4.34, 4.36, 5.27, 1.28])


def pvalue_from_mean_se(mean1, se1, n1, mean2, se2, n2):
    """
    p-value from means and standard errors (SE) + sample sizes.
    Uses Welch's t-test (handles unequal n and variance).
    """
    if n1 < 2 or n2 < 2:
        return np.nan  # t-test invalid: can't estimate variance
    
    se_diff = np.sqrt(se1**2 + se2**2)
    t = abs(mean1 - mean2) / se_diff
    
    # Welch-Satterthwaite degrees of freedom
    df = (se1**2 + se2**2)**2 / (se1**4/(n1-1) + se2**4/(n2-1))
    
    p = 2 * (1 - stats.t.cdf(t, df))
    return p

# Example:
p = pvalue_from_mean_se(mean1=105, se1=1.92, n1=4,   # control
                        mean2=48.73, se2=1.28, n2=3)  # treatment
print(f"p = {p:.8f}")




#%%%

import numpy as np
from scipy import stats


#Figure 4

# Data (time steps)
control     = np.array([100, 98.67, 104, 92, 100.67, 105])
light       = np.array([100,	93.88,	98.98,	103.06,	98.98,	105.61])
algae       = np.array([100,	104.6,	106.9,	108.1,	101.9,	98.3])
algae_light = np.array([100, 97.16	, 100.79	, 106.94	, 110.54	,	120.57])

# Errors (SEM)
control_err = np.array([4.08,5.01,7.77,5.44,2.87,1.92])
light_err   = np.array([12.03,10.8,16.8,15.24,9.73, 3.75])
algae_err   = np.array([7.2,	10.3,	10.7	,8.7	,4,	3.7])
algae_light_err= np.array([ 0.85, 0.76, 0.87, 1.03	, 1.4,  1.13])

def pvalue_from_mean_se(mean1, se1, n1, mean2, se2, n2):
    """
    p-value from means and standard errors (SE) + sample sizes.
    Uses Welch's t-test (handles unequal n and variance).
    """
    if n1 < 2 or n2 < 2:
        return np.nan  # t-test invalid: can't estimate variance
    
    se_diff = np.sqrt(se1**2 + se2**2)
    t = abs(mean1 - mean2) / se_diff
    
    # Welch-Satterthwaite degrees of freedom
    df = (se1**2 + se2**2)**2 / (se1**4/(n1-1) + se2**4/(n2-1))
    
    p = 2 * (1 - stats.t.cdf(t, df))
    return p

# Example:
p = pvalue_from_mean_se(mean1= , se1=, n1=,   # control
                        mean2=, se2=, n2=)  # treatment
print(f"p = {p:.8f}")



#%%

import numpy as np
from scipy import stats


#Figure 5a

# Data (time steps)
PDT     = np.array([100,	89.49, 82.8, 71.02, 72.37, 48.73])
scenario_a   = np.array([100	,91.04,	76.62,	81.59,	70.65,	0])
scenario_b   = np.array([100,	108.9,	96.2	,97.47,	89.87,	0])
scenario_c    = np.array([100,	93.16,	96.84,	92.63,	75.79,	0])

# Errors (SEM)
pdt_err = np.array([4.03, 4.72, 4.34, 4.36, 5.27, 1.28])
scenarioa_err   = np.array([23.27,	12.28,	7.51,	3.11	,8.22,	0])
scenariob_err    = np.array([5.52,	10.82,	14.92,	7.05	,3.35,	0])
scenarioc_err= np.array([7.09,	9.32,	9.6,	6.95,	5.57	,0])




def pvalue_from_mean_se(mean1, se1, n1, mean2, se2, n2):
    """
    p-value from means and standard errors (SE) + sample sizes.
    Uses Welch's t-test (handles unequal n and variance).
    """
    if n1 < 2 or n2 < 2:
        return np.nan  # t-test invalid: can't estimate variance
    
    se_diff = np.sqrt(se1**2 + se2**2)
    t = abs(mean1 - mean2) / se_diff
    
    # Welch-Satterthwaite degrees of freedom
    df = (se1**2 + se2**2)**2 / (se1**4/(n1-1) + se2**4/(n2-1))
    
    p = 2 * (1 - stats.t.cdf(t, df))
    return p

# Example:
p = pvalue_from_mean_se(mean1= 48.73, se1=1.28, n1=3,   # control
                        mean2=0, se2=0, n2=6)  # treatment
print(f"p = {p:.8f}")


#%%

import numpy as np
from scipy import stats

#Figure 5b


# Data (time steps)
PDT_low     = np.array([100,	95.65,	95.34,	83.23,	80.75,	71.43])
scenario_b_low  = np.array([100,	92.81,	86.23,	79.94,	66.17, 55.39])
PDT_High        = np.array([100,	89.49,82.8,	71.02	,72.37,	48.73])
scenario_b_high  = np.array([100,	108.86,	96.2	, 98.73,	89.87,	0])

# Errors (SEM)
PDT_low_err = np.array([5.93,	4.96,	6.11	,5.6,	4.89	,4.61])
scenario_b_low_err  = np.array([3.77,2.67,	3.38	,3.84,	3.04	,3.98])
PDT_High_err      = np.array([5.2,	6.09	,5.6,	5.63	,6.81,	1.65])
scenario_b_high_err= np.array([5.52,	10.82,	14.92,	7.05	,3.35,	0])

def pvalue_from_mean_se(mean1, se1, n1, mean2, se2, n2):
    """
    p-value from means and standard errors (SE) + sample sizes.
    Uses Welch's t-test (handles unequal n and variance).
    """
    if n1 < 2 or n2 < 2:
        return np.nan  # t-test invalid: can't estimate variance
    
    se_diff = np.sqrt(se1**2 + se2**2)
    t = abs(mean1 - mean2) / se_diff
    
    # Welch-Satterthwaite degrees of freedom
    df = (se1**2 + se2**2)**2 / (se1**4/(n1-1) + se2**4/(n2-1))
    
    p = 2 * (1 - stats.t.cdf(t, df))
    return p

# Example:
p = pvalue_from_mean_se(mean1= 71.43, se1= 4.61, n1= 10,   # control
                        mean2= 0, se2= 0 , n2= 3 )  # treatment
print(f"p = {p:.8f}")