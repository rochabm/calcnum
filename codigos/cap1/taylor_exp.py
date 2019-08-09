"""
DCC008 - Calculo Numerico
Cap.1. Exemplo: Taylor para exp(x)
"""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from math import exp

def exp_taylor(n,x):
    soma = 0.0
    for i in range(n+1):
        termo = x**i / factorial(i)
        soma = soma + termo
    return soma

def exp_taylor2(n,x):
    fat = 1
    termo = 1.0
    soma = termo
    for i in range(1,n+1):
        fat = fat * i
        termo = termo * x
        soma = soma + termo/fat
    return soma

if __name__ == "__main__":

    # ponto
    x = 1.0

    # valor exato
    ex = exp(x)

    # valor aproximado
    e1 = exp_taylor2(1,x)
    e2 = exp_taylor2(2,x)
    e3 = exp_taylor2(3,x)
    e7 = exp_taylor2(7,x)
    
    print("exp(1)  = %e" % (ex))
    print("taylor1 = %e \t erro = %e" % (e1, abs(e1-ex)))
    print("taylor2 = %e \t erro = %e" % (e2, abs(e2-ex)))
    print("taylor3 = %e \t erro = %e" % (e3, abs(e3-ex)))
    print("taylor7 = %e \t erro = %e" % (e7, abs(e7-ex)))
    
    # graficos
    xx = np.linspace(-2,2,1000)
    yy = exp(xx)

    yy1 = np.zeros(1000)
    for i in range(1000):
        yy1[i] = exp_taylor(1,xx[i])

    yy2 = np.zeros(1000)
    for i in range(1000):
        yy2[i] = exp_taylor(1,xx[i])

    plt.plot(xx,yy,label="exp(x)")
    plt.plot(xx,yy1,label="taylor1")
    plt.show()
