# File: chaos.py
# A simpole program illustrating chaotic behavior.

def main():
  print("This program illustrates a chaotic function")
  x = eval(input("Enter a number between 0 and 1: "))
  n = int(input("How many numbers should I print? "))
  for i in range(n):
    x = 3.9 * x * (1 - x)
    print(x)
main()
