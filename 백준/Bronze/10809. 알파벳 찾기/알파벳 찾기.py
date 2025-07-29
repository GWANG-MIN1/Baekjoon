s = list(input())
for i in range(97,123):
    if chr(i) in s and s[0] == chr(i):
        print(0)
    elif chr(i) in s:
        print(s.index(chr(i)))
    else :
        print(-1)