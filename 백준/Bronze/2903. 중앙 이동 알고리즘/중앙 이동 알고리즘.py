n = int(input())

# 한 변에 있는 점의 수: 1 + 2^n
side = 1 + 2**n

# 전체 점 개수는 정사각형 전체 격자 수
total_points = side ** 2

# 출력
print(total_points)
