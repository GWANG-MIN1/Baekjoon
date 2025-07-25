import sys
num = int(sys.stdin.readline())


nums = list(map(int, sys.stdin.readline().split()))

max_score = max(nums)
total = 0


if max_score != 0:
    for i in range(num):
        nums[i] = nums[i] / max_score * 100
        total += nums[i]


avg = total / num

print(avg)