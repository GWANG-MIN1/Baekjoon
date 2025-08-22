N,M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

min_repaint = float('inf')

for sx in range(N-7):
    for sy in range(M-7):
        cnt_w, cnt_b =0 , 0
        for i in range(8):
            for j in range(8):
                cell = board[sx+i][sy + j]
                if (i+j ) % 2 == 0:
                    if cell != 'W':
                        cnt_w += 1
                    if cell != 'B':
                        cnt_b += 1

                else:
                    if cell != 'B':
                        cnt_w +=1
                    if cell != 'W':
                        cnt_b +=1
        min_repaint = min(min_repaint, cnt_w, cnt_b)

print(min_repaint)                    
