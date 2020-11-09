#username.py
# Simple string processing program to generate usernames.

def main():
    print("***")

    first = input("Enter first name: ")
    last = input("Enter last name: ")

    uname = first[0] + last[:7]

    print("Your username is: ", uname)

main()
