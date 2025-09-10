import sys
input = sys.stdin.readline

N, M = map(int, input().split())
AMAP = set(map(int,input().split()))
BMAP = set(map(int,input().split()) )

FANSWER = sorted(AMAP - BMAP)
SANSWER = sorted(BMAP - AMAP)


print(len(FANSWER)+ len(SANSWER))