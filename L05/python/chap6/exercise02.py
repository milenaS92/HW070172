#exercise 2 chap 6

def intro(number):
    song = ("The ants go marching "+number+" by "+number+", hurrah! hurrah!\n")*2
    song += "The ants go marching "+number+" by "+number+","
    return song

def littleOne(phrase):
    song = "The little one stops to "+ phrase+","
    return song

def end():
    song = "And they all go marching down...\n"
    song += "In the ground...\n"+"To get out...\n"+"Of the rain.\n"
    song += "Boom! "*3+"\n"
    return song

def main():
    print("\nThe Ants Go Marching\n")
    #numbers=["one", "two", "three", "four", "five", "six", "seven", "eight", "nein", "ten"]
    rimesLittleOne = {"one": "suck his thumb", "two": "tie his shoe", "three": "climb a tree", "four": "shut the door", "five": "take a dive", "six": "pick up sticks", "seven": "pray to heaven", "eight": "roller skate", "nine": "ckeck the time", "ten": "to shout 'The End',"}
    for key, value in rimesLittleOne.items():
        print(intro(key))
        print(littleOne(value))
        print(end())

main()
