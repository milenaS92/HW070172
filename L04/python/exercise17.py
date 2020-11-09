
import math
def mySqrt(guess, x):
    return (guess + (x/guess))/2


def main():
    x = float(input("Please enter the x: "))
    times = int(input("Please enter the number of improvements: "))
    guess = x/2
    for i in range(times):
        guess = mySqrt(guess,x)
    print("The result is: ", guess)
    print("The error is: ", math.sqrt(x)-guess)

main()
