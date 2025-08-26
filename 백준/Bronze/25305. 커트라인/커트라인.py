a,b = map(int,input().split())

numbers = list(map(int, input().split()))

numbers.sort(reverse = True)

print(numbers[b-1])