#2292
n = int(input())

m = 1  # 방 개수 누적합
for i in range(1, 1000000):  # 충분히 큰 범위
    if n <= m:
        print(i)
        break
    m += 6 * i  # 다음 층의 마지막 방 번호

