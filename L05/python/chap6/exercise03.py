# exercise 3 chap 6, based on exercise 1 chap 3
import math

def sphereArea(radius):
    area = 4 * math.pi * (radius**2)
    #print("area:",area)
    return area

def sphereVolume(radius):
    volume = 4/3 * math.pi * (radius**3)
    #print("volume:",volume)
    return volume


def main():
    intro = print("This program calculates the area and volume of a sphere")
    radius = float(input("Please enter the radius of the sphere: "))
    print("The volume of the sphere is:", round(sphereVolume(radius),2))
    print("and the surface of the sphere is:", round(sphereArea(radius),2))
main()
