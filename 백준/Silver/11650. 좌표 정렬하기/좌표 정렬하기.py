n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
pairs.sort()
for x, y in pairs:
    print(x, y)