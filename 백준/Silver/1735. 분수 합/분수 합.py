import sys
import math

input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

f = (b * d) // math.gcd(b,d)
e = (a * (f // b) ) + (c * (f // d))

g = math.gcd(e,f)

print(e//g, f // g)