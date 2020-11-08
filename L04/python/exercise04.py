# This program calculates the distance to a lightning strike
# based on the time elapsed between the flash and the sound of thunder

def main():
    print("This program calculates the distance to a lightning strike")
    print("based on the time elapsed between the flash and the sound of thunder")
    time = float(input("Enter the time in seconds: "))
    rawDistance = time * 1100
    distance = rawDistance / 5280
    print("The distance is: ", round(distance,2), "miles.")
main()
