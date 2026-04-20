#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:14:51 2025

@author: luis
"""

import pandas as pd
import matplotlib.pyplot as plt


x =  pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/wavelength.xlsx')
y0 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/0min.xlsx')
y4 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/4min.xlsx')
y8 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/8min.xlsx')
y12 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/12min.xlsx')
y16 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/16min.xlsx')
y20 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura2/Figura2b/20min.xlsx')


plt.plot(x, y0, color='green', label='0 min')
plt.plot(x, y4, color='b', label='4 min' )
plt.plot(x, y8, color='grey', label='8 min' )
plt.plot(x, y12, color='r', label='12 min' )
plt.plot(x, y16, color='brown', label='16 min' )
plt.plot(x, y20, color='lightseagreen', label='20 min' )

plt.axvline(x = 664, linestyle = 'dashed', color = 'black')

plt.xlabel('Wavelength [nm]', size=14)
plt.ylabel('Absorbance [UA]', size=14)
plt.title('Methylene blue + algae absorbance spectra', size=14)
plt.legend(loc ="upper left", fontsize=14)
plt.ylim(-.1,1.1)
plt.xlim(350,800)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Figure2b.png", dpi=1200, bbox_inches='tight')
plt.show()