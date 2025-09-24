import sys 
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
need = 1 

for i in arr:
    if i == need:
        need +=1
    else:
        stack.append(i)

    while stack and stack[-1] == need :
        stack.pop()
        need +=1

if not stack:
    print('Nice')
else:
    print('Sad')