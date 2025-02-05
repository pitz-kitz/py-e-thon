# 1. A simple python program to
#check whether a year is a leap or not

# 2. A python program that checks whether
# letter is a vowel or a consonant

year = 2024

if (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


    #2

letter = "p"
if letter in ("a","e","i","o","u"):
    print("vowel")
elif letter in ("A","E","I","O","U"):
    print("vowel")
else:
    print("consonant")
