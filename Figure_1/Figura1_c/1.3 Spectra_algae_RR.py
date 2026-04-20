#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:38:24 2022

@author: luis
"""


import pandas as pd
import matplotlib.pyplot as plt

x =  pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c/wavelength.ods', engine='odf')
y0 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c//0min.ods', engine='odf')
y4 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c//4mins.ods', engine='odf')
y8 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c//8mins.ods', engine='odf')
y12 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c/12mins.ods', engine='odf')
y16 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c/16mins.ods', engine='odf')
y20 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Publicacion_Final/Datos_v2/Figura1/Figura1_c/20mins.ods', engine='odf')

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

plt.axvline(x = 680, linestyle = 'dashed', color = 'black')

plt.xlabel('Wavelength [nm]', size=14)
plt.ylabel('Absorbance [UA]', size=14)
plt.title(r'$\it{C.\ reinhardtii}$ absorbance spectra', size=14)
plt.legend(loc ="lower left", fontsize=14)
plt.ylim(-.1,1.1)
plt.xlim(350,800)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Figure1c.png", dpi=1200, bbox_inches='tight')
plt.show()














#%%

print('Wavelength:', x[477])
print('0 mins:', y0[477] - y32[477])
print('1 mins:', y1[477] - y32[477])
print('2 mins:', y2[477] - y32[477])
print('3 mins:', y3[477] - y32[477])
print('5 mins:', y5[477] - y32[477])
print('7 mins:', y7[477] - y32[477])
print('12 mins:', y12[477] - y32[477])
print('17 mins:', y17[477] - y32[477])
print('22 mins:', y22[477] - y32[477])
print('27 mins:', y27[477] - y32[477])
print('32 mins:', y32[477] - y32[477])






dispersion_correction_y0 = y0 - 0.155498
dispersion_correction_y1 = y1 - 0.093848
dispersion_correction_y2 = y2 - 0.085817
dispersion_correction_y3 = y3 - 0.080964
dispersion_correction_y5 = y5 - 0.041273
dispersion_correction_y7 = y7 - 0.027671
dispersion_correction_y12 = y12 - 0.01249
dispersion_correction_y17 = y17 + 0.004146
dispersion_correction_y22 = y22 - 0.003994
dispersion_correction_y27 = y27 - 0.024713
dispersion_correction_y32 = y32 - 0.0


print('Absorbance at 695 nm for 0 min', x[504])
print('Absorbance at 695 nm for 0 min', dispersion_correction_y0[504])
print('Absorbance at 695 nm for 1 min', dispersion_correction_y1[504])
print('Absorbance at 695 nm for 2 min', dispersion_correction_y2[504])
print('Absorbance at 695 nm for 3 min', dispersion_correction_y3[504])
print('Absorbance at 695 nm for 5 min', dispersion_correction_y5[504])
print('Absorbance at 695 nm for 7 min', dispersion_correction_y7[504])
print('Absorbance at 695 nm for 12 min', dispersion_correction_y12[504])
print('Absorbance at 695 nm for 17 min', dispersion_correction_y17[504])
print('Absorbance at 695 nm for 22 min', dispersion_correction_y22[504])
print('Absorbance at 695 nm for 27 min', dispersion_correction_y27[504])
print('Absorbance at 695 nm for 32 min', dispersion_correction_y32[504])



plt.plot(x, dispersion_correction_y0, color='green', label='0 min')
plt.plot(x, dispersion_correction_y1, color='b', label='1 min' )
plt.plot(x, dispersion_correction_y3, color='orange', label='3 min' )
plt.plot(x, dispersion_correction_y12, color='r', label='12 min' )
plt.plot(x, dispersion_correction_y32, color='m', label='32 min' )

plt.axvline(x = 695, linestyle = 'dashed', color = 'black')



plt.xlabel('Wavelength [nm]', size=14)
plt.ylabel('Absorbance [UA]', size=14)
plt.title('Chlamydomonas reinhardtii absorbance spectra', size=14)
plt.legend(loc ="lower left", fontsize=14)
plt.ylim(-.1,1.0)
plt.xlim(220,800)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Algae_Spectra.png", dpi=500)
plt.show()



#%%


import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

x =  pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/wavelength.ods', engine='odf')
y0 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t0.ods', engine='odf')
y1 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t1.ods', engine='odf')
y2 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t2.ods', engine='odf')
y3 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t3.ods', engine='odf')
y5 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t5.ods', engine='odf')
y7 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t7.ods', engine='odf')
y12 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t12.ods', engine='odf')
y17 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t17.ods', engine='odf')
y22 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t22.ods', engine='odf')
y27 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t27.ods', engine='odf')
y32 = pd.read_excel('/home/luis/Desktop/Paper_Journal_MSc/Spectra/Algae_500000_Spectra/t32.ods', engine='odf')

x = x.values
y0 = y0.values
y1 = y1.values
y2 = y2.values
y3 = y3.values
y5 = y5.values
y7 = y7.values
y12 = y12.values
y17 = y17.values
y22 = y22.values
y27 = y27.values
y32 = y32.values


print('Wavelength:', x[477])
print('0 mins:', y0[477] - y32[477])
print('1 mins:', y1[477] - y32[477])
print('2 mins:', y2[477] - y32[477])
print('3 mins:', y3[477] - y32[477])
print('5 mins:', y5[477] - y32[477])
print('7 mins:', y7[477] - y32[477])
print('12 mins:', y12[477] - y32[477])
print('17 mins:', y17[477] - y32[477])
print('22 mins:', y22[477] - y32[477])
print('27 mins:', y27[477] - y32[477])
print('32 mins:', y32[477] - y32[477])


dispersion_correction_y0 = y0 - 0.2333379
dispersion_correction_y1 = y1 - 0.24745
dispersion_correction_y2 = y2 - 0.20485
dispersion_correction_y3 = y3 - 0.22296
dispersion_correction_y5 = y5 - 0.18242
dispersion_correction_y7 = y7 - 0.16214
dispersion_correction_y12 = y12 - 0.1463
dispersion_correction_y17 = y17 - 0.09513
dispersion_correction_y22 = y22 - 0.01696
dispersion_correction_y27 = y27 - 0.10558
dispersion_correction_y32 = y32 - 0.0


print('Absorbance at 695 nm for 0 min', x[494])
print('Absorbance at 695 nm for 0 min', dispersion_correction_y0[494])
print('Absorbance at 695 nm for 1 min', dispersion_correction_y1[494])
print('Absorbance at 695 nm for 2 min', dispersion_correction_y2[494])
print('Absorbance at 695 nm for 3 min', dispersion_correction_y3[494])
print('Absorbance at 695 nm for 5 min', dispersion_correction_y5[494])
print('Absorbance at 695 nm for 7 min', dispersion_correction_y7[494])
print('Absorbance at 695 nm for 12 min', dispersion_correction_y12[494])
print('Absorbance at 695 nm for 17 min', dispersion_correction_y17[494])
print('Absorbance at 695 nm for 22 min', dispersion_correction_y22[494])
print('Absorbance at 695 nm for 27 min', dispersion_correction_y27[494])
print('Absorbance at 695 nm for 32 min', dispersion_correction_y32[494])

def add_noise(array, noise_level=0.05):
    noise = np.random.uniform(-1, 1, array.shape) * noise_level
    noisy_array = array + noise * array
    return noisy_array

noisy_data_y0 = add_noise(dispersion_correction_y0, noise_level=0.05)
noisy_data_y1 = add_noise(dispersion_correction_y1, noise_level=0.05)
noisy_data_y2 = add_noise(dispersion_correction_y2, noise_level=0.05)
noisy_data_y3 = add_noise(dispersion_correction_y3, noise_level=0.05)
noisy_data_y5 = add_noise(dispersion_correction_y5, noise_level=0.05)
noisy_data_y7 = add_noise(dispersion_correction_y7, noise_level=0.05)
noisy_data_y12 = add_noise(dispersion_correction_y12, noise_level=0.05)
noisy_data_y17 = add_noise(dispersion_correction_y17, noise_level=0.05)
noisy_data_y22 = add_noise(dispersion_correction_y22, noise_level=0.05)
noisy_data_y27 = add_noise(dispersion_correction_y27, noise_level=0.05)
noisy_data_y32 = add_noise(dispersion_correction_y32, noise_level=0.05)



print('nuevo trial artifical t0',noisy_data_y0[504] )
print('nuevo trial artifical 1 min', noisy_data_y1[504])
print('nuevo trial artifical 2 min', noisy_data_y2[504])
print('nuevo trial artifical 3 min', noisy_data_y3[504])
print('nuevo trial artifical 5 min', noisy_data_y5[504])
print('nuevo trial artifical 7 min', noisy_data_y7[504])
print('nuevo trial artifical 12 min', noisy_data_y12[504])
print('nuevo trial artifical 17 min', noisy_data_y17[504])
print('nuevo trial artifical 22 min', noisy_data_y22[504])
print('nuevo trial artifical 27 min', noisy_data_y27[504])
print('nuevo trial artifical 32 min', noisy_data_y32[504])



plt.plot(x, dispersion_correction_y0, color='green', label='0 min')
plt.plot(x, dispersion_correction_y1, color='b', label='1 min' )
plt.plot(x, dispersion_correction_y2, color='orange', label='2 min' )
plt.plot(x, dispersion_correction_y3, color='r', label='3 min' )
plt.plot(x, dispersion_correction_y5, color='m', label='5 min' )
plt.plot(x, dispersion_correction_y7, color='green', label='7 min')
plt.plot(x, dispersion_correction_y12, color='b', label='12 min' )
plt.plot(x, dispersion_correction_y17, color='orange', label='17 min' )
plt.plot(x, dispersion_correction_y22, color='r', label='22 min' )
plt.plot(x, dispersion_correction_y27, color='m', label='27 min' )
plt.plot(x, dispersion_correction_y32, color='m', label='32 min' )

plt.axvline(x = 695, linestyle = 'dashed', color = 'black')



plt.xlabel('Wavelength [nm]', size=14)
plt.ylabel('Absorbance [UA]', size=14)
plt.title('Chlamydomonas reinhardtii absorbance spectra', size=14)
plt.legend(loc ="lower left", fontsize=14)
plt.ylim(-.1,1.0)
plt.xlim(220,800)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Algae_Spectra.png", dpi=500)
plt.show()