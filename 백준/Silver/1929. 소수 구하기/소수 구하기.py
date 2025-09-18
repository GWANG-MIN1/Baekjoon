import sys 

input = sys.stdin.readline

N,M = map(int, input().split())
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n ==3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
             
for k in range(N, M+1):
    if is_prime(k):
        print(k)