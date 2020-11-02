#this program calculates the area and volume of a sphere
import math

def main():
    intro = print("This program calculates the area and volume of a sphere")
    radius = float(input("Please enter the radius of the sphere: "))
    volume = 4/3 * math.pi * (radius**3)
    surface = 4 * math.pi * (radius**2)
    print("The volume of the sphere is:", round(volume,2))
    print("and the surface of the sphere is:", round(surface,2))
main()
