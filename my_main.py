import random
from art import logo

print(logo)
print('Welcom to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if(level == 'easy'):
  attempts = 10
elif level == 'hard':
  attempts = 5
else:
  print("Invalid Input")

randNumber = random.randint(1,100);

while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if(guess > randNumber):
    print("Too high.")
    attempts -= 1
  elif(guess < randNumber):
    print("Too Low.")
    attempts -= 1
  else:
    print("Correct. You Won")
    break

  if attempts <= 0:
    print("You Loose.") 
  else:
    print("Guess again.")
