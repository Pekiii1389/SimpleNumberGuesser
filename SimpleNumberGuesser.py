#SimpleNumberGuesser
import random

while True:
 while True:
  # Input of number
  number = int(input("Guess which number am i thinking of (1 to 10): "))
  if number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
     break
  else:
     print("Invalid input.")

 # Program generating his number
 randomnumber = random.randint(1, 10)

 # Checking and printing the answer
 if number == randomnumber:
    print("You guessed it right!")
 else:
    print("Wrong guess, you lost :)")

 # Option for repeating the process or shutting down
 another_try = input("Do you want to try another one? (Y/N): ").capitalize()
 if another_try != 'Y':
        break