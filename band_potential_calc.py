# -*- coding: UTF-8 -*-
import pandas as pd
import chemparse


# Read data from the csv file in the current directory
"""Database based on the article: R.G. Pearson, Absolute electronegativity and hardness: application to inorganic 
chemistry,Inorg. Chem. 27 (1988) 734–740. https://doi.org/10.1021/ic00277a030."""
df = pd.read_csv('pearson1988.csv', sep=',', index_col='Element')

"""Database based on the two alternative sources"
https://chem.libretexts.org/Ancillary_Materials/Reference/Reference_Tables/Atomic_and_Molecular_Properties/A7%3A_Electron_Affinities
https://environmentalchemistry.com/yogi/periodic/1stionization.html"""
# df = pd.read_csv('table_energies_of_elements.csv', sep=',', index_col='Element')

# We have already calculated electronegativity of elements and save it to csv file.
# If you wish to change data, uncomment line below, calculate again and save as csv file.
# df['Electronegativity'] = (df['Electron affinity (eV)'] + df['1st Ionization Potential (eV)']) / 2
# df.to_csv('pearson1988.csv', sep=',', index_label='Element')

def get_formula():
    """Get formula of semiconductor from user input"""
    return input("Please, enter a semiconductor formula: ")


def parse_chem_formula(composition):
    """Parse semiconductor formula and return chemical composition as dictionary {'element': index, etc.}"""
    return chemparse.parse_formula(composition)


def get_eg():
    """Get band gap value of the semiconductor form user"""
    return float(input("Please, enter the band gap value of the semiconductor: "))


def calc_electronegativity():
    """Calculate semiconductor electronegativity"""
    geom_mean = 1
    ind_sum = 0
    for el, ind in formula_as_dict.items():
        geom_mean *= df['Electronegativity'][el.title()] ** ind
        ind_sum += ind
    return geom_mean ** (1 / ind_sum)


def calc_band_potentials(eg):
    """Calculate band edge potentials in normalized hydrogen scale, eV"""
    e_cb = round(semicond_electronegativity - 4.5 - 0.5 * eg, 2)
    e_vb = round(eg + e_cb, 2)
    return e_cb, e_vb


def save_database():
    """Save processed data as database in the csv file.
    Make DataFrame for output information of the processed semiconductors"""
    col_names = ['Band gap, eV', 'Ecb, eV', 'Evb, eV']
    df_out = pd.DataFrame(columns=col_names)
    return df_out


semicond_dict = {'BaTaO2N': 1.49, 'BaTa0.5Al0.5O2N': 1.61, 'BaTa0.5Mg0.5O2N': 2.01, 'BaTa0.5Al0.375Mg0.125O2N': 1.36}
# semicond_dict = {}

df_out = save_database()
if semicond_dict:
    for semicond, band in semicond_dict.items():
        formula_as_dict = parse_chem_formula(semicond)
        semicond_electronegativity = calc_electronegativity()
        e_cb, e_vb = calc_band_potentials(band)
        df_out.loc[semicond] = [band, e_cb, e_vb]
else:
    semiconductor = get_formula()
    formula_as_dict = parse_chem_formula(semiconductor)
    band_gap = get_eg()
    semicond_electronegativity = calc_electronegativity()
    e_cb, e_vb = calc_band_potentials(band_gap)
    df_out.loc[semiconductor] = [band_gap, e_cb, e_vb]
print(df_out)
df_out.to_csv('out_data.csv')


# print(f"{semiconductor} has band gap {band_gap} ev, Ecb is {round(e_cb, 2)} eV, and Evb is {round(e_vb, 2)} eV")

# Make DataFrame for output information of the processed semiconductors
# col_names = ['Band gap, eV', 'Ecb, eV', 'Evb, eV']
# df_out = pd.DataFrame(columns=col_names)
# df_out.loc[semiconductor] = [band_gap, e_cb, e_vb]
# print(df_out)
# df_out.to_csv('out_data.csv')

# To check semiconductors from list, for QA tests
# semiconds = {'BaTaO2N': 1.49, 'BaTa0.5Al0.5O2N': 1.61, 'BaTa0.5Mg0.5O2N': 2.01, 'BaTa0.5Al0.375Mg0.125O2N': 1.36}
# col_names = ['Band gap, eV', 'Ecb, eV', 'Evb, eV']
# df_out = pd.DataFrame(columns=col_names)
# for semicond, band in semiconds.items():
#     formula_as_dict = parse_chem_formula(semicond)
#     semicond_electronegativity = get_electronegativity()
#     e_cb, e_vb = get_band_potentials(band)
#     df_out.loc[semicond] = [band, e_cb, e_vb]
# print(df_out)
# df_out.to_csv('out_data.csv')