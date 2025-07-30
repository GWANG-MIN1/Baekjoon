n = list(map(int, input().split()))
ans = [1,1,2,2,2,8]
out =[]

for i in range(len(n)):
     out.append(ans[i] - n[i])

print(*out)