# exercise 4 chap 6

def sumN(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(n):
        sum += i**3
    return sum

def main():
    n = int(input("Please enter a natural number: "))
    print("The sum of the first",n,"numbers is: ",sumN(n))
    print("The sum of the cubes of the first",n,"numbers is: ",sumNCubes(n))

main()
