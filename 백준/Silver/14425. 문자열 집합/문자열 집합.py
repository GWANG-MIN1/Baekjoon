import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    Strings = [input() for _ in range(n)]
    checks = [input() for _ in range(m)]
    result = [1 if x in Strings else 0 for x in checks ]
    cnt = 0
    for x in result:
        if x == 1:
            cnt += 1
        else:
            continue
    print(cnt)

if __name__ == "__main__":
    main()