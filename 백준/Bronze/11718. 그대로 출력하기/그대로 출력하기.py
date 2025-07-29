s = []
cnt = 0
try:
    while True:
        if cnt < 100:
            s.append(input())
            cnt +=1
        else:
            break
except EOFError:
    pass

for i in range(len(s)):
    print(s[i])