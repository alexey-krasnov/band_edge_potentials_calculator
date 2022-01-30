# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import chemparse


# Read data from the csv file in the current directory
df = pd.read_csv('table_energies_of_elements.csv', sep=',', index_col='Element')
# We have already calculated electronegativity of elements and save it to csv file.
# If you wish to change data, uncomment line below and calculate again.
# df['Electronegativity'] = (df['Electron affinity (eV)'] + df['1st Ionization Potential (eV)']) / 2

print(df, df.info())
semiconductor = input("Please, enter a semiconductor formula: ")
formula_as_dict = chemparse.parse_formula(semiconductor)
print(formula_as_dict)

geom_mean = 1
ind_sum = 0
for el, ind in formula_as_dict.items():
    geom_mean *= df['Electronegativity'][el.title()] ** ind
    ind_sum += ind
semicond_electronegativity = geom_mean ** (1 / ind_sum)

print(semicond_electronegativity)
band_gap = float(input("Please, enter the band gap value of the semiconductor: "))
e_cb = semicond_electronegativity - 4.5 - 0.5 * band_gap
e_vb =band_gap + e_cb
print(f"{semiconductor} has band gap {band_gap} ev, Ecb is {round(e_cb, 2)} eV, and Evb is {round(e_vb, 2)} eV")
# df.to_csv('table_energies_of_elements.csv')

# To chekc semiconductors from list, for QA tests
# semicond_list = ['BaTaO2N', 'BaTa0.5Al0.5O2N', 'BaTa0.5Mg0.5O2N', 'BaTa0.5Al0.375Mg0.125O2N']
# for i in semicond_list:
#     formula_as_dict = chemparse.parse_formula(i)
#     print(formula_as_dict)
#     geom_mean = 1
#     ind_sum = 0
#     for el, ind in formula_as_dict.items():
#         geom_mean *= df['Electronegativity'][el.title()] ** ind
#         ind_sum += ind
#     semicond_electronegativity = geom_mean ** (1 / ind_sum)
#     print(semicond_electronegativity)
