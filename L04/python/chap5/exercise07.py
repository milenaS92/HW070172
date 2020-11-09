# This program encodes a message with a given key

def main():
#get message and key
    msgIn = input("Insert the message: ")
    key = int(input("Insert the key: "))

#create list with alphabet
    alphabet = []
    letter = "a"
    for i in range(26):
        alphabet.append(letter)
        letter = chr(ord(letter)+1)

#encode and print the final message
    msgOut = ""
    for ch in msgIn:
        msgOut += chr(ord(ch)+key)
    print("Coded message: ", msgOut)
main()
