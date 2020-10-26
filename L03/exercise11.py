# A program to convert kilograms to pounds

def main():
    print("------------------------------------------------------")
    print("This program converts kilograms to pounds")
    print("------------------------------------------------------")
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = kilos * 2.20462
    print("The entered weight equals", round(pounds,2), "pounds.")

main()
