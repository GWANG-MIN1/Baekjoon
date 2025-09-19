import sys 

input = sys.stdin.readline

MAX = 123456 *2
is_prime = [True] * (MAX +1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    primes = []
    for i in range(n+1, (2*n)+1):
        if is_prime[i]:
            primes.append(i)
    print(len(primes))        
    