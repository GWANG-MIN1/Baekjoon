n = int(input())

lst = []

for i in range(n):
        a,b = map(int,input().split())
        lst.append((a,b))

if n ==1:
        print(0)
else:
    x_values = [x for x,y in lst]
    y_values = [y for x,y in lst]

    result = (max(x_values) - min(x_values)) * (max(y_values) - min(y_values))


    print(result)
