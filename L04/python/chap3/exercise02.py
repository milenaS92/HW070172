# this program calculates the cost per square inch
# of a circular pizza
import math

def main():
    print("This program calculates the cost per square inch of a circular pizza")
    diam = float(input("Enter the diameter of the pizza in inches: "))
    price = float(input("Enter the price of a pizza: "))
    radius = diam / 2
    surface = math.pi * (radius**2)
    costPerInch = price / surface
    print("The cost per square inch is: ", round(costPerInch,2))
main()
