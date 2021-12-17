#Code predicts Love Connection
print ("Welcome to the love connector please enter your names below:")
name1 = input('Contestant one enter your name: ')
name2 = input('Contestant two enter your name: ')
nameLength_Total = (len(name1) + len(name2))
remainder = nameLength_Total%3

if remainder == 0:
    print('A match made in heaven')
elif remainder == 1: 
    print ('Its risky if you try!!')
else:
    print ('Not in a million years')

#Code Determines 
#num1 = int(input('Enter first number: '))
#print ('I will now determine if your number is divisible by 2')
#num2 = 2
#value = int(num1/num2)
#remainder = num1%num2

#if remainder == 0:
    #print ("your number is divisible by 2")
    #print (f'{num1} divided by {num2} is {value} with a remainder of {remainder}')
#else:
    #print ('Your number is not evenly divisible by 2')
    #print (f'{num1} divided by {num2} is {value} with a remainder of {remainder}')


#Code takes a number divider w remainder
#num1 = int(input('Enter first number: '))
#num2 = int(input('Enter second number: '))
#value = int(num1/num2)
#remainder = num1%num2
#print (f'{num1} divided by {num2} is {value} with a remainder of {remainder}')


#Code is a Random number generator
#import random
#def number_Inputs():
    #num1 = int(input('Please enter a number: '))
    #num2 = int(input('Please enter another number: '))
    #finalNumber = random.randint(num1,num2)
    #if (num1) >= (num2):
        #print ('error: number 2 needs to be larger than number 1.' )
        #print ('please try again')
        #return [number_Inputs()]
    #else:
        #print (finalNumber)

#number_Inputs()

#Code is a Dice Program
#import random
#print ('Welcome to the dice simulator!')

#num1 = random.randint(1,6)
#num2 = random.randint(1,6)
#numTotal = (num1 + num2)
#print (f'You rolled a {num1} and a {num2} for a total of {numTotal}')


#Code determines Area of a square
#def area():
    #total = num1 * num2 
    #print ("The area of  your square is " + str(total))
#num1 = float(input('Enter length of the side: '))
#num2 = float(input('Enter the height of another side: '))

#area ()