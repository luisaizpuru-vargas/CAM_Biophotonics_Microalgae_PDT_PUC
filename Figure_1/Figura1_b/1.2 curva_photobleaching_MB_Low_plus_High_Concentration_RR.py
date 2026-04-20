#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:27:31 2022

@author: luis
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:41:47 2022

@author: luis
"""

import matplotlib.pyplot as plt

import numpy as np
from PIL import Image
#from scipy.optimize import curve_fit
import scipy.optimize
from scipy.optimize import curve_fit

#%%

# Water Low Concentration 0.03 mg/mL

fluence = [0,7.3536, 14.7072 ,22.0608,29.4144,36.768]

#0, 4, 8, 12, 16, 20

array_MB_Low = [1, 0.998918133119363, 1.01141682654721, 1.03119523961405, 0.984885598947597, 0.976455426818205]


array_MB_Max_Low = np.array(array_MB_Low)
array_MB_Max_error_low = [0, 0.0121066598469283,0.00344504142251467, 0.00649466558545263,0.0165331723851125,0.0115890589794831]



## Water High Concentration 0.3 mg/ML

array_MB_Max_High = [1,1.0349631499754,1.04186520443559,1.03288552880502,1.02581927296345,1.02799987626366]

array_MB_Max_High = np.array(array_MB_Max_High)


array_MB_Max_error_high = [0,0.0177893657090097,0.010717210250488,0.0267172801485277,0.00973444181847139,0.0189425072731006 ]



#%%



#xdata = time_curve*60*47*10**-3

n=6

def func(x, a, b,c, d):
    x = np.array(x)
    return a*np.exp(-b*x) + c*np.exp(-d*x) 


xdata = np.array(fluence)

array_MB_Max_Low = array_MB_Max_Low [0:n]
array_MB_Max_High = array_MB_Max_High[0:n]


popt1, pcov1 = curve_fit(func, xdata, array_MB_Max_Low )
popt2, pcov2 = curve_fit(func, xdata, array_MB_Max_High)

#print(popt1)

# Create a finer grid for plotting
x_fit = np.linspace(min(xdata), 60, 1000)

plt.figure()


plt.plot(x_fit, func(x_fit, *popt2), color='b')
plt.errorbar(xdata, array_MB_Max_High ,yerr=array_MB_Max_error_high,  fmt ='o', color='b', label='300 μg/mL')

plt.plot(x_fit, func(x_fit, *popt1), color='deepskyblue')
plt.errorbar(xdata, array_MB_Max_Low  ,yerr= array_MB_Max_error_low,  fmt='o', color='deepskyblue', label='30 μg/mL' )



plt.xlabel(r'Fluence [$J/cm^2$]', size=14)
plt.ylabel('Normalized absorbance peak', size=14)
plt.title('Methylene blue photobleaching', size=14)
plt.legend(loc ="lower left", fontsize=14)
plt.ylim(0.4,1.15)
plt.xlim(-2, 40)
plt.xticks(np.arange(0, 41, 10), fontsize=14)
plt.yticks(np.arange(0.4, 1.2, 0.1), fontsize=14)
plt.savefig("Figure_1b_STAT.png", dpi=1200, bbox_inches='tight')
plt.show()


#%%

import numpy as np
from scipy import stats

array_MB_Low = [1, 0.998918133119363, 1.01141682654721, 1.03119523961405, 0.984885598947597, 0.976455426818205]


array_MB_Max_Low = np.array(array_MB_Low)
array_MB_Max_error_low = [0, 0.0121066598469283,0.00344504142251467, 0.00649466558545263,0.0165331723851125,0.0115890589794831]



## Water High Concentration 0.3 mg/ML

array_MB_Max_High = [1,1.0349631499754,1.04186520443559,1.03288552880502,1.02581927296345,1.02799987626366]

array_MB_Max_High = np.array(array_MB_Max_High)


array_MB_Max_error_high = [0,0.0177893657090097,0.010717210250488,0.0267172801485277,0.00973444181847139,0.0189425072731006 ]



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
p = pvalue_from_mean_se(mean1= 0.976455426818205, se1= 0.0115890589794831, n1= 3,   # control
                        mean2= 1.02799987626366, se2= 0.0189425072731006, n2= 3 )  # treatment
print(f"p = {p:.8f}")












#%%

#%%

print("Parameters for low concentration:", popt1)
print("Parameters for high concentration:", popt2)


#%%

residuals = array_MB_Max_Low - func(xdata, *popt1)
plt.scatter(xdata, residuals)
plt.axhline(0, color='gray', linestyle='--')
plt.title('Residuals')
plt.show()
