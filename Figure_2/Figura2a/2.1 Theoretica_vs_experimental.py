#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 18:58:13 2025

@author: luis
"""

import pandas as pd
import matplotlib.pyplot as plt

x =  pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2a/wavelength.xlsx')
experimental = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2a/2aexp.xlsx')
theoretical = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2a/2a_theo.xlsx')



plt.plot(x, experimental, color='m', label='Experimental')
plt.plot(x, theoretical, color='orange', label='Theoretical' )


plt.axvline(x = 664, linestyle = 'dashed', color = 'black')

plt.xlabel('Wavelength [nm]', size=14)
plt.ylabel('Absorbance [UA]', size=14)
plt.title('Theoretical and experimental @ t=0 mins spectra', size=14)
plt.legend(loc ="upper left", fontsize=14)
plt.ylim(-.1,1.1)
plt.xlim(350,800)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Figure2a.png", dpi=1200, bbox_inches='tight')
plt.show()
