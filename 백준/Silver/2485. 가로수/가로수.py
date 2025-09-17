import sys
import math

input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]
trees.sort()

diffs = [trees[i+1] - trees[i] for i in range(N-1)]
g = diffs[0]
for d in diffs[1:] :
    g = math.gcd(g, d)

total_len = trees[-1] - trees[0]

need = (total_len // g) + 1
print(need - N )
