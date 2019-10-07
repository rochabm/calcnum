# -----------------------------------------------------------------------------
# UFJF - DCC008 - Calculo Numerico
# Capitulo 4 - Solucao de Sistemas Lineares
# Bernardo M. Rocha
# -----------------------------------------------------------------------------

import sys
import numpy as np
from sistemas import *
from scipy.linalg import hilbert

def exemplo1():
    A = np.array([[5.,1,1],
                  [3,4,1],
                  [3,3,6]])
    b = np.array([[5.],[6],[0]])
    return A, b

def exemplo2():
    A = np.array([[4,0.24,-0.08],
                  [0.09,3,-0.15],
                  [0.04,-0.08,4]])
    b = np.array([[8.],[9],[20]])
    return A, b    

# -----------------------------------------------------------------------------

if __name__ == "__main__":

    #
    # Exemplo 1
    #
    print("\n\nEXEMPLO 1\n\n")
    A1,b1 = exemplo1()    
    print(A1)
    print(b1)
    x1 = gauss(A1,b1)
    print("Solucao")
    print(x1)
    print(A1)
    print(b1)


    #
    # Exemplo 2 (LU,Cholesky)
    #
    print("\n\nEXEMPLO 2\n\n")
    A2,b2 = exemplo1()
    decompLU(A2)
    print("Fatores L e U")
    print(A2)
    x2 = solveLU(A2,b2)
    print("Solucao")
    print(x2)
