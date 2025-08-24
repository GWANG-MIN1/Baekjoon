n = int(input())
nums = [int(input()) for _ in range(n)]

if max(nums) == nums[0]:
    print("hard")
elif min(nums) == nums[0]:
    print("ez")
else:
    print("?")