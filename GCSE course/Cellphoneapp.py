#program calculates the cost of a cell phone from a list of two differnt phones and sizes
#funtion calculates monthly cost of phone
def billStatement ():
  monthlyCost = ((cost/contractLength) + 10) 
  print (f'Your monthly bill wll be {round(monthlyCost,2)}$ for {contractLength} months.') 

custName = input('Enter your name: ')

actualPhones = ['iphone 12','iphone 12 pro']
phone= input('Name of phone (iPhone 12 or iPhone 12 Pro): ')
while (phone.lower() not in actualPhones):
  print ('ERROR: That is not a phone in our list. Try again. ') 
  phone= input('Name of phone (iPhone 12 or iPhonPhone 12 Pro): ')
#if you choose iphone 12   
if (phone == 'iphone 12'):
  actualSizes =['mini', 'reg', 'max']
  phoneSize= input('Size of phone (Mini, Reg, Max):  ')
  while (phoneSize.lower() not in actualSizes):
    print ('Sizes are incorrect Please Try again')
    phoneSize= input('Size of phone (mini, reg, max):  ')
  contractLength = int(input('Length of contract in months: '))
  if (phoneSize == "mini"):
        print ('799.99$ for the phone with a 10$ monthly charge.')
        cost = float(799.99)
        billStatement()
  elif (phoneSize == 'reg'):
        print ('999.99$ for the phone with a 10$ monthly charge.')
        cost = float(999.99)
        billStatement()
  else: 
        print ('Incorrect size iphone 12 does not come in that size.')
        phoneSize= input('Size of phone (mini, reg, max):  ')
#if you choose iphone 12 pro
if (phone == 'iphone 12 pro'):
  actualSizes =['mini', 'reg', 'max']
  phoneSize= input('Size of phone (Mini, Reg, Max):  ')
  while (phoneSize.lower() not in actualSizes):
    print ('Sizes are incorrect Please Try again')
    phoneSize= input('Size of phone (mini, reg, max):  ')
  contractLength = int(input('Length of contract in months: '))
  if (phoneSize == 'reg'):
        print ('1099.99$ for the phone with a 10$ monthly charge.')
        cost = float(1099.99)
        billStatement()
  elif (phoneSize == 'max'):
        print ('1190.00$ for the phone with a 10$ monthly charge.')
        cost = float(1190.00)
        billStatement()
  else: 
        print ('Incorrect size iphone 12 pro does not come in that size.')
        phoneSize= input('Size of phone (mini, reg, max):  ')