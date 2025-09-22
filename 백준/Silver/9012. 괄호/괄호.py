import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    stack = []
    ok = True

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                ok = False
                break

    if ok and not stack: 
        print('YES')
    else:
        print('NO')