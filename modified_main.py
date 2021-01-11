import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check guess
def checkAnswer(guess , answer, turns):
  if(guess > answer):
    print("Too high.")
    return turns - 1
  elif(guess < answer):
    print("Too Low.")
    return turns - 1
  else:
    print("Correct. You Won")
    return -1

#function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if(level == 'easy'):
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def game():
  print(logo)
  print('Welcom to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100")

  randNumber = random.randint(1,100);
  print(randNumber)
  attempts = set_difficulty()
  guess = 0
  while guess != randNumber:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = checkAnswer(guess,randNumber,attempts)
    
    if attempts == -1:
      return
    elif attempts <= 0:
      print("You Loose.") 
      return
    else:
      print("Guess again.")

game()
