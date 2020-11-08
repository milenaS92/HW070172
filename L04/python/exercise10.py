# This program calculates the lenght of a ladder required
# to reach a given height
import math

def main():
    print("This program calculates the lenght of a ladder")
    height = float(input("Please enter the height to reach: "))
    angle = float(input("Please enter the angle: "))
    lenght = height/math.sin(angle)
    print("The lenght of the needed ledder is: ", round(lenght,2))
main()
