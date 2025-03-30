mod = 1000000007 ;

def sumOddFibonacci(n): 
    Sum=[0]*(n + 1); 
 
    # base values 
    Sum[0] = 0; 
    Sum[1] = 1; 
    Sum[2] = 2; 
    Sum[3] = 5; 
    Sum[4] = 10; 
    Sum[5] = 23; 
 
    for i in range(6,n+1): 
        Sum[i] = ((Sum[i - 1] +
                    (4 * Sum[i - 2]) % mod -
                    (4 * Sum[i - 3]) % mod +
                    mod) % mod + (Sum[i - 4] -
                    Sum[i - 5] + mod) % mod) % mod; 
 
    return Sum[n]; 
 
n = 6; 
print(sumOddFibonacci(35)); 