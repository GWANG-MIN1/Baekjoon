arr  = []
ans = []
for i in range(5):
    arr.append(input())

max_len = max(map(len,arr))

for i in range(max_len):
   for j in range(5):
      if i < len(arr[j]):
        ans.append(arr[j][i])

for i in ans:
   print(i , end = '')