# A program to compute the value of an investment

def main():
    print("---------------------------------------------------------")
    print("This program calculates the future value of an investment")
    print("---------------------------------------------------------")


    investment = eval(input("Enter the yearly investment: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the amount of years: "))
    principal = 0
    for i in range(years):
        principal += investment
        principal += principal * apr
    print("The value in", years, "years is:", round(principal,2))
main()
