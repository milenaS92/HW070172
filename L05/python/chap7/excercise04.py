# exercise 4 chap 7

def studentClass(credits):
    if credits < 7:
        return "Freshman"
    elif credits < 16:
        return "Sophomore"
    elif credits < 26:
        return "Junior"
    else:
        return "Senior"

def main():
    credits = int(input("Please enter the credits: "))
    student = studentClass(credits)
    print("The student is a", student)
main()
