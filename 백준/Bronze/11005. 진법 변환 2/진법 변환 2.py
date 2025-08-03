n,b = map(int, input().split())


if n ==0:
    print(0)

result = ''
nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n > 0:
    remainder = n % b
    n //= b

    result +=nums[remainder]

print(result[::-1])
