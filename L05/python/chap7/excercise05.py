# exercise 5 chap 7

def bmiCalc(weight, height):
    bmi = weight * 720 / (height**2)
    if bmi < 19:
        return "below the healthy range"
    elif bmi < 26:
        return "within the healthy range"
    else:
        return "above the healthy range"

def main():
    weight = float(input("Please enter your weight in pounds: "))
    height = float(input("Please enter your height in inches: "))
    print("Your BMI is", bmiCalc(weight, height))
main()
