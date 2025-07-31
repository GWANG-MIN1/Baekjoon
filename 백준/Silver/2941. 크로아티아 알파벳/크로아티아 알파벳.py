s = input()
m = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=" , "z="]

for i in m:
    s = s.replace(i,"*")

print(len(s))