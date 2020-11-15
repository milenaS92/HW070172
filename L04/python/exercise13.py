# This program sums a series of numbers entered by the user.

def main():
    print("This program allows to sum a serie of numbers.")
    n = int(input("How many numbers do you want to sum?: "))
    sum = 0
    for i in range(n):
        j = float(input("Enter the number: "))
        sum += j
    print("The total sum is: ", round(sum,2))
main()
