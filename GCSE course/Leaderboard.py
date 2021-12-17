leaderboard = []

while (True):
  name = input ('Enter your name: ')
  email = input ('Enter your email: ')
  bestScore = int(input('Enter your highScore: '))

  row = [name,email,bestScore]
  leaderboard.append(row)

  print ('==LEADERBOARD==')
  for row in leaderboard:
    for item in row:
      print (item, end='\t')
    print ()
