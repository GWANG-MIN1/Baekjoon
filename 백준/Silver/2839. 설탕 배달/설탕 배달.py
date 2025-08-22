n = int(input())

lst = []

for a in range(n//3 +1):
    for b in range(n//5 +1):
        if 3*a + 5*b == n:
            lst.append((a,b))

if lst:
    result = min(lst, key = lambda x : x[0] + x[1])
    print(result[0] + result[1] )
else:
    print(-1)
