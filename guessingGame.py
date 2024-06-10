import random
print('welcome to guessing game ')
game_on = True
num = random.randint(1,10)
print(num)
guessed = []
while game_on:

  gues = int(input('Gues a number between 1 and 10 :'))
  if gues not in guessed:
    if gues > num:

      print(gues ,'is too high')
      guessed.append(gues)
    
    elif gues<num:
      print(gues ,'is too low')
      guessed.append(gues)
    else:
      print('💥💥 You correctly guessed the number : ')
      game_on = False
  else:
    print('Already guessed !')
print('End of the game ...')



