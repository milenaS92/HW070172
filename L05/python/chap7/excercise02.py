# exercise 2 chap 7

def gradeOfQuiz(score):
    if score == 5:
        return "A"
    elif score == 4:
        return "B"
    elif score == 3:
        return "C"
    elif score == 2:
        return "D"
    else:
        return "F"

def main():
    score = int(input("Please enter the score: "))
    grade = gradeOfQuiz(score)
    print("The corresponding grade is:", grade)
main()
