import sys
import math

input = sys.stdin.readline
a,b = map(int,input().split())

g = math.gcd(a,b)
lcm = a*b // g
print(lcm)