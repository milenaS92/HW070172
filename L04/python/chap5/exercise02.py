# This programs returs the corresponding grade by entering
# the score in a 5-point quiz

def main():
    score = int(input("Please enter the score in the 5-point quiz: "))
    grade = "FFDCBA"
    print("Grade: ",grade[score])
main()
