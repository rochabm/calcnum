"""
Este modulo implementa diversos metodos para encontrar o zero
de funcoes nao-lineares da forma:
 
                    f(x) = 0

Metodos implementados: 
    - bisseccao
    - falsa posicao
    - ponto fixo
    - Newton
    - secante

Universidade Federal de Juiz de Fora
Departamento de Ciencia da Computacao
Bernardo M. Rocha 
"""

from math import *
from pylab import *
import numpy as np

#------------------------------------------------------------------------------

def bissecao(f,a,b,tol=1.0e-8):
    """
    Essa funcao implementa o metodo da Bissecao que encontra uma raiz da 
    funcao f no intervalo [a,b] com uma precisao tal que |f(x)| < tol.
    """
    if( f(a) * f(b) > 0 ):
        print("Nao ha garantias de existir raiz nesse intervalo")
        return None
    k = 0
    x = a
    print(" passo\txk \t\t f(xk)")
    while abs(f(x)) > tol:
        x = a + (b-a)/2.0
        print(" %d\t%e\t%e" % (k,x,f(x)))
        if( f(a)*f(x) > 0 ):
            a = x
        else:
            b = x
        k = k + 1
    return x

#------------------------------------------------------------------------------

def falsaposicao(f,a,b,tol=1.0e-8):
    """
    Essa funcao implementa o metodo da Falsa Posicao para encontrar uma raiz da 
    funcao f no intervalo [a,b] com uma precisao tal que |f(x)| < tol.
    """    
    if (f(a)*f(b)>0):
        print("Nao ha garantias de existir raiz nesse intervalo")
        return None
    k = 0
    xk = a
    while abs(f(xk)) > tol:	
        xk = ( a * f(b) - b * f(a) ) / ( f(b) - f(a) )		
        print(" %d\t%e\t%e" % ( k, xk, f(xk) ))
        if f(a)*f(xk) < 0:
            b = xk
        else:
            a = xk             
        k = k + 1
    return xk

#------------------------------------------------------------------------------

def pontofixo(f,phi,x,tol=1e-8,maxit=100):
    """
    Essa funcao implementa o metodo do Ponto Fixo. Recebe como parametros a 
    funcao f que se deseja encontrar a raiz, a funcao de iteracao phi, 
    uma aproximacao inicial x e ainda a precisao tol e numero maximo 
    de iteracoes maxit.

    Parametros:
       - f - funcao
       - phi - funcao de iteracao
       - x - aproximacao inicial
       - tol - precisao
       - maxit - numero maximo de iteracoes

    Exemplo:
       Resolver f(x) = (x/2)**2 - sin(x)

       def f(x):
           return (x/2)**2 - sin(x)

       def phi(x):
           return 2.0 * sqrt(sin(x))

       raiz = pontofixo(f,phi,1.5)   
       raiz = pontofixo(f,phi,1.5, 1e-5) 
       raiz = pontofixo(f,phi,1.5, 1e-5, 50) 
    """
    x0 = x
    for k in range(maxit):
        x1 = phi(x0)              
        print(" %d %e %e" % ( k, x1, abs(x1-x0) ))              
        if abs(x1 - x0)/abs(x1) <= tol:
            return x1
        x0 = x1              
    print("Numero maximo de iteracoes excedido")
    return x1
              
#------------------------------------------------------------------------------

