# This program creates an acronym for the entered phrase

def main():
    phrase = input("Please enter the words for the acronym: ")
    acro = ""
    for word in phrase.split():
        acro += word[0]
    print("Acronym: ", acro.upper())
main()
