from cmath import sqrt
import pandas as xls

table = xls.read_excel("2022.xlsx", sheet_name=None)

listSheets = ['A76','A95','A98']

sheetA = [
    list(table[listSheets[0]]['Амп']),
    list(table[listSheets[1]]['Амп']),
    list(table[listSheets[2]]['Амп'])
]
sheetAX = list(table['AX']['Амп1'])

def R(vector1, vector2):
    return sqrt(sum(((i1-i2)**2 for i1, i2 in zip(vector1, vector2)))).real

listR = [R(a, sheetAX) for a in sheetA]

print(f"List R: {listR}")

print(f"The shortest distance between the wind AX and {listSheets[listR.index(min(listR))]}: {min(listR)}")