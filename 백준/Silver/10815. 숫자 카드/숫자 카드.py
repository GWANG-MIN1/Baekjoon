import sys
input = sys.stdin.readline


def main():
    n = int(input())
    cards = set(map(int,input().split()))
    m = int(input())
    checks = list(map(int, input().split()))
    result = ["1" if x in cards else "0" for x in checks]
    print(" ".join(result))


if __name__ == "__main__":
    main()