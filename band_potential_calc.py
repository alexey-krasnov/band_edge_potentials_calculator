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

# We have already calculated electronegativity of elements and save it initial csv file.
# If you wish to change data, uncomment line below, calculate again, and save as date csv file.
# df['Electronegativity'] = (df['Electron affinity (eV)'] + df['1st Ionization Potential (eV)']) / 2
# df.to_csv('pearson1988.csv', sep=',', index_label='Element')

def check_data_type():
    """Check if data to precess is theoretical(DFT) or experimental"""
    type = input("Chose type of data needs to be processed: theoretical(DFT) or experimental.\n"
                 "Chose 't' if data is theoretical(DFT) or 'e' if data is experimental ")
    if type.lower() == 't':
        return 'Theoretical(DFT)'
    elif type.lower() == 'e':
        return "Experimental"
    else:
        print("Warning! The input data should be only letters 't' or 'e'.")


def get_formula():
    """Get formula of semiconductor from user input and return it"""
    return input("Please, enter a semiconductor formula: ")


def parse_formula(formula):
    """Parse semiconductor formula and return chemical composition as dictionary {'element': index, etc.}"""
    return chemparse.parse_formula(formula)


def calc_electronegativity(formula):
    """Calculate semiconductor electronegativity"""
    geom_mean = 1
    ind_sum = 0
    formula_as_dict = parse_formula(formula)
    for el, ind in formula_as_dict.items():
        geom_mean *= df['Electronegativity'][el.title()] ** ind
        ind_sum += ind
    return geom_mean ** (1 / ind_sum)


def get_direct_indirect():
    """Ask user about semiconductor type: direct or indirect"""
    type = input("Chose the semiconductor type: direct or indirect.\n"
                 "Chose 'd' if the semiconductor is direct or 'i' if the semiconductor is indirect.")
    if type.lower() == 'd':
        return 'direct'
    elif type.lower() == 'i':
        return "indirect"
    else:
        print("Warning! The input data should be only letters 'd' or 'i'.")


def get_eg(type='direct'):
    """Get band gap value of the semiconductor from user"""
    e_g = input(f"Please, enter the {type} band gap value of the semiconductor: ")
    return float(e_g)


def calc_band_potentials(formula, type='direct'):
    """Calculate band edge potentials in normalized hydrogen scale, eV"""
    e_g = get_eg(type)
    electronegativity = calc_electronegativity(formula)
    e_cb = round(electronegativity - 4.5 - 0.5 * e_g, 2)
    e_vb = round(e_g + e_cb, 2)
    return e_g, e_cb, e_vb


def make_df():
    """Make DataFrame for output information of the processed semiconductors"""
    col_names = ['Direct band gap, eV',
                 'Ecb, eV',
                 'Evb, eV',
                 'Indirect band gap, eV',
                 'Ecb, eV',
                 'Evb, eV',]
    df = pd.DataFrame(columns=col_names)
    return df


def save_database(df, semiconductor, data_type, e_g_dir, e_cb_dir, e_vb_dir,
                  e_g_indir=None, e_cb_indir=None, e_vb_indir=None):
    """Save processed data as database in the csv file."""
    df.loc[semiconductor] = [e_g_dir, e_cb_dir, e_vb_dir, e_g_indir, e_cb_indir, e_vb_indir]
    df.to_excel('out_data.xlsx', sheet_name=data_type)


if __name__ == "__main__":
    df_out = make_df()
    data_type = check_data_type()
    semiconductor = get_formula()
    type_semiconductor = get_direct_indirect()
    # For direct band gap
    e_g_dir, e_cb_dir, e_vb_dir = calc_band_potentials(semiconductor)
    # For indirect band gap type we should calculate data for indirect and direct Eg
    if type_semiconductor == 'indirect':
        e_g_indir, e_cb_indir, e_vb_indir = calc_band_potentials(semiconductor, type_semiconductor)
    save_database(df_out, semiconductor, data_type, e_g_dir, e_cb_dir, e_vb_dir, e_g_indir, e_cb_indir, e_vb_indir)

