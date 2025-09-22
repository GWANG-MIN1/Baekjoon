import sys
input = sys.stdin.readline

N = int(input())
Num  = []
for i in range(N):
    A = int(input())
    if A !=0:
        Num.append(A)
    else:
        Num.pop()

sum = 0
for x in Num:
    sum +=x
print(sum)