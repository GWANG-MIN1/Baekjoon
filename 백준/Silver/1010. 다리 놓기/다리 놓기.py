import sys 
from collections import deque

input = sys.stdin.readline

def factorial(n):
    if n <=1:
        return 1
    return n*factorial(n-1)

M = int(input())
for i in range(M):
    a,b = map(int,input().split())
    if a ==b:
        print(1)
    elif a > b:
        print(b)
    else:
        print(factorial(b) // (factorial(a) * factorial(b-a)))