import sys
input = sys.stdin.readline

N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]
coords.sort(key=lambda x: (x[1], x[0]))  # (y, x) 순으로 정렬

print("\n".join(f"{x} {y}" for x, y in coords))
