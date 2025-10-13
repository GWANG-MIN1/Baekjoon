import sys 
from collections import deque

input = sys.stdin.readline

def factorial(n):
    if n <=1:
        return 1
    return n*factorial(n-1)

a,b = map(int,input().split())

print(factorial(a) // (factorial(b) * factorial(a-b)))
    

