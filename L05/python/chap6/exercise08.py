# exercise 8 chap 6 based on exercise 17 chapter 3

import math
def nextGuess(guess, x):
    return (guess + (x/guess))/2

def main():
    x = float(input("Please enter the x: "))
    times = int(input("Please enter the number of improvements: "))
    guess = x/2
    for i in range(times):
        guess = nextGuess(guess,x)
    print("The result is: ", guess)
    print("The error is: ", math.sqrt(x)-guess)

main()
