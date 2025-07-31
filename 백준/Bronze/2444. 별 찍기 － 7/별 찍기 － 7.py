n = int(input())
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

for j in range(n+1, 2*n):
    print(" " * (j-n) + "*" *(2*((2*n-1) - j) +1))