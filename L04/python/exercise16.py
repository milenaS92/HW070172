# This program calculates the nth Fibonacci number

def main():
    print("This program calculates the nth Fibonacci number ")
    n = int(input("Enter the number n: "))
    def fibonacci(n):
        if n < 1:
            return n
        if n == 1:
            return n
        else:
            return fibonacci(n-2)+fibonacci(n-1)
    print("Fibo: ", fibonacci(n))
main()
