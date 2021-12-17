mockebeast = []
entry = 0

while (True):
  entry += 1
  beastname = input('Enter the beast name: ')
  beast =['earth' ,'fire', 'water','air', 'spirit']
  beasttype = input('Enter the beast type (earth, fire, water, air, sprit): ')
  while beasttype.lower() not in beast:
    print ("Invalid beast type. Please enter correct beast type. ")
    beasttype = input('Enter the beast type: ')
  specialmove = input('Enter special move: ')
  headpoints = input('Headpoints: ')
  movepoints = input('Movepoints: ')
  
  row = [entry, beastname, beasttype, specialmove, headpoints, movepoints]
  mockebeast.append (row)

  print ('==Mockebeast Board==')
  for row in mockebeast:
    for item in row:
      print (item, end='\t')
    print ()
    
    
  