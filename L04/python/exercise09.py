# This program calculates the area of a triangle
import math

def main():
    print("This program calculates the area of a triangle")
    a = float(input("Please enter the lenght of one of the triangle's sides (a): "))
    b = float(input("Please enter the lenght of one of the triangle's sides (b): "))
    c = float(input("Please enter the lenght of one of the triangle's sides (c): "))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is: ", round(area,2))
main()
