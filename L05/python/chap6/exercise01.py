#exercise01 chap6
def farm():
    return("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")


def oldMac(animal,sound):
    song = farm() + "And on that farm he had a " + animal +", Ee-igh, Ee-igh, Oh!\n"
    song += "With a " + sound + ", "+ sound + " here and a " + sound + ", "+ sound + " there.\n"
    song += "Here a "+ sound + ", "+ "there a "+ sound + ", everywhere a "+ sound + ", "+ sound+ ".\n"
    song += farm()
    return song

def main():
    print(" ")
    animals = {"cow": "moo", "chick": "cluck", "sheep": "baa", "pig": "oink", "duck": "quack"}
    for key, value in animals.items():
        print(oldMac(key,value))

main()
