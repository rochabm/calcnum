# -----------------------------------------------------------------------------
# UFJF - DCC008 - Calculo Numerico
# Capitulo 4 - Solucao de Sistemas Lineares
# Bernardo M. Rocha
# -----------------------------------------------------------------------------

import numpy as np

# -----------------------------------------------------------------------------

def substituicao(A, b):
    """
    Uso: x = substituicao(A,b)    
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes sucessivas, ou seja, assume-se que A
    e uma matriz triangular inferior.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += A[i,j] * x[j]
        x[i] = ( b[i] - soma ) / A[ i, i ]
    
    return np.matrix(x).transpose()

# -----------------------------------------------------------------------------
				
def substituicaoDiagonalUnitaria(A, b):
    """
    Uso: x = substituicoesDiagonalUnitaria(A,b)    
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes sucessivas, mas assumindo que a diagonal
    principal de A e unitaria.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += A[i,j] * x[j]
        x[i] = b[i] - soma

    return np.matrix(x).transpose()
                    
# -----------------------------------------------------------------------------

def retrosubstituicao(A,b):
    """
    Uso: x = retrosubstituicao(A,b)
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes retroativas, ou seja, assume-se que A
    e uma matriz triangular superior.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma += A[i,j] * x[j]
        x[i] = (b[i] - soma)/A[i,i]

    return np.matrix(x).transpose()

# -----------------------------------------------------------------------------

def gauss(A,b):
    """
    Uso: x = gauss(A,b)

    Essa funcao resolve o sistema de equacoes lineares Ax=b usando 
    o metodo da Eliminacao de Gauss sem pivoteamento.
    """
    n = b.shape[ 0 ]
    # Etapa de eliminacao
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                m = A[i,k]/A[k,k]
                for j in range(k,n):
                    A[i,j] = A[i, j] - m * A[k,j]
                b[i] = b[i] - m * b[k]
                    
    # Resolve o sistema triangular
    x = retrosubstituicao( A, b )
    return x

# -----------------------------------------------------------------------------

def decompLU(A):
    """
    Uso: decompLU(A)
    
    Essa funcao decompoe a matriz de coeficientes A no produto LU
    e armazena o resultado na propria matriz A.
    """
    n = A.shape[ 0 ]
    # Etapa de eliminacao
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                m = A[i,k]/A[k,k]
                A[i,k] = m
                for j in range(k+1,n):
                    A[i,j] = A[i, j] - m * A[k,j]

# -----------------------------------------------------------------------------

def solveLU(A,b):    
    """
    Uso: x = solveLU(A,b)

    Essa funcao recebe uma matriz A = LU, a qual ja foi fatorada
    em L e U e resolve o sistemas de equacoes y = np.zeros(n)Ax = b e retorna
    o vetor solucao x.
    
    Etapas:
      - a matriz A deve ser [A]=[L/U]
      - b eh o vetor do lado direito
      - resolve Ly = b
      - resolve Ux = y
      - retorna a solucao em x
    """
    n = len(A)
    x = np.zeros(n)
    y = np.zeros(n)
    
    # substituicao
    y[0] = b[0]
    for k in range(1,n):
        y[k] = b[k] - np.dot(A[k,0:k], y[0:k])

    # retrosubstituicao
    for k in range(n-1,-1,-1):
        x[k] = (y[k] - np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]

    return x

# -----------------------------------------------------------------------------
	
def cholesky(A):
    """
    Uso: G = cholesky(A)
    
    Essa funcao gera a matriz G da decomposicao de Cholesky
    e a armazena na propria matriz A.
    """
    n = A.shape[0]

    # etapa de eliminacao
    for j in range(0,n):
        soma = 0
        for k in range(0,j):
            soma += A[j,k]*A[j,k]

        try: 
            A[j,j] = sqrt( A[j,j] - soma )
        except ValueError:
            print("A matriz nao eh positiva definida.")
                
        for i in range(j+1,n):
            soma = 0
            for k in range(0,j):
                soma += A[i,k]*A[j,k]
            A[i,j] = ( A[i,j] - soma ) / A[j,j]

    # zera a parte triangular superior
    for k in range(1,n):
        A[0:k,k] = 0.0

    return A

# -----------------------------------------------------------------------------

def solveCholesky(G,b):
    """
    Uso: x = choleskySolve(G,b)

    Resolve o sistema Ax=B usando a decomposicao de Cholesky A = G G^T,
    sendo que G foi obtida atraves do uso da funcao cholesky(A) na
    matriz do sistema A.
    
    G deve ser triangular inferior.
    """
    n = len(b)    
    # substituicao - resolve Gy = b
    y = substituicao(G,b)    
    # retrosubstituicao - resolve G^T x = y
    Gt = G.T
    x = retrosubstituicao(Gt,y)
    return x
                    
# -----------------------------------------------------------------------------

def jacobi(A, b, x0, epsilon, kmax):
    
    # implemente aqui a sua solucao
    # x0: chute inicial
    # epsilon: tolerancia
    # kmax: numero maximo de iteracoes

    pass

# -----------------------------------------------------------------------------

def gaussSeidel(A, b, x0, epsilon, kmax):
    
    # implemente aqui a sua solucao
    # x0: chute inicial
    # epsilon: tolerancia
    # kmax: numero maximo de iteracoes

    pass
