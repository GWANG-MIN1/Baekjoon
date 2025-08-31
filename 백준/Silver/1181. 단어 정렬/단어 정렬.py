n = int(input())
sentences = [input().strip() for _ in range(n)]
sentences = list(set(sentences))
sentences.sort(key = lambda x :(len(x),x))

for s in sentences:
    print(s)