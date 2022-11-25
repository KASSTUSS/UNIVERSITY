import numpy as np
import random
import math
import matplotlib.pyplot as plt

def showPlot(res, Range, origin, weight, title):
    plt.plot(
        [origin*(-1), origin], 
        [0, 0], 
        color='gray', 
        linewidth = 0.2)
    plt.plot( 
        [0, 0],
        [origin*(-1), origin], 
        color='gray', 
        linewidth = 0.2)
    plt.plot(
        [i*weight for i in range(Range[0], Range[1]+1)], 
        res, 
        color='red', 
        linewidth = 2)
    plt.axis(
        [
            Range[0]*(weight+0.5), 
            Range[1]*(weight+0.5), 
            min(res)-max(res)*0.1, 
            max(res)*1.1
        ])
    plt.title(title)
    plt.show()

class Neyron:
    def __init__(self, X, w=0) -> None:
        self.X = [i for i in X]
        self.W = [w if w != 0 else random.random() for i in range(len(X))]
        self.NET = [x*w for x, w in zip(self.X, self.W)]

    def linearFunction(self, k):
        return [i*k for i in self.NET]
    
    def logistFunction(self, k):
        return [1/(1+math.exp(k*i*(-1))) for i in self.NET]
    
    def porogFunction(self, k):
        return [0 if (i<k) else 1 for i in self.NET]


pn = Neyron([i for i in range(-30, 31)], w=1.5)

# Обзорный персептрон и графики
showPlot(pn.porogFunction(-10), [-30, 30], 100, 1.5, 'Пороговая функция активации (обзор)')
showPlot(pn.linearFunction(0.9), [-30, 30], 100, 1.5, 'Линейная функция активации (обзор)')
showPlot(pn.logistFunction(0.1), [-30, 30], 100, 1.5, 'Логистическая функция активации (обзор)')

# Задание 1
showPlot(pn.porogFunction(0), [-30, 30], 100, 1.5, 'Пороговая функция активации (задание 1, k=0)')
showPlot(pn.porogFunction(15), [-30, 30], 100, 1.5, 'Пороговая функция активации (задание 1, k=15)')
showPlot(pn.linearFunction(5), [-30, 30], 100, 1.5, 'Линейная функция активации (задание 1, k=5)')
showPlot(pn.linearFunction(1), [-30, 30], 100, 1.5, 'Линейная функция активации (задание 1, k=1)')
showPlot(pn.logistFunction(0.1), [-30, 30], 100, 1.5, 'Логистическая функция активации (задание 1, k=0.1)')
showPlot(pn.logistFunction(1.5), [-30, 30], 100, 1.5, 'Логистическая функция активации (задание 1, k=1.5)')
showPlot(pn.logistFunction(3), [-30, 30], 100, 1.5, 'Логистическая функция активации (задание 1, k=3)')


def Perceptron(count:int, weight:list, xRange:int, yRange:int):
    k = (-1)*weight[0]/weight[1]

    inputX = [random.uniform(int(-0.5*xRange), int(0.5*xRange)) for i in range(count)]
    inputY = [random.uniform(int(-0.5*yRange), int(0.5*yRange)) for i in range(count)]

    summer = [(i*weight[0]+j*weight[1]) for i, j in zip(inputX, inputY)]

    class1 = [[],[]]
    class2 = [[],[]]

    for i in range(count):
        if (summer[i] >= 0):
            class1[0].append(inputX[i])
            class1[1].append(inputY[i])
        else:
            class2[0].append(inputX[i])
            class2[1].append(inputY[i])

    x1:list = [i for i in range(int(-0.5*xRange), int(0.5*xRange), 1)]
    x2:list = [i*k for i in x1]
    plt.plot(
        x1, x2, 
        color='gray', 
        linewidth = 1)
    plt.plot(
        [int(-0.5*xRange), int(0.5*xRange)], 
        [0, 0], 
        color='gray', 
        linewidth = 0.2)
    plt.plot( 
        [0, 0], 
        [int(-0.5*xRange), int(0.5*xRange)], 
        color='gray', 
        linewidth = 0.2)
    
    plt.scatter(class1[0], class1[1], s=5, color='blue')
    plt.scatter(class2[0], class2[1], s=5, color='red')

    plt.show()

Perceptron(count=100,weight=[1,10], xRange=20, yRange=20)
Perceptron(count=75,weight=[1,3], xRange=20, yRange=20)
Perceptron(count=150,weight=[0.3,-1], xRange=20, yRange=20)