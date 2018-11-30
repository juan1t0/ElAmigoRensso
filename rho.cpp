#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>

using namespace std;

typedef long long int lli;


lli modulo(lli a, lli b){
    lli r;
    r = a-( (a / b) * b);
    if(r < 0)
        r += b;
    return r;
}
lli modular_pow(lli base, int exponent, lli modulus) 
{ 
    lli result = 1; 
    while (exponent > 0) 
    { 
        if (exponent & 1) 
            result = (result * base) % modulus; 

        exponent = exponent >> 1; 
        base = modulo((base * base), modulus); 
    } 
    return result; 
}
lli GCD(lli a, lli b){
    lli r = modulo(a, b);
    while(r > 0){
        a = b;
        b = r;
        r = modulo(a, b);
    }
    return b;
}

lli PollardRho(lli n) 
{ 
    if (n == 1) return n; 
    if (modulo(n, 2) == 0) return 2; 

    lli x = modulo(rand(),(n-2)) + 2; 
    lli y = x; 
    lli c = modulo(rand(),(n-1)) + 1; 
    lli d = 1;   

    while (d==1) 
    { 
        x = modulo((modular_pow(x, 2, n) + c + n), n); 
        y = modulo((modular_pow(y, 2, n) + c + n), n); 
        y = modulo((modular_pow(y, 2, n) + c + n), n); 
        d = GCD(abs(x - y), n); 
        if (d == n) return PollardRho(n); 
    } 
    return d; 
} 

int main() 
{
    srand (time(NULL)); 

    lli n; //= 10967535067; 
    cin>>n;
    printf("One of the divisors for %lld is %lld.", n, PollardRho(n)); 
    return 0; 
} 

/* 
    Yash Varyani - geeks for geeks / pollards-rho-algorithm-prime-factorization
*/