# exercise 3 chap 7

def gradeOfQuiz(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    score = int(input("Please enter the score: "))
    grade = gradeOfQuiz(score)
    print("The corresponding grade is:", grade)
main()
