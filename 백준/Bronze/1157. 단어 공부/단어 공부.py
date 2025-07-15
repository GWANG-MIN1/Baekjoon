from collections import Counter
word = input().strip().upper()
cnt = Counter(word)
most = cnt.most_common()
if len(most) > 1 and most[0][1] == most[1][1]:
    print("?")
else:
    print(most[0][0])