import sys 
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
Q = deque(range(1, N+1))
A = []


while len(Q) >= 1:
    Q.rotate(-(M-1))
    A.append(Q.popleft())

print("<" + ", ".join(map(str, A)) + ">")
        