def newton(f,df,x0,tol=1.0e-8,maxit=100):
    """
    Essa funcao implementa o metodo de Newton para encontrar a raiz da funcao f,
    cuja derivada e dada por df usando x0 como aproximacao inicial.

    Parametros:
       - f: funcao
       - df: derivada de f
       - x0: aproximacao inicial
       - tol: precisao, i.e., converge quando |x1-x0| < tol
       - maxit: numero maximo de iteracoes que o metodo pode realizar

    Exemplo de uso:

       def funcao(x): 
           return 4*cos(x) - exp(x)

       def derivada(x):
           return -4*sin(x) - exp(x)

       raiz = newton(funcao, derivada, 1.0)
       raiz = newton(funcao, derivada, 1.0, 1e-5)
       raiz = newton(funcao, derivada, 1.0, 1e-5, 20)
    """
    for k in range(1,maxit):
        x1  = x0 - f(x0) / df(x0)
        err = abs(x1 - x0)/abs(x1)
        print(" %d  %e  %e  %e" % (k, x1, f(x1), err) )
        if (err < tol):
            return x1
        x0 = x1
    print("Numero maximo de iteracoes excedido.")
    return x1

#------------------------------------------------------------------------------

def secante(f,x0,x1,tol=1.0e-8,maxit=100):
    """
    Essa funcao implementa o metodo da Secante para encontrar a 
    raiz da funcao f, usando x0 e x1 como aproximacoes iniciais.

    Parametros:
       - f: funcao
       - x0: aproximacao inicial
       - x1: aproximacao inicial
       - tol: precisao, i.e., converge quando |x2-x1| < tol
       - maxit: numero maximo de iteracoes que o metodo pode realizar

    Exemplo:

       def funcao(x): 
           return 4*cos(x) - exp(x)

       raiz = secante(funcao, 1.0)
       raiz = secante(funcao, 1.0, 1e-5)
       raiz = secante(funcao, 1.0, 1e-5, 40)

    """
    for k in range(maxit):
        f1, f0 = f(x1), f(x0)
        x2 = x1 - (f1*(x1-x0))/(f1-f0)
        f2 = f(x2)
        err = abs(x2-x1)/abs(x2)
        print(" %d\t%e\t%e\t%e" % (k, x2, f2, err) )
        if err < tol:
            return x2
        x0, x1 = x1, x2
    print("Numero maximo de iteracoes excedido.")
    return x2

#------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Aqui definimos cada problema e em seguida
    # chamamos os metodos para a solucao.
    # Para mudar de problema, basta comentar e descomentar
    # a definicao da funcao, derivada, funcao de iteracao
    # ou implementar seu proprio problema.

    ### Problemas ###

    # Voce pode implementar f(x) e f'(x) criando uma funcao
    #
    # def f(x):
    #     return exp(-x**2) - cos(x)
    #
    # ou usando funcoes lambda da seguinte forma (+ compacta)    
    # f = lambda x: exp(-x**2) - cos(x)

    # Teste 1
    f   = lambda x: (x/2)**2 - sin(x)
    df  = lambda x: x/2 - cos(x)
    phi = lambda x: 2 * sqrt(sin(x))
    a,b = 1.5 , 2.0
    x0  = 2.0
    x1  = 1.6

    # Teste 2 (para Newton / Secante)
    #f  = lambda x: ((x-5.0)**3)*exp(x)
    #df = lambda x: (3.0*(x-5.0)**2)*exp(x) + ((x-5.0)**3)*exp(x)   
    #x0 = 4.5
    #x1 = x0+0.1
   
    # Teste 3 (slide 37)
    f = lambda x: 10000. - (1250.0/x)*(1.0 - (1+x)**(-10))
    a,b = 0, 10 
    a,b = 0.0001, 1 

    x = np.linspace(a,b,1000)
    plot(x,f(x))
    show()


    ### Metodos ###

    print("\nmetodo da bissecao")
    x = bissecao(f,a,b)
    print(" raiz = ", x)

    #print("\nmetodo da falsa posicao")
    #x = falsaposicao(f,a,b)
    #print(" raiz = ", x)

    #print("\nmetodo do ponto fixo")
    #x = pontofixo(f, phi, x0)
    #print(" raiz = ", x)

    #print("\nmetodo de newton")
    #x = newton(f,df,x0)
    #print(" raiz = ", x)

    #print("\nmetodo da secante")
    #x = secante(f,x0,x1)
    #print(" raiz = ", x)

    print("\n fim")

