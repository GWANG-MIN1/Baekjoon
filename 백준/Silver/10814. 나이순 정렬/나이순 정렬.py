n = int(input())
members = [(int(a), b) for a, b in (input().split() for _ in range(n))]
members.sort(key = lambda x : x[0])
for age, name in members:
    print(age, name)