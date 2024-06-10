import random
print('welcome to guessing game ')
num = random.randint(1,10)
guessed = []
play_again=True
game_on = True
allowed_attempts = 3
games_played=1
number_of_wins = 0
while game_on:
    
  while allowed_attempts > 0:
    gues = int(input('Gues a number between 1 and 10 :'))
    if gues not in guessed:
      if gues > num:

        print(gues ,'is too high')
        guessed.append(gues)
        allowed_attempts -=1
      
      elif gues<num:
        print(gues ,'is too low')
        guessed.append(gues)
        allowed_attempts -=1
      else:
        print('💥💥 You correctly guessed the number : ')
        allowed_attempts=0
        number_of_wins +=1

    else:
      print('Already guessed !')

  again = input('Would you like to play again Y/N :')

  if again == 'Y' or again == 'y':
    num = random.randint(1,10)
    allowed_attempts=3
    games_played +=1
    guessed=[]
  else:
    game_on = False
    print('You played :',games_played)
    print('You won :',number_of_wins)
    print('You lost :',games_played - number_of_wins)
    print('End of the game ...')
    print('Thanks👍🏽👍🏽👍🏽')



