import math

a,b,c = map(int, input().split())

days  = math.ceil ((c-b) / (a-b))

print(days)
