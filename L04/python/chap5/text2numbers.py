#text2numbers.py

def main():
    print("*****")
    message = input("Enter the message to encode: ")

    for ch in message:
        print(ord(ch),end=" ")
main()
