from cmath import sqrt
from matplotlib.pyplot import get
import pandas as xls

table = xls.read_excel("2022.xlsx", sheet_name=None)

listSheets = ['A76','A95','A98']

sheetA = [
    list(table[listSheets[0]]['Амп']),
    list(table[listSheets[1]]['Амп']),
    list(table[listSheets[2]]['Амп'])
]
sheetAX = list(table['AX']['Амп1'])

def getM(vector):
    return sum(vector)/len(vector)

def getK(vector1, vector2):
    Mv1 = getM(vector1)
    Mv2 = getM(vector2)
    
    return sum([(i1-Mv1)*(i2-Mv2) for i1,i2 in zip(vector1,vector2)])/len(vector1)

def getSigma(vector):
    Mv = getM(vector)

    return sqrt(sum([(i-Mv)**2 for i in vector])/len(vector))

def corr(vector1, vector2):
    return getK(vector1, vector2)/(getSigma(vector1)*getSigma(vector2))

listR = [corr(r, sheetAX).real for r in sheetA]

print(f"Correlation coefficient list: {listR}\n")

print(f"The shortest distance between the wind AX and {listSheets[listR.index(max(listR))]}: {max(listR)}")