# A program to convert Celsius temps to Farenheit, runs 5 times

def main():
    print("********************************************************")
    print("This program converts Celsius temperature into Farenheit")
    print("********************************************************")

    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        farenheit = 9/5 * celsius + 32
        print("The temperature is", farenheit, "degrees Farenheit.")

main()
