#exercise 5 chapter 6
import math

def pizzaSurface(diam):
    radius = diam / 2
    surface = math.pi * (radius**2)
    return surface

def costPerInch(price,surface):
    cost = price / surface
    return cost

def main():
    print("This program calculates the cost per square inch of a circular pizza")
    diam = float(input("Enter the diameter of the pizza in inches: "))
    price = float(input("Enter the price of a pizza: "))
    print("The cost per square inch is: ", round(costPerInch(price,pizzaSurface(diam)),2))
main()
