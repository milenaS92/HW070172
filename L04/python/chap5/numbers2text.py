#numbers2text

def main():
    message = input("Please enter the coded message: ")
    output = ""
    for nr in message.split():
        char = chr(int(nr))
        output += char
    print(output)
main()

# 66 117 101 110 111 115 32 100 237 97 115 33
