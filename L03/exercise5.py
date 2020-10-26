# A program to compare Celsius and Farenheit temperatures

def main():
    print("********************************************************")
    print("This program compares Celsius and Farenheit temperatures")
    print("********************************************************")

    for i in range(0, 110, 10):
        celsius = float(i)
        farenheit = 9/5 * celsius + 32
        if celsius<10:
            print("Celsius: ", celsius, "   Farenheit: ", farenheit)
        elif celsius>=10 and celsius<100:
            print("Celsius: ", celsius, "  Farenheit: ", farenheit)
        else:
            print("Celsius: ", celsius, " Farenheit: ", farenheit)
main()
