while True:
    a,b,c = map(int, input().split())
    lst =[a,b,c]
    result = sum(lst) - max(lst)
    if a==b==c==0:
        break
    elif max(lst) >= result:
        print("Invalid")
    else:
        if a==b==c:
            print("Equilateral")
        elif a==b or a==c or b==c:
            print("Isosceles")
        else:
            print("Scalene")