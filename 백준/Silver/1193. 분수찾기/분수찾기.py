#1193
X = int(input())

line = 1
# 그룹 찾기
while X > line * (line + 1) // 2:
    line += 1

# 해당 그룹의 시작 번호
start_num = (line - 1) * line // 2 + 1
position = X - start_num + 1

if line % 2 == 0:
    numerator = position
    denominator = line - position + 1
else:
    numerator = line - position + 1
    denominator = position

print(f"{numerator}/{denominator}")


