def greet(lang):
  if lang == '1': 
    return ('Hola')
  elif lang == '2':
    return ('Bounjour')
  else:
    return ('Hello')

name = input('What is your name?  ')
print ('Please chooose your language.')
lang = input('Choose 1 for Spanish\nChoose 2 for French\nChoose 3 for English\nChoice:?  ')

print (greet(lang), (name))
