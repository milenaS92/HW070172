# A program to compute the value of an investment

def main():
    print("---------------------------------------------------------")
    print("This program calculates the future value of an investment")
    print("---------------------------------------------------------")


    principal = eval(input("Enter the initial investment: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the amount of years: "))
    periods = eval(input("Enter the amount of periods per year: "))
    for i in range(years*periods):
        principal += principal * (apr/periods)
    print("The value in", years, "years is:", round(principal,2))
main()
