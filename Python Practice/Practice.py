videoGames = ['Mario', 'Zelda', 'Sonic', 'Joust']
new_game = input('Enter the name of your favorite video game:  ')
while new_game in videoGames:
  print ("We already have that game in our list.")
  new_game = input('Enter the name of your favorite video game:  ')
if new_game in videoGames:  
  videoGames.remove (new_game)
  videoGames.append (new_game)
else:
  videoGames.append (new_game)
print (videoGames)
print ("Thankyou for you input. Would you like to add another game?")

while True:
    a = input("Enter yes/no to continue")
    if a=="yes":
        videoGames = ['Mario', 'Zelda', 'Sonic', 'Joust']
        new_game = input('Enter the name of your favorite video game:  ')
        while new_game in videoGames:
          print ("We already have that game in our list.")
          new_game = input('Enter the name of your favorite video game:  ')
        if new_game in videoGames:  
          videoGames.remove (new_game)
          videoGames.append (new_game)
        else:
          videoGames.append (new_game)
          print (videoGames)
          print ("Thankyou for you input. Would you like to add another game?")
        continue
    elif a=="no":
        break
    else:
        print("Enter either yes/no ")

print ('Thankyou for your input')
 


#Practice making lists
#squareNumbers = [1, 4, 9, 16, 25, 36, 49]
#squareNumbers [0] +=1
#print (squareNumbers [1])
#total = squareNumbers [2] + squareNumbers [3]
#print (total)
#squareNumbers.append ('64')
#squareNumbers.insert (3,"0")
#print (squareNumbers [3])

#program picks random fruit
#fruit = ['apple', 'banana', 'mango', 'orange', 'melon']
#input = int(input('Enter a number 0 to 4: '))
#print (fruit [input])

#print (fruit [0] + " " + fruit[3])
#fruit [3] = 'lime'
#print (fruit [3])
#print (fruit)
#This program cubes any number entered
#num_1 = int(input('Enter a number: '))
#counter = 1
#while counter <= 5:
 #  print (counter)
  # counter = counter + 1
#output = (num_1**3)
#print (output)

#plication program
#x = int(input('Enter 1st number: '))
#y = int(input('Enter 2nd number: '))
#output = x * y

#print ((x), "*" ,(y) ,'=' , output)

#((x) + '*' + (y) + "="(output))
 

#print (counter * mult_num)
#counter = 10
#while counter > 8
#print counter
#print ('The counter is done.')

#number guessing game
#number = (input('Guess the number between 1 and 10 that I am thinking. '))

#while number != "5":
  #print ('Incorrect, Try again!')
  #print ('Guess the number between 1 and 10 that I am thinking. ')
  #number = input()

#print ('Congratulations! That is correct.')


#Insult Generator
#name = (input('What is your name? '))
#num_1 = int(input('Input a number between 1 and 5: '))

#if num_1 == 1:
  #print ('Hi ' + (name)+', ' + "if I had a dog that looked like you I would shave his butt and teach him to walk backward." )
#elif num_1 == 2:
  #print ('Hi ' + (name)+', ' + "Your stupid." )
#elif num_1 == 3:
  #print ('Hi ' + (name)+', ' + "Whats your problem?" )
#elif num_1 == 4:
  #print ('Hi ' + (name)+', ' + "Dumb and ugly....a bad combo." )
#else:
  #print ('Hi ' + (name)+', ' + "I'm glad I'm not as dumb as you look.") 
#answer = (input('Play again? yes or no : '))
#while answer != 'yes ':
  #num_1 = int(input('Input a number between 1 and 5: '))
  #answer =(input)

#print ('See ya next time')

#while answer = 'yes'
#num_1 = int(input('Input a number between 1 and 5: '))

#program for picking a class and room
#name = (input ('What is your name? '))
#subject = (input("Please enter which subject you are studying: spanish, math, science? " ))
#if subject == "spanish":
  #print ('Hi ' + (name) + ' Go to room 101' )
#elif subject == "math":
  #print ('Hi ' + (name) +' Go to room 102' )
#elif subject == "science":
  #print ('Hi ' + (name) +' Go to room 103' )
#else: 
  #print ('That subject is not offered')

#program enter number 1-10
#num_1 = int(input('Player 1 - Enter a number between 1 and 10 ')) 
#num_2 = int(input('Player 2 - Enter a number between 1 and 10 '))
#if num_1 > num_2:
 #print (str(num_1) +" is bigger.")
#elif num_1 < num_2:
 #print (str(num_2) +" is bigger.")
#else: 
 #print ('The numbers are equal!')

#This Program is a gradescale
#fail = range(1, 40, 1)
#C= range(40,59,1)
#B= range(60, 79,1)
#A= range(80, 100,1)
#number = int(input('Enter the grade of the test '))
#if number in fail:
 # print ('retake test')
#else :
 # print ('Good Score')

#if number in fail:
 # print ('grade = U ')
#if number in C:
 # print ('grade = C ')
#if number in B:
 # print ('grade = B ')
#if number in A:
 # print ('grade = A ')
#if test >= 41: 
 # print ('passing')
#else:
  #print ('Retake Required')

#This program finds the area of a cube
#height = int(input ('Enter the height of the object. '))
#length = int(input ('Enter the length of the object. '))
#width = int(input ('Enter the width of the object. '))
#volume = height * length * width
#print ("The volume of your object is " + str(volume))

#num1 = 5
#num2 = 40
#result = num1 * num2
#print (result)

#print (8//3)

#score = 10
#score = score+1
#print (score)

#This program finds a %20 tip for a meal
#num1 = int(input('Enter the cost of your meal '))
#num2 = .20
#tip = (num1 * num2)

#output = ((num1 * num2) + num1)
#print (num1)
#print ('Your tip at 20% should be $'+str(tip))
#print ('Your total cost is $' + str(output))


#food1 = 'tacos'
#food2 = 'ice cream'
#print ("My favorite food is " + (food1) ,"and", (food2)) 

#print ('hi what\'s your name')
#name ='Dave'
#print (('Hi ') + (name) + ('! How are you today?'))

#print ('What\'s your name?')
#name =(input)
#name = input('What\'s your name?')
#print ('Good morning ' +(name)+ '.')
#print()
#Age =input('How old are you?')
#Birth = input('What is your birtdate?')
#Experience =input('How long have you been programming?')
#print ((name) + ', according to our survey you are '+(Age)+ ' and were born on ' +(Birth)+ ' and have been programming ' +(Experience)+ '.')
#print ('Is that correct?')