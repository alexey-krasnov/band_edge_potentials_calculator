# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import chemparse

#"""Read data from the xlsx file in the current directory.
 #   Please, check the input file."""

df = pd.read_csv('table_energies_of_elements.csv', sep=',', index_col='Element')
print(df['Electron affinity (eV)'])
df['Electronegativity'] = (df['Electron affinity (eV)'] + df['1st Ionization Potential (eV)']) / 2
print(df, df.info())
# semiconductor = input("Please, enter a semiconductor formula: ")
semicond_list = ['BaTaO2N', 'BaTa0.5Al0.5O2N', 'BaTa0.5Mg0.5O2N', 'BaTa0.5Al0.375Mg0.125O2N']
for i in semicond_list:
    formula_as_dict = chemparse.parse_formula(i)
    print(formula_as_dict)
    geom_mean = 1
    ind_sum = 0
    for el, ind in formula_as_dict.items():
        geom_mean *= df['Electronegativity'][el.title()] ** ind
        ind_sum += ind
    semicond_electronegativity = geom_mean ** (1 / ind_sum)
    print(semicond_electronegativity)
# df.to_csv('table_energies_of_elements.csv')