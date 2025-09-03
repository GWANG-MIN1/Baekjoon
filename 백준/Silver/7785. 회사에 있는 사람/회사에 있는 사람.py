import sys
input = sys.stdin.readline

def main():
    n = int(input())
    entered = set()
    for _ in range(n):
        name, action = input().split()
        if action == "enter":
            entered.add(name)
        else:
            entered.discard(name)
    
    for name in sorted(entered, reverse=True):
        print(name)

if __name__ == "__main__":
    main()