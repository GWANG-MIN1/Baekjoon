import sys
input = sys.stdin.readline

N, M = map(int, input().split())
LISTEN = set(input().strip() for _ in range(N))
SEEN = set(input().strip() for _  in range(M))

answers = sorted(LISTEN & SEEN)

print(len(answers))
for name in answers:
    print(name)
