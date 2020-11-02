# This program calculates the slope of a line trough 2 points

def main():
    print("This program calculates the slope of a line trough 2 points")
    valid = False
    while valid == False:
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
        if x1 != x2:
            valid = True
        else:
            print("The entered coordinates are vertical points, please enter new ones!")
    slope = (y2-y1)/(x2-x1)
    print("The slope of a line through this points is: ", round(slope,2))
main()
