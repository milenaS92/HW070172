# exercise 6 chap 7

def speedControll(mph,limit):
    if mph > limit:
        fine = 50 + 5 * (mph-limit)
        print(fine)
        if mph > 90:
            fine += 200
        return fine
    else:
        return 0

def main():
    limit = int(input("Please enter the speed limit in mph: "))
    mph = int(input("Please enter the clocked speed in mph: "))
    fine = speedControll(mph, limit)
    if fine > 0:
        print("The fine to charge is:",fine)
    else:
        print("The entered speed is legal :)")
main()
