Hak = {"A+" : 4.5, "A0" : 4.0, "B+": 3.5, "B0" : 3.0, "C+" : 2.5 , 
       "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0}

total = 0
sum_credit = 0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    
    if grade == "P":
        continue
    
    sum_credit +=  credit
    m = Hak[grade]
    total += credit * (m)

    

if sum_credit == 0:
    print(0.0)
else:
    avg = total/sum_credit

print(avg)