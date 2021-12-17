2name = input('First Name: ')
while name == (''):
  print ('ERROR: You must enter your name.')
  name = input('First Name: ')

lastName = input('Last Name: ')
while lastName == (''):
  print ('ERROR: You must enter your last name.')
  lastName = input('First Name: ')

mobileNum = input ('Cell Number: ')
while (len(mobileNum) != 10):
  print ('Error: Not the correct number of digits in the phone number' )
  mobileNum = input ('Cell Number: ')

gradYear = int(input('Graduation Year: '))
while (gradYear<20 or gradYear>25):
  print ('Error: Graduation year not correct') 
  gradYear = int(input('Graduation Year: '))

email = input('Email:   ')
while email == ('') or ('@'and'.' not in email): 
  print ('ERROR: email address is required.')
  email =input('Email:  ')

telephone = input('Telephone: ')
while (len(telephone) != 10):
  print ('ERROR: ten digits required for telephone number.')
  telephone = input('Telephone: ')

numberChoice = int(input('Enter a number 1-10: '))
while (numberChoice<1 or numberChoice>10):
  print ('ERROR:  Please enter a number 1-10: ')
  numberChoice = int(input('Enter a number 1-10: '))

actualSizes = ['s','m','l','xl']
size = input('Enter you t-shirt (s-xl): ')
while (size.lower() not in actualSizes):
  print ('ERROR: You must select S, M, L, or XL')
  size = input('Enter you t-shirt (s-xl): ')