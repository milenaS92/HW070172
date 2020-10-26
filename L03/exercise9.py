# A program to convert Farenheit temperature into Celsius

def main():
    print("********************************************************")
    print("This program converts Farenheit temperature into Celsius")
    print("********************************************************")
    farenheit = eval(input("What is the Farenheit temperature? "))
    celsius = (farenheit - 32)* (5/9)
    print("The temperature is", round(celsius,2), "degrees Celsius.")

main()
