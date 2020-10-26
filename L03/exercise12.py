#This program can be used to do simple calculations up to 100 times

def main():
    print("------------------------------------------------------")
    print("This program allows you to do simple calculations")
    print("------------------------------------------------------")
    i=1
    while i<=100:
        try:
            calc = eval(input("Enter the calculation or press <enter> to finish: "))
            print("Result: ", round(calc,2))
        except:
            break
        i+=1
    print("------------------------------------------------------")
    print("Goodbye! :) ")
    print("------------------------------------------------------")
main()
