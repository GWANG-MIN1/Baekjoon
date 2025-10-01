import sys 
from collections import deque

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dq = deque(enumerate(nums, start=1))
Ans = []

while dq:
    idx, x = dq.popleft()
    Ans.append(idx)

    if dq:
        if x >0:
            dq.rotate(-(x-1))
        else:
            dq.rotate(-x)

print(*Ans)