from classobject import student1


class student:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def study(self):
        print(self.name,"is studying")

student1 = student("Innocent", "male",21)
print(student1.name,student1.gender,student1.age)

student2 = student("Abigael", "female",19)
print(student2.name,student2.gender,student2.age)

student3 = student("Chris", "male",20)
print(student3.name,student3.gender,student3.age)

student4 = student("Rachael", "female",23)
print(student1.name,student4.gender,student4.age)