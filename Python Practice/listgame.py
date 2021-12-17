uclgoal_list = ['Ronaldo', 'Messi', 'Lewandowski', 'Benzema', 'Raul', 'Van Nistelrooy', 'Henry']

userGuess =  input('Name one of the top goal scorers of all time in Champions League soccer. ')
lower_userGuess = userGuess.lower()
is_userGuess_inlist = lower_userGuess in (string.lower() for string in uclgoal_list)

def check_list():
  if lower_userGuess in (string.lower() for string in uclgoal_list):
    print ('Correct! He is one of the all time greats!')
  continue    
  elif lower_userGuess not in (string.lower() for string in uclgoal_list):
    print ('Sorry, he is not on the list.')
    entry_try_again = (input('would you like to try again? Y/N '))
  else:
    entry_try_again = (input('would you like to try again? Y/N '))

check_list()
while entry_try_again == 'y' or 'Y':
  entry_try_again = (input('would you like to try again? Y/N '))
  if entry_try_again == 'y' or "Y":
    userGuess =  input('Name one of the top goal scorers of all time in Champions League soccer. ')
  check_list()
else:
  print ('Thank you for playing')
#try_again = (input('would you like to try again? Y/N '))
#while True:
  #check_list()


  


 