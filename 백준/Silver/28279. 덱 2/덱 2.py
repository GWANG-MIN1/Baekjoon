import sys 
from collections import deque

input = sys.stdin.readline
dq = deque()
N = int(input())

for i in range(N):
    S = input().split()
    if S[0] == '1':
        dq.appendleft(int(S[1]))

    elif S[0] == '2':
        dq.append(int(S[1]))
        
    elif S[0] == '3':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif S[0] =='4':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif S[0] == '5':
        print(len(dq))
    
    elif S[0] == '6':
        if dq:
            print(0)
        else:
            print(1)
    elif S[0] == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif S[0] == '8':
        if dq:
            print(dq[-1])
        else:
            print(-1) 

           





