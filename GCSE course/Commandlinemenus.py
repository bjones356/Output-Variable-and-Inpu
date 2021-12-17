import time, os, sys

def createAccount():
  print ('Our books section is coming soon, you might need to go into an actual store until then. Sorry.')
  pass

def logIn():
  print('Yeah, sorry. It\'s Netflix or your local multiplex until our developer sorts themselves out. Sorry.')
  pass

print (' WELCOME TO \n\n Sherwood\n  Prime\n')
print ('Your place for one stop shopping\n')
time.sleep(2)
os.system('clear')

while (True):
  print ('Press 1 for books.')
  print ('Press 2 for movies.')
  print ('Press 3 your account.')
  print ('Press 4 to logout')

  menuSelection = input("> ")

  if (menuSelection == '1'):
    createAccount()
  elif (menuSelection == '2'):
    logIn()
  elif (menuSelection == '4'):
    sys.exit('Goodbye')
  else: ('ERROR: Unknown Selection, try again.')
  pass

  time.sleep(3)
  os.system('clear')