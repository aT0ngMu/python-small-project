import sys
import csv
import re

# read csv
with open('periodictable.csv', encoding='utf-8') as f:
    elementsCsvReader = csv.reader(f)
    elements = list(elementsCsvReader)

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

# find longest column
Longest_column = 0
for column in ALL_COLUMNS:
    if len(column) > Longest_column:
        Longest_column = len(column)


# pull all the elements into a data structure
ELEMENTS = {}
for line in elements:
    element = {
        'Atomic Number': line[0],
        'Symbol': line[1],
        'Element': line[2],
        'Origin of name': line[3],
        'Group': line[4],
        'Period': line[5],
        'Atomic weight': line[6] + ' u',  # atomic mass unit
        'Density': line[7] + ' g/cm^3',  # grams/cubic cm
        'Melting point': line[8] + ' K',  # kelvin
        'Boiling point': line[9] + ' K',  # kelvin
        'Specific heat capacity': line[10] + ' J/(g*K)',
        'Electronegativity': line[11],
        'Abundance in earth\'s crust': line[12] + ' mg/kg'
    }


    for key,value in element.items():
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)


    ELEMENTS[line[0]] = element
    ELEMENTS[line[1]] = element

while True:
    print('''            Periodic Table of Elements
  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
1 H                                                  He
2 Li Be                               B  C  N  O  F  Ne
3 Na Mg                               Al Si P  S  Cl Ar
4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
        Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
        Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print("Enter a symbol or atomic number to examine, or QUIT to quit.")

    enter = input(">").title()

    if enter == "Quit":
        sys.exit()

    if enter in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(Longest_column)
            print(f"{keyJustified} : {ELEMENTS[enter][key]}")
        input('Press Enter to continue...')

