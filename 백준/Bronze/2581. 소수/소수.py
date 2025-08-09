a = int(input())
b = int(input())    

lst = []


for num in range(a,b+1):
    is_prime = True

    if num >1:
        for i in range(2,int(num **0.5) +1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            lst.append(num)        

        


lst.sort()
if len(lst) == 0:
        print(-1)

else: 
     print(sum(lst))
     print(lst[0])