#convert.py
# A program to convert Celsius temps to Farenheit

def main():
    print("********************************************************")
    print("This program converts Celsius temperature into Farenheit")
    print("********************************************************")
    celsius = eval(input("What is the Celsius temperature? "))
    farenheit = 9/5 * celsius + 32
    print("The temperature is", farenheit, "degrees Farenheit.")
    input("Press the <Enter> key to quit.")

main()
