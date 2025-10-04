import sys 
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input().strip())
C = list(map(int, input().split()))

dq = deque()
for i in range(N):
    if A[i] == 0:
        dq.append(B[i])

out = []
for x in C:
    dq.appendleft(x)
    val = dq.pop()
    out.append(str(val))

print(" ".join(out))