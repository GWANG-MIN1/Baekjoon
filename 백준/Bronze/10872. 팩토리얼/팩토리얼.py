def factorial(n):
    if n <= 1:  # 0! 또는 1! 은 1
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
