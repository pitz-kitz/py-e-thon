# Built-in functions/Standard-Library function

y = max(45, 89, 75, 89, 56, 43)
print("The maximum value is",y )

x = min(5, 90, 68, 43, 40)
print("The minimum value is",x)

# User-defined functions
def school():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1 + num2)

add()

# Parameter/variable and Argument/value
def multiply(a , b):
    print(a * b)

multiply(6,5)
multiply(10,56)
multiply(5,20)


def employee(name, age, gender, salary, position):
    print(name, age, gender, salary, position)

employee("Maureen",25,"Female", 56000,"CEO")
employee("John",52,"Male", 80000,"Managing Director")
employee("Mary",34,"Female", 94000,"Product Manager")
employee("David",44,"Male", 74000,"Accountant")
employee("Harry",27,"Male", 120000,"Marketer")
employee("Joan",40,"Female", 40000,"Secretary")

# A program to display details of five patients
# Using a user-defined function,implement parameter
# and argument
# fullname, gender, age, disease

def patient(fullname, gender, age, disease):
    print(fullname, gender, age, disease)

patient("JamesMwangi","Male",36,"malaria")
patient("SarahWangui","Female",14,"bilharzia")
patient("DeborahAkinyi","Female",47,"HIV")
patient("RoyBrown","Male",8,"Marasmus")
patient("MitchellOuma","Female",28,"Std")
