# exercise 1 chap 7

def wagesCalc(hours,rate):
    wages = 0.0
    if hours > 40:
        extraH = hours - 40
        wages = 40 * rate + extraH * rate * 1.5
    else:
        wages = hours * rate
    return wages

def main():
    hours = float(input("Please enter the number of hours worked in a week: "))
    ratePH = float(input("Please enter the rate per hour: "))
    wages = wagesCalc(hours,ratePH)
    print("The total wages for the week is:",round(wages,2))
main()
