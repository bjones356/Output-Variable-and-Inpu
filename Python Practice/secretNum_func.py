def CompareGuess (playerGuess):
  secretNum = 7
  if playerGuess < secretNum:
    print ('You guessed too low!')
  elif playerGuess > secretNum:
    print ('You guessed too high!')
  else:
    print ('You guessed it correct! Congratulations!')

numGuess = int(input('Enter a number between 1-10: '))

CompareGuess(numGuess)