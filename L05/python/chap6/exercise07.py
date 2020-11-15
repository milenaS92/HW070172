# exercise 7 chap 6 based on exercise 16 chapter 3
# This program calculates the nth Fibonacci number

def fibonacci(n):
    if n < 1:
        return n
    if n == 1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

def main():
    print("This program calculates the nth Fibonacci number ")
    n = int(input("Enter the number n: "))
    print("The nth Fibonacci number is: ", fibonacci(n))
main()
