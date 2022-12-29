import numpy as np
import math

DIM = 10 # число нейронов
NUM_EPOCHS = 10000 # количество эпох
ALPHA = 0.0025 # скорость обучения

def logistFunction(p): # активационная функция
    return 1/(1+math.exp((-1)*p))

def getAbsoluteErr(t:list, y:list): # получить список абсолютных погрешностей
    absoluteErr = [abs(ti-yi) for ti, yi in zip(t,y)]
    return absoluteErr

def getRelativeErr(absErr:list, maxT): # получить список относительных погрешностей
    relativeErr = [absI/maxT for absI in absErr]
    return relativeErr

def getErr(y:list, t:list):
    errList = [(yi-ti) for yi,ti in zip(y,t)]
    return errList

p = np.random.rand(DIM) # входные сигналы
t = np.random.rand(DIM) # желаемые выходные сигналы
w = np.random.rand(DIM, DIM) # инициализируем веса

net = p @ w # аргумент для функции активации
y0 = [logistFunction(i) for i in net] # реальный выход до обучения

for _ in range(NUM_EPOCHS):
    net = p @ w # аргумент для функции активации
    y = [logistFunction(i) for i in net] # реальный выход

    E = getErr(y, t)

    for yi in range(DIM):
        for pi in range(DIM):
            w[pi][yi] = w[pi][yi] - ALPHA*E[yi]*p[pi] # подстройка весов

net = p @ w  # аргумент для функции активации
y1 = [logistFunction(i) for i in net]  # реальные выход

E = getErr(y1, t)

listAbsErr = getAbsoluteErr(t, y1)
listRelErr = getRelativeErr(listAbsErr,np.max(t))

maxAbsErr = np.max(listAbsErr)
maxRelErr = np.max(listRelErr)

print(f'\n\n\np  - входные сигналы(заданные случайно)\nt  - желаемые выходные сигналы(заданные случайно)\ny1 - реальные выходные сигналы(полученные "обученной" нейросетью)\ny0 - реальные выходные сигналы(полученные не "обученной" нейросетью)\n')

print(f' \t p\t\t\t  t\t\t\t  y1\t\ty0\n______________________________________________\n')
for i in range(DIM):
    print(f'{i+1}\t{ format(float(p[i]), ".3f") }\t|\t{format(float(t[i]), ".4f")}\t|\t{format(float(y1[i]), ".4f")}\t|\t{format(float(y0[i]), ".3f")}')
print(f'\n')


print(f'\n\n\nabsErr  - абсолютная погрешность\nrelErr  - относительная погрешность\n')

print(f'\t  absErr\t\t   relErr\n________________________________\n')
for i in range(DIM):
    print(f'{i+1}\t{ format(float(listAbsErr[i]), ".9f") }\t|\t{format(float(listRelErr[i]), ".9f")}')
print(f'\n')

print(f'Максимальная относительная погрешность вычисления: {format(float(maxRelErr*100), ".3f")}%')