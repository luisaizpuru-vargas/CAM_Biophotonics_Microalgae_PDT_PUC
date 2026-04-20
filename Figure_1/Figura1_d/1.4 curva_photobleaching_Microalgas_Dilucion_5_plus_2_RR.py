#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:15:34 2022

@author: luis
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:00:07 2022

@author: luis
"""

#%%


import matplotlib.pyplot as plt

import numpy as np
from PIL import Image
#from scipy.optimize import curve_fit
import scipy.optimize
from scipy.optimize import curve_fit


# Algae High Concentration 3 million

fluence = [0,11.28,22.56,33.84,45.12,56.4]
xdata = np.array(fluence)

array_Algae_3mill = [1,1.03618117349802,1.02482521606058,1.02980061852672,1.0485807322268,1.03688363934795]


array_Algae_3mill = np.array(array_Algae_3mill)
array_Algae_3mill_error = [0,0.0597065960023615,0.0399927696477605,0.0533944201542622,0.0532571633816181,0.0484893631556639]



## Algae Low concentration 2 million

array_Algae_2mill = [1,1.04674308709413,1.04862387778359,1.05384969889388,1.05250743204027,1.04627521301372]

array_Algae_2mill = np.array(array_Algae_2mill)


array_Algae_2mill_error = [0,0.0464168390855511,0.0388451248737854,0.0474061371380509,0.0498961251834327,0.0390126471253884]



n=6

def func(x, a, b,c, d):
    x = np.array(x)
    return a*np.exp(-b*x) + c*np.exp(-d*x) 


xdata = np.array(fluence)

array_Algae_3mill = array_Algae_3mill[0:n]
array_Algae_2mill = array_Algae_2mill[0:n]


popt1, pcov1 = curve_fit(func, xdata, array_Algae_3mill)
popt2, pcov2 = curve_fit(func, xdata, array_Algae_2mill)

#print(popt1)

#Create a finer grid for plotting
x_fit = np.linspace(min(xdata), 60, 1000)

plt.figure()

plt.plot(x_fit, func(x_fit, *popt1), color='g')
plt.errorbar(xdata, array_Algae_3mill ,yerr= array_Algae_3mill_error,  fmt='o', color='g', label= r'$3 \times 10^6$ algae/mL')


plt.plot(x_fit, func(x_fit, *popt2), color='limegreen')
plt.errorbar(xdata, array_Algae_2mill,yerr=array_Algae_2mill_error,  fmt ='o', color='limegreen', label= r'$2 \times 10^6$ algae/mL')



plt.xlabel(r'Fluence [$J/cm^2$]', size=14)
plt.ylabel('Normalized absorbance peak', size=14)
plt.title(r'$\it{C.\ reinhardtii}$ photobleaching', size=14)
plt.legend(loc ="lower left", fontsize=14)
plt.ylim(0.4,1.15)
plt.xticks(np.arange(0, 61, 10), fontsize=14)
plt.yticks(np.arange(0.4, 1.2, 0.1), fontsize=14)
plt.savefig("Figure1d_STAT.png", dpi=1200, bbox_inches='tight')

plt.show()