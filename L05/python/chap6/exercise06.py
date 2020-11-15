# exercise 6 chap 6 based on exercise 9 chapter 3
import math

def triangArea(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    print("This program calculates the area of a triangle")
    a = float(input("Please enter the lenght of one of the triangle's sides (a): "))
    b = float(input("Please enter the lenght of one of the triangle's sides (b): "))
    c = float(input("Please enter the lenght of one of the triangle's sides (c): "))
    print("The area of the triangle is: ", round(triangArea(a,b,c),2))
main()
