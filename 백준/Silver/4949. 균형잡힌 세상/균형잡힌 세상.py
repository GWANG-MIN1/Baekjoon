import sys 
input = sys.stdin.readline


while True:
    s = input().rstrip()
    stack = []
    ok = True
    if s == '.':
        break

    for ch in s:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                ok = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                ok =False
                break
            stack.pop()

    if ok and not stack:
            print('yes')
    else:
            print('no')