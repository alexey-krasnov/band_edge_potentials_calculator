# -*- coding: UTF-8 -*-
import pandas as pd
import chemparse


# Read data from the csv file in the current directory
df = pd.read_csv('table_energies_of_elements.csv', sep=',', index_col='Element')
# We have already calculated electronegativity of elements and save it to csv file.
# If you wish to change data, uncomment line below and calculate again.
# df['Electronegativity'] = (df['Electron affinity (eV)'] + df['1st Ionization Potential (eV)']) / 2

def get_formula():
    """Get formula of semiconductor from user input"""
    semiconductor = input("Please, enter a semiconductor formula: ")
    return semiconductor


def parse_chem_formula(semiconductor):
    """Parse semiconductor formula and return as dictionary {'element': index, etc}"""
    formula_as_dict = chemparse.parse_formula(semiconductor)
    return formula_as_dict


def get_eg():
    """Get band gap value of the semiconductor form user"""
    band_gap = float(input("Please, enter the band gap value of the semiconductor: "))
    return band_gap


def get_electronegativity():
    """Calculate semiconductor electronegativity"""
    geom_mean = 1
    ind_sum = 0
    for el, ind in formula_as_dict.items():
        geom_mean *= df['Electronegativity'][el.title()] ** ind
        ind_sum += ind
    semicond_electronegativity = geom_mean ** (1 / ind_sum)
    return semicond_electronegativity


def get_band_potentials(eg):
    e_cb = semicond_electronegativity - 4.5 - 0.5 * eg
    e_vb = eg + e_cb
    return e_cb, e_vb


semiconductor = get_formula()
formula_as_dict = parse_chem_formula(semiconductor)
band_gap = get_eg()
semicond_electronegativity = get_electronegativity()
e_cb, e_vb = get_band_potentials(band_gap)

# print(f"{semiconductor} has band gap {band_gap} ev, Ecb is {round(e_cb, 2)} eV, and Evb is {round(e_vb, 2)} eV")

# Make DataFrame for output information of the processed semiconductors
# col_names = ['Band gap, eV', 'Ecb, eV', 'Evb, eV']
# df_out = pd.DataFrame(columns=col_names)
# df_out.loc[semiconductor] = [band_gap, e_cb, e_vb]
# print(df_out)
# df_out.to_csv('out_data.csv')

# To check semiconductors from list, for QA tests
semiconds = {'BaTaO2N': 1.49, 'BaTa0.5Al0.5O2N': 1.61, 'BaTa0.5Mg0.5O2N': 2.01, 'BaTa0.5Al0.375Mg0.125O2N': 1.36}
col_names = ['Band gap, eV', 'Ecb, eV', 'Evb, eV']
df_out = pd.DataFrame(columns=col_names)
for semicond, band in semiconds.items():
    formula_as_dict = parse_chem_formula(semicond)
    geom_mean = 1
    ind_sum = 0
    for el, ind in formula_as_dict.items():
        geom_mean *= df['Electronegativity'][el.title()] ** ind
        ind_sum += ind
    semicond_electronegativity = geom_mean ** (1 / ind_sum)
    e_cb = semicond_electronegativity - 4.5 - 0.5 * band
    e_vb = band + e_cb
    df_out.loc[semicond] = [band, e_cb, e_vb]
print(df_out)
df_out.to_csv('out_data.csv')