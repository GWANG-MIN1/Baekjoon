import sys
input = sys.stdin.readline

MAX = 1000000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) +1):
    if is_prime[i]:
        for j in range(i*i , MAX +1 , i):
            is_prime[j] = False


N = int(input())
for i in range(N):
    a = int(input())
    cnt = 0
    for j in range(2, a // 2 + 1):
        if is_prime[j] and is_prime[a - j]:
            cnt += 1
    print(cnt)
