"""
Exemplo de funcao para aproximar exp(x) usando polinomio de Taylor
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

def bisecao(f,a,b,tol=1e-8,maxit=100):
    """
    Essa funcao implementa o metodo da Biseccao que encontra uma raiz da 
    funcao f no intervalo [a,b] com uma precisao tal que |f(x)| < tol.
    """
    print("\nMETODO DA BISECAO")
    if (f(a)*f(b) > 0):
        print("Nao ha garantias de que existe raiz nesse intervalo.")
        return None
    x = a
    k = 0
    for k in range(maxit):    
        x = (a+b)/2
        print("%d %e %e" % (k,x,f(x)))

        if (abs(f(x)) < tol):
            return x
        
        if(f(a)*f(x) < 0):
            b = x
        else:
            a = x           
        k = k + 1       
    return x

# -----------------------------------------------------------------------------

def pontofixo(phi,x,tol=1e-8,maxit=100):
    """
    Essa funcao implementa o metodo do Ponto Fixo. Recebe como
    parametros a funcao f que se deseja encontrar a raiz, a
    funcao de iteracao phi, uma aproximacao inicial x e
    ainda a precisao tol e numero maximo de iteracoes maxit.
    """
    print("\nMETODO DO PONTO FIXO")
    x0 = x
    for k in range(maxit):
        x1 = phi(x0)

        print(" %d %e %e" % ( k, x1, abs(x1-x0) ))

        if (abs( x1 - x0 ) <= tol):
            return x1
        x0 = x1

    print("Numero maximo de iteracoes excedido")
    return None

# -----------------------------------------------------------------------------

def falsaposicao(f,a,b,tol=1e-8,maxit=100):

    print("\nMETODO DA FALSA POSICAO")

    if ( f(a) * f(b) > 0 ):
        print('Nao ha garantias de raiz no intervalo dado')
        return None
    xold = b
    for k in range(maxit):
        fa = f(a), f(b)
        fb = f(b)
        x = (a*fb - b*fa)/(fb-fa)
        if (abs(x-xold) < tol):
            return x
        print(" %d %e %e" % ( k, x, abs(x-xold) ))
        fx   = f(x)
        xold = x
        if (fa*fx > 0):
            a = x
        else:
            b = x
    print('Numero maximo de iteracoes excedido.')
    return None

# -----------------------------------------------------------------------------  

def newton(f,df,x0,tol=1.0e-8,maxit=100):

    print("\nMETODO DE NEWTON")

    for k in range(1,maxit):
        x1  = x0 - f(x0)/df(x0)
        err = abs(x1 - x0)

        print(" %d  %e  %e  %e" % (k, x1, f(x1), err) )

        if (err < tol):
            return x1

        x0 = x1

    print("Numero maximo de iteracoes excedido.")
    return None    

# -----------------------------------------------------------------------------

def secante(f,x0,x1,tol=1.0e-8,maxit=100):
    """
    Essa funcao implementa o metodo da Secante para encontrar a raiz da funcao f,
    usando x0 e x1 como aproximacoes iniciais.

    Parametros:
       - f: funcao
       - x0: aproximacao inicial
       - x1: aproximacao inicial
       - tol: precisao, i.e., converge quando |x2-x1| < tol
       - maxit: numero maximo de iteracoes que o metodo pode realizar

    Exemplo de uso:

       def funcao(x): return 4*cos(x) - exp(x)
       raiz = secante(funcao, 1.0)
    """
    print("\nMETODO DA SECANTE")

    for k in range(maxit):
        f1, f0 = f(x1),f(x0)
        x2 = x1 - (f1*(x1-x0))/(f1-f0)
        f2 = f(x2)

        print("%2d %18.11e %18.11e" % ( k, x2, abs(x2-x1) ) )

        if (abs(x2-x1) < tol):
            return x2

        x0 = x1
        x1 = x2

    print("Numero maximo de iteracoes excedido.")
    return None

# -----------------------------------------------------------------------------
# Exemplos de funcoes para encontrar as raizes
# -----------------------------------------------------------------------------
# Exemplo 1
# -----------------------------------------------------------------------------

def f1(x): 
    # f1(x) = 0
    return (x/2.0)**2 - sin(x)

def phi1(x): 
    # x = phi1(x)
    return 2.0*sqrt(sin(x))

# -----------------------------------------------------------------------------
# Exemplo 2 - Wilkinson
# -----------------------------------------------------------------------------

def pw(x):
    #
    # polinomio p(x) = (x-1)(x-2)(x-3)...(x-19)(x-20)
    # expandido como c20 x^20 + c19 x^19 + ... + c1 x + c0 
    #
    return 1.0*x**20 - 210.0*x**19 + 20615.0*x**18 \
           - 1256850.0*x**17 + 53327946.0*x**16 - 1672280820.0*x**15\
           + 40171771630.0*x**14 - 756111184500.0*x**13 \
           + 11310276995381.0*x**12 - 135585182899530.0*x**11 \
           + 1.3075350105404e+15*x**10 - 1.01422998655115e+16*x**9 \
           + 6.30308120992949e+16*x**8 - 3.11333643161391e+17*x**7 \
           + 1.20664780378037e+18*x**6 - 3.59997951794761e+18*x**5 \
           + 8.03781182264505e+18*x**4 - 1.2870931245151e+19*x**3 \
           + 1.38037597536407e+19*x**2 - 8.7529480367616e+18*x \
           + 2.43290200817664e+18

# -----------------------------------------------------------------------------
       
if __name__ == "__main__":

    # --------------------
    # Teste 1
    # --------------------
    a = 1.5
    b = 2.0
    tol = 1e-3
    r1 = bisecao(f1,a,b,tol)
    print("Raiz aproximada bissecao %e" % r1)

    x0 = 1.5
    r2 = pontofixo(phi1,x0)   
    print("Raiz aproximada pt. fixo %e" % r2)

    # --------------------
    # Teste 2 
    # --------------------

    x = np.linspace(0.9,20.1,10000)
    y = pw(x)
    plt.plot(x,y)
    plt.show()
    plt.savefig("pw1.png")
    plt.clf()

    x = np.linspace(9.1,10.9,10000)
    y = pw(x)
    plt.plot(x,y)
    plt.show()
    plt.savefig("pw2.png")

