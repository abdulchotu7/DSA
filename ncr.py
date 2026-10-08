n = 10**5 

m = 10**9 + 7 

fact = [1]*(n+1)
invfact = [1]*(n+1)

for i in range(1,n+1):
    fact[i] = (fact[i-1]*i) % m 

print(fact[5])


invfact[n] = pow(fact[n],m-2,m)

for i in range(n-1,0,-1):
    invfact[i] = (invfact[i+1]*(i+1)) % m


def ncr(n,r):
    if r>n:
        return 0
    return (fact[n]*invfact[r]*invfact[n-r]) % m

print(ncr(5,2))