num = int(input())

nums = list(map(int, input().split()))


max_score = max(nums)
total = 0
if max_score != 0:
    for score in nums:
        total += score / max_score * 100
       

avg = total / num

print(avg)
