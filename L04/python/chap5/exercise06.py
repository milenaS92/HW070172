# This program calculates the "numeric value" of a name
# (same as in exercise 05)

def main():
    name = input("Please enter the name: ").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = 0
    value = 0
    for i in name:
        for j in alphabet:
            if i == j:
                #print(pos+1)
                value += (pos+1)
            pos += 1
        pos = 0
    print("The 'numeric value' of the name is: ",value)
main()
