all_nam = set()
for _ in range(1,11):
    N = int(input())
    all_nam.add(N % 42)
    
print(len(all_nam))


