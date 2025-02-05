
courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

# Accessing an element
print(courses[2])

# Looping through an array
for x in courses:
    print("Course is", x)

# Adding a new element into an array
courses.append("laravel")
print(courses)

#Removing an element
courses.remove("Cybersecurity")
print(courses)