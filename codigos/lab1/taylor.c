#include <stdio.h>
#include <math.h>

double fat(int n)
{
    int i;
    double f=1.0;
    for(i=n; i>=2; i--)
        f*=i;
    return f;
}

double exp_taylor(int n, double x)
{
    int i;
    double term, sum=0.0;
    for(i=0; i<=n; i++)
    {
        term = pow(x,i)/fat(i);
        sum = sum + term;
    }
    return sum;    
}

double exp_taylor2(int n, double x)
{
    int i;
    double fat=1.0, term=1.0, sum=term;
    for(i=1; i<=n; i++)
    {
        fat  = fat * i;
        term = term * x;
        sum = sum + term/fat;
    }
    return sum;    
}

int main () {

    int n;
    double x;

    printf("n = ");
    scanf("%d", &n);

    printf("x = "); 
    scanf("%lf", &x);
    
    printf("exp(x)  = %e\n", exp(x) );
    printf("taylor  = %e\n", exp_taylor(n, x) );
    printf("taylor2 = %e\n", exp_taylor2(n, x) );
         
    
    return 0;
}
