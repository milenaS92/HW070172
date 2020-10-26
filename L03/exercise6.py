# A program to compute the value of an investment
# input: the amount of years that the investment will be carried

def main():
    print("----------------------------------------------")
    print("This program calculates the future value")
    print("of an investment after a given amount of years")
    print("----------------------------------------------")


    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the amount of years: "))

    for i in range(years):
        principal = principal * (1 + apr)
    print("The value in", years, "years is:", round(principal,2))
main()
