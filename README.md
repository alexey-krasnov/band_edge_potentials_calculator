<h1 align="center">band_edge_potentials_calculator</h1>
<p>
  <a href="https://twitter.com/AlekseiKrasnov4" target="_blank">
    <img alt="Twitter: AlekseiKrasnov4" src="https://img.shields.io/twitter/follow/AlekseiKrasnov4.svg?style=social" />
  </a>
</p>

> Calculation of the edge potentials of valence and conduction bands. The band edge potentials are in normalized hydrogen scale.

##  Prerequisites

This package requires:

- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [chemparse](https://pypi.org/project/chemparse/)

##  Theory

The band edge positions could be calculated according to the empirical formulas:

```
ECB = χ − Ee – 0.5Eg
EVB = ECB − Eg
```
Here, ECB and EVB are the valence band and conduction band edge potentials, respectively. Eg is the band gap. 
The Mulliken electronegativity of semiconductor χ can be calculated as the geometric mean of the absolute electronegativities of the constituent atoms. This is defined as the arithmetic mean of the electron affinities and atomic ionization. Ee is the energy of free electrons of the hydrogen scale ca. 4.5 eV.

## Usage

To start the calculation run:
```sh
band_potential_calc.py
```
The program asks about the type of band gap Eg: theoretical(DFT) or experimental. 
Next, write the semiconductor chemical formula and band gap value.

The program creates an Excel file with data in 4 columns: semiconductor formula, Band gap eV, Ecb eV, Evb eV in the sheet corresponding to theoretical(DFT) or experimental data.

## Author

👤 **Aleksei Krasnov**

* Website: [Ph.D. Aleksei Krasnov](https://www.researchgate.net/profile/Aleksei-Krasnov)
* Twitter: [@AlekseiKrasnov4](https://twitter.com/AlekseiKrasnov4)
* Github: [alexey-krasnov](https://github.com/alexey-krasnov)
* LinkedIn: [Aleksei Krasnov](https://linkedin.com/in/aleksei-krasnov-b53b2ab6)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/alexey-krasnov/band_edge_potentials_calculator/issues). 
