from collections import defaultdict

d = defaultdict(int)
n = 150 
p = 2
while p*p <= n:
    while n % p == 0:
        d[p] += 1
        n //= p
    print(p)
    p += 1
if n > 1:
    d[n] += 1

print(d)