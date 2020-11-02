# This program calculates the average
# of a series of numbers entered by the user.

def main():
    print("This program allows to calculate the average of a serie of numbers.")
    n = int(input("How many numbers do you want to enter?: "))
    sum = 0
    for i in range(n):
        j = float(input("Enter the number: "))
        sum += j
    avg = sum / n
    print("The average is: ", round(avg,2))
main()
