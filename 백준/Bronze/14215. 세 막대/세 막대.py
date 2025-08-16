a,b,c = map(int, input().split())
arr = sorted([a,b,c])

if arr[2] < arr[0] + arr[1]:
    print(sum(arr))
else:
    print((arr[0] + arr[1]) * 2 -1)