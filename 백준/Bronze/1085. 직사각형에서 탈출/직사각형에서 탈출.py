x,y,z,w = map(int, input().split())

# a , c-a b , d-b
a = x
b = abs(z-x)
c = y
d = abs(w-y)

print(min(a,b,c,d))
