# This program calculates the distance between two points
import math

def main():
    print("This program calculates the distance between two points")

    cord1 = input("Enter the first coordinates separated by a comma (x,y): ")
    list1 = cord1.split(",")
    x1 = int(list1[0])
    y1 = int(list1[1])
    #print("x1: ", x1, "y1: ", y1)

    cord2 = input("Enter the other coordinates separated by a comma (x,y): ")
    list2 = cord2.split(",")
    x2 = int(list2[0])
    y2 = int(list2[1])
    #print("x2: ", x2, "y2: ", y2)
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The distance between the points is: ",round(distance,2))
main()
