# This program calculates the cost of an order of The Konditorei

def main():
    print("This program calculates the cost of an order of The Konditorei")
    pounds = float(input("Enter the amount of coffe in pounds: "))
    coffeeCost = 10.5 * pounds
    shipCost = 1.5 + 0.86 * pounds
    totalCost = coffeeCost + shipCost
    print("The cost of this order is: $", totalCost)
main()
