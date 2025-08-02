paper = [[0] * 100 for _ in range(100)]
total_area = 0

n = int(input())

for _ in range(n):
    x,y = map(int,input().split())

    for i in range(x, x+10):
        for j in range(y, y+ 10):
            if paper[i][j] == 0:
                paper[i][j] =1
                total_area +=1 

print(total_area)