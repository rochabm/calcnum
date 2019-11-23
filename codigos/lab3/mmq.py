"""
Codigo para Minimos Quadrados
Calculo Numerico, Turma X, DCC, UFJF, 2019
Bernardo M. Rocha
"""

from pylab import *
from math import acos,pi
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Metodos
# -----------------------------------------------------------------------------

#
# Implemente aqui a sua funcao para aproximacao de minimos quadrados
# Aproximacao polinomial
# Exercicio 1
#
def mmq(x, y):

    # x: vetor de dados x_i
    # y: vetor dos valores da funcao y_i = f(x_i) a ser aproximada
    # a funcao deve retornar os coeficientes de
    # g(x) = c0 phi_0 + ... + c_n phi_n

    return None    

# -----------------------------------------------------------------------------
       
if __name__ == "__main__":

    # --------------------
    # Teste
    # --------------------

    dados = np.loadtxt("ex1_dados.txt", delimiter=';')
    
    x = dados[:,0]
    y = dados[:,1]
    plt.plot(x,y,'o')
    plt.xlabel("x")
    plt.ylabel("y=f(x)")
    plt.show()
    plt.clf()

