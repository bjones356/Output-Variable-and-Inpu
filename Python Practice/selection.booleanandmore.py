newPassword1 = input("Enter your new password that is at least 8 characters long: ")
newPassword2 = input("Verify your new password: ")

while newPassword1 != newPassword2 or len(newPassword1) <= 8 :
    newPassword1 = input('Passwords do not match or fit requirements: ')
    newPassword2 = input("Verify your new password: ")

if newPassword1 == newPassword2 and len(newPassword1) >= 8:
    print ("Thankyou, you have a new password.")

#Code ask for password
#password = "bjones"
#userInput1 = input("Enter your password: ")
#userInput2 = input("Reenter your password to Confirm: ")

#while userInput1 != password:
    #userInput1 = input("Incorrect password: \n Enter your password: ")

#userInput2 = input("Reenter your password to Confirm: ")
#while userInput1 != userInput2:
    #userInput2 = input("Your passwords did not match. Reenter your password to confirm: ")
    
#if userInput1 == userInput2: 
    #print ('Access Granted')
#print ("Welcome")


#Code asks for birth date
#monthBorn = int(input('Enter the number of the month you were you born? '))

#while monthBorn < 1 or monthBorn > 12:
    #monthBorn = int(input("There are no months that fit that number \n Try again: "))

#print ("Thank you for you input.")

#Code ask for a number in a range
#num1 = int(input("Enter a number between  1 and 50: "))

#while num1 < 0 or num1 > 50:
    #num1 = int(input("That number is not between 1 and 50. Enter a number between  1 and 50: "))

#print ("Thank you, your number is in the range.")