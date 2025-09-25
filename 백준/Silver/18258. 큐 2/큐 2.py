import sys 
from collections import deque

input = sys.stdin.readline

N = int(input())
Q = deque()

for _ in range(N):
    S = input().split()
    if S[0] == 'push':
        Q.append(int(S[1]))
    elif S[0] == 'pop':
        print(Q.popleft() if Q else -1)
    elif S[0] == 'size':
        print(len(Q))
    elif S[0] == 'empty':
        print(0 if Q else 1)
    elif S[0] == 'front':
        print(Q[0] if Q else -1)
    elif S[0] == 'back':
        print(Q[-1] if Q else -1)