# This program calculates the number of days between January 1st and
# the previous new moon.

def main():
    print("This program calculates the number of days between January 1st")
    print("and the previous new moon.")
    year = int(input("Please enter a 4-digit year: "))
    c = year // 100
    epact = (8+(c//4)-c+((8*c+13)//25)+11*(year%19))%30
    print("The epact is: ", epact)
main()
