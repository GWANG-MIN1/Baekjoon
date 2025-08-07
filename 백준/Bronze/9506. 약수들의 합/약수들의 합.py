while True:
    a = int(input())
    if a == -1:
        break

    divisors = [i for i in range(1,a) if a % i ==0]
    divisors.sort()
    total = sum(divisors)

    if total == a:
        print(f"{a} = {' + '.join(map(str,divisors))}")
    else:
        print(f"{a} is NOT perfect.")