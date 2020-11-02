# This program calculates the sum of the first n natural numbers

def main():
    print("This program calculates the sum of the first n natural numbers")
    n = int(input("Please enter the natual number: "))
    sum = 0
    for i in range(0,n+1):
        sum += i
    print("The sum of the numbers is: ", sum)
main()
