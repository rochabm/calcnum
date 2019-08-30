from pylab import *

# -----------------------------------------------------------------------------
# Exemplos de funcoes para encontrar as raizes
# -----------------------------------------------------------------------------

def f1(x): 
    # f1(x) = 0
    return (x/2.0)**2 - sin(x)

def phi1(x): 
    # x = phi1(x)
    return 2.0*sqrt(sin(x))

# -----------------------------------------------------------------------------

def pontofixo(phi,x,tol=1e-8,maxit=100):
    """
    Essa funcao implementa o metodo do Ponto Fixo. Recebe como
    parametros a funcao f que se deseja encontrar a raiz, a
    funcao de iteracao phi, uma aproximacao inicial x e
    ainda a precisao tol e numero maximo de iteracoes maxit.
    """
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

def bisecao(f,a,b,tol=1e-8):
    """
    Essa funcao implementa o metodo da Biseccao que encontra uma raiz da 
    funcao f no intervalo [a,b] com uma precisao tal que |f(x)| < tol.
    """
    if (f(a)*f(b) > 0):
        print("Nao ha garantias de que existe raiz nesse intervalo.")
        return None
    x = a
    k = 0
    while(abs(f(x)) > tol):
        x = (a+b)/2
        
        print("%d %e %e" % (k,x,f(x)))

        if(f(a)*f(x) < 0):
            b = x
        else:
            a = x           
        k = k + 1       
    return x

# -----------------------------------------------------------------------------
        
if __name__ == "__main__":

    # Teste 1
    # Metodo da Bissecao
    a = 1.5
    b = 2.0
    tol = 1e-3
    r1 = bisecao(f1,a,b,tol)
    
    # Teste 2 
    # Metodo do ponto fixo
    x0 = 1.5
    r2 = pontofixo(phi1,x0)

    print("Raiz aproximada bissecao %e" % r1)
    print("Raiz aproximada pt. fixo %e" % r2)
