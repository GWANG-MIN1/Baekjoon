n = int(input())
numbers = list(map(int, input().split()))
numbers2 = sorted((set(numbers)))
mapping = {v: i for i, v in enumerate(numbers2)}
result = [mapping[x] for x in numbers]
print(*result)