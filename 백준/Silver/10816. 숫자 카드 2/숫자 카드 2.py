import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
answers = list(map(int, input().split()))

counter = Counter(numbers)

sum_cnt = [counter[x] for x in answers]
print(*sum_cnt)
