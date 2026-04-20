#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:38:24 2022

@author: luis
"""


import pandas as pd
import matplotlib.pyplot as plt


x = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/wavelength_1a.xlsx')
y0 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/0min_1a.xlsx')
y4 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/4min_1a.xlsx')
y8 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/8min_1a.xlsx')
y12 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/12min_1a.xlsx')
y16 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/16min_1a.xlsx')
y20 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_a/20min_1a.xlsx')

#%%

x = x
y0 = y0
y4 = y4
y8 = y8
y12 = y12
y16 = y16
y20 = y20


plt.plot(x, y0, color='green', label='0 min')
plt.plot(x, y4, color='b', label='4 min' )
plt.plot(x, y8, color='grey', label='8 min' )
plt.plot(x, y12, color='r', label='12 min' )
plt.plot(x, y16, color='brown', label='16 min' )
plt.plot(x, y20, color='lightseagreen', label='20 min' )

plt.axvline(x = 664, linestyle = 'dashed', color = 'black')

plt.xlabel('Wavelength [nm]', size=14)
plt.ylabel('Absorbance [UA]', size=14)
plt.title('Methylene blue absorbance spectra', size=14)
plt.legend(loc ="upper left", fontsize=14)
plt.ylim(-.1,1.1)
plt.xlim(350,800)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Figure1a.png", dpi=1200, bbox_inches='tight')
plt.show()





