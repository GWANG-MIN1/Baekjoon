n = int(input())
num = []
val = []

for i in range(n):
    s,v = input().split()
    num.append(int(s))
    val.append(v)

for i in range(n):
    for j in val[i]:
        print(num[i]* j , end = "")
    print()