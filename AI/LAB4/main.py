from cmath import sqrt
from matplotlib.pyplot import get
import pandas as xls
import numpy as np


A = 10
B = 0.01

table = xls.read_excel("2022.xlsx", sheet_name=None)

listSheets = ['A76','A95','A98']

sheetA = [
    list(table[listSheets[0]]['Амп']),
    list(table[listSheets[1]]['Амп']),
    list(table[listSheets[2]]['Амп'])
]
sheetAX = list(table['AX']['Амп1'])

def optimal_similarity(Ai, Ax):
    Ai = np.array(Ai)
    Ax = np.array(Ax)

    return A/(B+((Ax-Ai).T@(Ax-Ai))) 


listR = [optimal_similarity(r, sheetAX).real for r in sheetA]

print(f"Correlation coefficient list: {listR}\n")
print(f"The shortest distance between the wind AX and {listSheets[list(map(abs,listR)).index(max(list(map(abs,listR))))]}: {max(list(map(abs,listR)))}")