#Zombie Games
weapons = ['sword', 'gun', 'dagger', 'axe', 'bat', 'spear']
zombieWeakness = ('sword')
print ('You have encountered a Zombie!  Prepare to fight!!!!! ')
print ('You have the following weapons at your disposal: ' + "\n" + str(weapons))
choice = int(input('Type 1 to pick a weapon from the list\nor\nType 2 to choose a weapon of your own. '))
if choice == 1:
  print ('Choose your weapon from the list: ')
  weapons_choice = input ()
else:
  print ('Enter the weapon you prefer to use: ')
  new_weapon = input ()
  weapons.append (new_weapon)

if weapons_choice == zombieWeakness:
  print ('You have chosen wisely. You defeated the Zombie!!!!')
else:
  print ('You have chosen poorly. The zombie has eaten your brains.')
