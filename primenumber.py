
number = int(input("Enter Number: "))
count = 0
if number > 1:
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    if count ==2:
        print("Number is prime")

    else:
        print("Number is not prime")
