# This program approximates the value of pi by summing terms of a serie
import math

def main():
    print("This program approximates the value of pi by summing terms")
    terms = int(input("How many terms do you want to sum?: "))
    sum = 0
    for i in range(1,terms*4,4):
        #print(i,"->",i+2)
        sum += (4/i-4/(i+2))
    print("Approximation of the sum of",terms,"terms: ",sum)
main()
