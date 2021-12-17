names = ['Ben', 'Tim', 'Ed', 'Adam', 'Jo', 'Frank', 'Randy', 'Justin', 'Daryl', 'Matt']
num1 = int(input('Enter 1 for to print all the names.\nEnter 2 to print the first 5 names.\nEnter 3 to print the last 5 names.\nEnter:  '))
if num1 == 1:
    print (names)
if num1 == 2:
    print (names[0:4])
if num1 ==3:
    print (names[5:9] )
 
while True:
    a = input('Would you like another list. y/n  ')
    if input == ('y'):
      num1 = int(input('Enter 1 for to print all the names.\nEnter 2 to print the first 5 names.\nEnter 3 to print the last 5 names.\nEnter:  '))
      if num1 == 1:
        print (names)
      if num1 == 2:
        print (names[0:4])
      if num1 ==3:
          print (names[5:9])
      continue
    elif a ==('n'):
      break
    
print ('thanks')

  

  #str(input('Would you like another list? y/n  ' ))
  #if input == ('n'):
    #break
    #print ('thanks')
  #elif input == ('y'):
    #continue



#names = ['Ben', 'Tim', 'Ed', 'Adam', 'Jo', 'Frank', 'Randy', 'Justin', 'Daryl', 'Matt']
#num1 = int(input ('Enter a number 0 - 9.  '))


#if num1 < 0 or num1 > 8:
 # num1 = int(input ('That number does not work. Enter a number 0 - 8.  '))

#num2 = int(input ('Enter a second number between 0-9.  Make it bigger than the first number. '))

#if num2 <= num1 or num1 > 9:
 # num2 = int(input ('That number does not work. Enter a second number between 0-9.  Make it bigger than the first number. '))

#print (names[num1:num2])



#names = ['Ben', 'Tim', 'Ed', 'Adam', 'Jo']
#new_name = input('Enter your name: ')
#if new_name in names:  
  #names.remove (new_name)
  #names.append (new_name)
#else:
  #names.append (new_name)
#number = input('Enter a number 0-4: ')
#names.insert(int(number), new_name)
#print (names)