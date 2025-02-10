
num1 = int(input("Enter First Number: "))
operator = input("Enter operator(*,+,-,/): ")
num2 = int(input("Enter Second Number"))

if operator =="*":
    ans = (num1*num2)
    print(ans)

elif operator =="+":
    ans = (num1+num2)
    print(ans)

elif operator =="-":
    ans = (num1-num2)
    print(ans)

elif operator =="/":
    ans = (num1/num2)
    print(ans)


else:
    print("Invalid operator")