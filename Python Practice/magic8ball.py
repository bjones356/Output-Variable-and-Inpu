#magic 8 ball program
def createdBy():
  print('Created by Ben Jones')
# generates random answers
def getResponse ():
  import random
  rndnum = random.randrange(1,10)
  if rndnum == 1: 
    print ('It is certain.')
  elif rndnum == 2: 
    print ('It is decidedly so.')
  elif rndnum == 3: 
    print ('Without a doubt.')
  elif rndnum == 4: 
    print ('Yes, definitely.')
  elif rndnum == 5: 
    print ('You, may rely on it.')
  elif rndnum == 6: 
    print ('As I see it, yes.')
  elif rndnum == 7: 
    print ('Most likely.')
  else:
    print ('Outlook good.')
#gets player name and welcomes to game
def getPlayerName(playerName='Player'):
  playerName = input ('Enter your name: ')
  print (f'Welcome to the magic 8 ball {playerName}')
  print ('Think of a yes or no question that you would like answered.')
  return 
#end game funttion
def endGame():
  print ('Thank you for playing.')
  createdBy()

#Start the game
getPlayerName()
play_begin = input ('Are you read to play? y/n ' )
#loop for game while player says yes
while play_begin == ('y' or 'yes'):
  if play_begin == ('y' or 'yes'):
    input ('What is your question?  Remember it has to be a yes or no question. \n')
    getResponse()
    play_begin = input('Would you like to play again? y/n ')
  else:
    break
  
endGame()   

