"""
Exemplo de funcao para aproximar exp(x) usando polinomio de Taylor
Calculo Numerico, Turma X, DCC, UFJF, 2019
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------

def exp_taylor(n, x):
    """
    Calcula uma aproximacao para exp(x) usando o polinomio de Taylor
    de grau n em torno de x=0. O polinomio de Taylor eh dado por:
   
        Pn(x) = 1 + x + x^2/2! + x^3/3! + ... + x^n/n!

    Exemplos:

        exp_taylor(5, 1.0) -> aproximacao para exp(1.0) com 5 termos  
        exp_taylor(9, 1.0) -> aproximacao para exp(1.0) com 9 termos  
        exp_taylor(9, 0.5) -> aproximacao para exp(0.5) com 9 termos     
    """
    fat = 1.0
    term = 1.0
    sum = term
    for i in range(1,n+1):
        fat = fat * i
        term = term * x
        sum = sum + term/fat
    return sum

# -----------------------------------------------------------------------------

def taylor(f, x0, x):
    """
    Calcula uma aproximacao para uma funcao f(x) qualquer usando o 
    polinomio de Taylor de grau n em torno de x=x0. A funcao f(x) deve
    ser fornecida como um vetor com os valores da funcao e suas
    derivadas. 

    Parametros:
       - f  - vetor com os valores da funcao e suas derivadas no ponto x0 
       - x0 - valor do ponto de referencia
       - x  - valor de x aonde se deseja calcular f(x)
       
    Exemplo:
    
    """
    n = len(f)
    if n == 0:
        print("Erro. Devem ser fornecidos os valores de f(x0), f'(x0), ...")
        return None
    h   = x - x0
    fat = 1.0
    termo = 1.0
    resultado = f[0]
    i = 1
    while i < n:
        fat = fat * i
        termo = termo * h
        resultado = resultado + (f[i]*termo)/fat
        i = i + 1
    return resultado


# -----------------------------------------------------------------------------

if __name__ == "__main__":

    print("Polinomios de Taylor\n")

    # Teste 1 - Testa aproximacao para exp(x)
    print("Aproximacao para exp(x)")
    n = 5
    x = 1.0
    ap = exp_taylor(n,x)
    ex = exp(x)
    er = abs(ex-ap)
    print(" Exato = %e" % ex)
    print(" Aprox = %e" % ap)
    print(" Erro  = %e\n" % er)

    # Teste 2 - Testa aproximacao para uma f(x) qualquer
    # Vamos usar f(x) = sin(x)
    # Vamos aproximar pn(0.5)
    # O vetor f deve conter [f(x0), f'(x0), f''(x0), ...]
    # Para esse caso, isto eh
    # [sin(x0), cos(x0), -sin(x0), -cos(x0),  sin(x0), cos(x0), -sin(x0), -cos(x0), ...]
    x0 = 0
    f = [sin(x0), cos(x0), -sin(x0), -cos(x0), sin(x0), cos(x0), -sin(x0), -cos(x0)]
    x = 2.5    
    ap = taylor(f,x0,x)
    ex = sin(x)
    er = abs(ex-ap)
    print("Aproximacao para sin(x)")
    print(" Exato = %e " % ex)
    print(" Aprox = %e " % ap)
    print(" Erro  = %e\n" % er)
    
    # Teste 3 - Grafico da aproximacao
    # Plot da aproximacao para exp(x) de -2 a 2
    x = np.linspace(-2,2,10000)
    y = np.exp(x)
    n = 3
    yy = exp_taylor(n,x)
    plt.plot(x,y,label="exp")
    plt.plot(x,yy,label="taylor")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Polinomio de Taylor")
    plt.legend(loc="best")
    plt.show()
    plt.savefig("teste1.png")
    
    
