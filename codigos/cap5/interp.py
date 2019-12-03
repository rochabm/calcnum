# -*- coding: utf-8 -*-
"""
@author: Bernardo M. Rocha
"""

from numpy import linalg, array, zeros

# -----------------------------------------------------------------------------

def polyinterp(x,y):
    """
    Interpola os dados (x0,y0), ... , (xn,yn) resolvendo o sistema
    de equações associado com a matriz de Vandermonde.
    
    Entrada:
        - coordenadas x dos dados
        - coordenadas y dos dados
    
    Saida:
        - coeficientes c do polinomio interpolador
          p(x) = a0 + a1 x + a2 x^2 + ... + an x^n
    """
    n = len(x)
    A = zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = x[i]**j
            
    c = linalg.solve(A,y)
    return c

# -----------------------------------------------------------------------------    

def polyhorner(c,z):
    """
    Avalia o polinômio p(x) cujos coeficientes estao armazenados no vetor
    c no(s) ponto(s) dado(s) pelo argumento z.
    
    Entrada:
        - c coeficientes do polinomio
        - z pontos a avaliar o polinomio
    
    Saida:
        - valor do polinomio p(x) no ponto z, i.e., p(z)
    """
    n = len(c)
    b = c[-1]
    for i in range(n-2,-1,-1):
        b = c[i] + b * z
    return b

# -----------------------------------------------------------------------------
    
def lagrange(x,y,z):
    """
    Interpola e avalia o polinomio interpolador de grau n na forma de
    Lagrange em um conjunto de pontos. 

    Entrada:
	- x: coordenadas X dos dados (tamanho n+1)
        - y: coordenadas Y dos dados (tamanho n+1)
        - z: pontos que se deseja avaliar o polinomio (tamanho m)

    Saida:
	- s: valor do polinomio interpolador na forma de Lagrange avaliado
 	     nos pontos z=(z0, ... , zm)
    """
    z = array(z)
    n = len(z)
    s = zeros(n)
    
    for k in range(n):
        r = 0.0
        for i in range(len(x)):
            c = 1.0
            d = 1.0
            for j in range(len(x)):
                if (i != j):
                    c = c * (z[k] - x[j])
                    d = d * (x[i] - x[j])
            r = r + y[i] * (c/d)
        s[k] = r    
    return s

# -----------------------------------------------------------------------------

def difdiv(x,y):
    """
    Calcula coeficientes do polinomio na forma de Newton atraves
    do calculo das diferencas divididas:
           f[x0]
           f[x0,x1]
           f[x0,x1,x2]
           ...
           f[x0,...,xn]

    Entrada:
       - x: pontos x0, x1, ..., xn 
       - y: valores da funcao a ser interpolada avaliada em x.
            y0=f(x0), y1=f(x1), ..., yn=f(xn)

    Saida:
       - d: coeficientes do polinomio interpolador na forma de Newton  
    """
    n = len(x)-1
    d = y.copy()
    for k in range(1,n+1):
        for i in range(n,k-1,-1):
            d[i] = (d[i]-d[i-1])/(x[i]-x[i-k])    
    return d

# -----------------------------------------------------------------------------

def evalnewton(c, x, z):
    """
    Avalia polinomio na forma de Newton usando o algoritmo de Horner.

    Entrada:
       - c: coeficientes do polinomio na forma de Newton
       - x: coordenada x dos dados usados para interpolacao (x0,x1,...,xn)
       - z: ponto ou vetor de pontos para avaliar o polinomio

    Saida:
       - valor do polinomio P(x) no(s) ponto(s) z
    """
    n = len(x)-1
    r = c[n]
    z = array(z)
    for i in range(n-1,-1,-1):
        r = r * (z - x[i]) + c[i]
    return r

