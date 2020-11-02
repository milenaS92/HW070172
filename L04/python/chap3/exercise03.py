# This program calculates the molecular weight of a carbohydrate
# (in grams per mole)

def main():
    print("This program calculates the molecular weight of a carbohydrate.")
    hydro = int(input("Enter the number of hydrogen atoms: "))
    carbon = int(input("Enter the number of carbon atoms: "))
    oxygen = int(input("Enter the number of oxygen atoms: "))
    weight = 1.00794 * hydro + 12.0107 * carbon + 15.9994 * oxygen
    print("The total weight of the molecule is: ", round(weight,6))

main()
