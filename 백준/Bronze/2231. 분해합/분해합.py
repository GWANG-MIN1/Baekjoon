n = int(input())
result = 0

for m in range(1, n+1):
    digit_sum = sum(int(ch) for ch in str(m))
    if digit_sum + m == n:
        result = m
        break

print(result)
