# dateconvert.py
#    Converts a date in form "mm/dd/yyyy" to "month day, year"

def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/year): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    monthStr = months[int(monthStr)-1]

    # output the result in month day, year format
    print("The date is {0} {1}, {2}".format(monthStr,dayStr,yearStr))

main()
