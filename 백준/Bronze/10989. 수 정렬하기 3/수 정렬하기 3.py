import sys

MAX_VALUE = 10001
counts = [0] * MAX_VALUE


n = int(sys.stdin.readline())


for _ in range(n):
    num = int(sys.stdin.readline())
    if 0 <= num < MAX_VALUE: 
        counts[num] += 1


for i in range(MAX_VALUE):
    for _ in range(counts[i]):
        print(i)