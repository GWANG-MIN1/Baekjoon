import sys 

input = sys.stdin.readline

N = int(input())
for i in range(N):
    k = int(input())
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    num = k
    while True:
        if is_prime(num):
            print(num)
            break
        num += 1