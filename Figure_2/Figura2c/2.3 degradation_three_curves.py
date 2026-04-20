#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:54:57 2025

@author: luis
"""

import matplotlib.pyplot as plt

import numpy as np
from PIL import Image
#from scipy.optimize import curve_fit
import scipy.optimize
from scipy.optimize import curve_fit

#%%

## MB Low Concentration

fluence = [0,
7.3536,
14.7072,
22.0608,
29.4144,
36.768
]

array_MB_Low = [1,
0.998918133119363,
1.01141682654721,
1.03119523961405,
0.984885598947597,
0.976455426818205
]


array_MB_Max_Low = np.array(array_MB_Low)
array_MB_Max_error_low = [0,
0.0121066598469283,
0.00344504142251467,
0.00649466558545263,
0.0165331723851125,
0.0115890589794831
]




#xdata = time_curve*60*47*10**-3

n=6

def func(x, a, b,c, d):
    x = np.array(x)
    return a*np.exp(-b*x) + c*np.exp(-d*x) 


xdata = np.array(fluence)

array_MB_Max_Low = array_MB_Max_Low [0:n]


popt1, pcov1 = curve_fit(func, xdata, array_MB_Max_Low )

#print(popt1)

# Create a finer grid for plotting
x_fit = np.linspace(min(xdata), 60, 1000)

#plt.figure(figsize=(11, 6))



plt.plot(x_fit, func(x_fit, *popt1), color='deepskyblue')
plt.errorbar(xdata, array_MB_Max_Low  ,yerr= array_MB_Max_error_low,  fmt='o', color='deepskyblue', label='30 μg/mL MB' )



#%%


# MB High Concentration

fluence = [0,
7.3536,
14.7072,
22.0608,
29.4144,
36.768,
]
xdata = np.array(fluence)

array_Algae_3mill = [1,
1.0349631499754,
1.04186520443559,
1.03288552880502,
1.02581927296345,
1.02799987626366
]


array_Algae_3mill = np.array(array_Algae_3mill)
array_Algae_3mill_error = [0,
0.0177893657090097,
0.010717210250488,
0.0267172801485277,
0.00973444181847139,
0.0189425072731006
]


n=6

def func(x, a, b,c, d):
    x = np.array(x)
    return a*np.exp(-b*x) + c*np.exp(-d*x) 


xdata = np.array(fluence)

array_Algae_3mill = array_Algae_3mill[0:n]


popt2, pcov2 = curve_fit(func, xdata, array_Algae_3mill)

#print(popt1)

#Create a finer grid for plotting
x_fit = np.linspace(min(xdata), 60, 1000)


plt.plot(x_fit, func(x_fit, *popt2), color='b')
plt.errorbar(xdata, array_Algae_3mill ,yerr= array_Algae_3mill_error,  fmt='o', color='b', label= '300 μg/mL MB ')



#%%

## Combination Algae + MB

array_Algae_3mill_MB_Low = [1,
0.98432825132582,
0.992585822185281,
0.967300688177481,
0.959752584378542,
0.928416792213966
]


array_Algae_3mill_MB_Low = np.array(array_Algae_3mill_MB_Low)
array_Algae_3mill_MB_Low_error = [0,
0.00354277289952832,
0.00305204838232493,
0.012302230819535,
0.00379169839176535,
0.00386447949234111

]




n=6

def func(x, a, b,c, d):
    x = np.array(x)
    return a*np.exp(-b*x) + c*np.exp(-d*x) 


xdata = np.array(fluence)

array_Algae_3mill_MB_Low  = array_Algae_3mill_MB_Low [0:n]


popt3, pcov3 = curve_fit(func, xdata, array_Algae_3mill_MB_Low)

#print(popt1)

#Create a finer grid for plotting
x_fit = np.linspace(min(xdata), 60, 1000)


plt.plot(x_fit, func(x_fit, *popt3), color='orange')
plt.errorbar(xdata, array_Algae_3mill_MB_Low  ,yerr= array_Algae_3mill_MB_Low_error,  fmt='o', color='orange', label=r'30 μg/mL MB + $10^6$ algae/mL')






plt.xlabel(r'Fluence [$J/cm^2$]', size=14)
plt.ylabel('Normalized absorbance peak', size=14)
plt.title('Methylene blue with and without algae photobleaching ', size=14)
plt.legend(loc ="lower left", fontsize=14)
plt.ylim(0.4,1.15)
plt.xlim(-2, 40)
plt.xticks(np.arange(0, 41, 10), fontsize=14)

plt.yticks(np.arange(0.4, 1.2, 0.1), fontsize=14)


# === VERTICAL SIGNIFICANCE BRACKET with adjustable vertical length ===
x_pos = fluence[2]                    # 29.4144 J/cm²
y_blue   = array_Algae_3mill[2]
y_orange = array_Algae_3mill_MB_Low[2]

bracket_x = x_pos + 1.6               # distance to the right of the points
cap_length = 1.8                      # width of the horizontal caps
padding = 0.01                       # <--- CHANGE THIS VALUE (larger = longer/taller bracket)

y_higher = max(y_blue, y_orange)
y_lower  = min(y_blue, y_orange)

y_top    = y_higher + padding         # extended top
y_bottom = y_lower  - padding         # extended bottom

# Vertical line (now adjustable length)
plt.plot([bracket_x, bracket_x], [y_bottom, y_top], color='black', lw=1.4)

# Horizontal caps at the new extended positions
plt.plot([bracket_x - cap_length/2, bracket_x + cap_length/2], [y_top,    y_top],    color='black', lw=1.4)
plt.plot([bracket_x - cap_length/2, bracket_x + cap_length/2], [y_bottom, y_bottom], color='black', lw=1.4)

# Asterisk BELOW the bracket
plt.text(bracket_x, y_bottom - 0.025, '*', 
         fontsize=22, ha='center', va='top', fontweight='bold', color='black')


# === VERTICAL SIGNIFICANCE BRACKET with adjustable vertical length ===
x_pos = fluence[4]                    # 29.4144 J/cm²
y_blue   = array_Algae_3mill[4]
y_orange = array_Algae_3mill_MB_Low[4]

bracket_x = x_pos + 1.6               # distance to the right of the points
cap_length = 1.8                      # width of the horizontal caps
padding = 0.01                       # <--- CHANGE THIS VALUE (larger = longer/taller bracket)

y_higher = max(y_blue, y_orange)
y_lower  = min(y_blue, y_orange)

y_top    = y_higher + padding         # extended top
y_bottom = y_lower  - padding         # extended bottom

# Vertical line (now adjustable length)
plt.plot([bracket_x, bracket_x], [y_bottom, y_top], color='black', lw=1.4)

# Horizontal caps at the new extended positions
plt.plot([bracket_x - cap_length/2, bracket_x + cap_length/2], [y_top,    y_top],    color='black', lw=1.4)
plt.plot([bracket_x - cap_length/2, bracket_x + cap_length/2], [y_bottom, y_bottom], color='black', lw=1.4)

# Asterisk BELOW the bracket
plt.text(bracket_x, y_bottom - 0.025, '**', 
         fontsize=22, ha='center', va='top', fontweight='bold', color='black')


# === VERTICAL SIGNIFICANCE BRACKET with adjustable vertical length ===
x_pos = fluence[5]                    # 29.4144 J/cm²
y_blue   = array_Algae_3mill[5]
y_orange = array_Algae_3mill_MB_Low[5]

bracket_x = x_pos + 1.6               # distance to the right of the points
cap_length = 1.8                      # width of the horizontal caps
padding = 0.01                       # <--- CHANGE THIS VALUE (larger = longer/taller bracket)

y_higher = max(y_blue, y_orange)
y_lower  = min(y_blue, y_orange)

y_top    = y_higher + padding         # extended top
y_bottom = y_lower  - padding         # extended bottom

# Vertical line (now adjustable length)
plt.plot([bracket_x, bracket_x], [y_bottom, y_top], color='black', lw=1.4)

# Horizontal caps at the new extended positions
plt.plot([bracket_x - cap_length/2, bracket_x + cap_length/2], [y_top,    y_top],    color='black', lw=1.4)
plt.plot([bracket_x - cap_length/2, bracket_x + cap_length/2], [y_bottom, y_bottom], color='black', lw=1.4)

# Asterisk BELOW the bracket
plt.text(bracket_x, y_bottom - 0.025, '*', 
         fontsize=22, ha='center', va='top', fontweight='bold', color='black')

plt.savefig("Fig2c.png", dpi=1200, bbox_inches='tight')
plt.show()



#%%

import numpy as np
from scipy import stats

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
p = pvalue_from_mean_se(mean1= 1.02799987626366, se1= 0.0189425072731006, n1= 3,   # control
                        mean2= 0.928416792213966, se2= 0.00386447949234111 , n2= 3 )  # treatment
print(f"p = {p:.8f}")

#%%


