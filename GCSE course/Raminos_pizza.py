import time, os, sys

def finalCharge():
  if counter < 3:
    final_price = totPrice + deliveryFee
    print(f'Amount due: {final_price}')
  if counter >= 3:
    final_price = (totPrice + deliveryFee)
    discount_price =  round(final_price - (.3 * final_price), 2)
    print (f'You recieved a 33% discount for your order -Amount due: {discount_price} ')
#Inro Screen
print (" WELCOME TO \n\n Ramino's\n  Pizza\n")
print ('Your place for the best pizza in town.\n')
print ("Order 3 or more Pizza's and get 33% off!")
time.sleep(2)
os.system('clear')
order_more = ('y')
price = 0
totPrice =0.0

#ordering your pizza
counter = 0
while order_more == ('y'):
  counter = counter + 1
  if order_more == ('n'):
    break
 
  print ('Place your order\n')
  #order your size
  actualSizes = ['1','2','3',]
  size = input('Pick your size\nEnter: 1 for small, 2 for medium, 3 for large: ')
  while size not in actualSizes:
    print ("ERROR: You must pick your size by entering 1 for small, 2 for medium, 3 for large: ")
    size = input('Pick your size\nEnter: 1 for small, 2 for medium, 3 for large: ')
  
  actualStyle = ['t', 'p', 'i']
  style= input('Pick your style of crust\nEnter T for thin, I for Italian, P for pan: ')
  while style.lower() not in actualStyle:
    print ('ERROR: You must pick your style by entering T for thin, I for Italian, P for pan: ')
    style= input('Pick your style of crust\nEnter T for thin, I for Italian, P for pan: ')

  if size == '1':
    if style == 't':
      price =  float(4.99)
    elif style == 'i':
      price = float(5.49)
    elif style == 'p':
      price = float(5.99)
  if size == '2':
    if style == 't':
      price =  float(7.99)
    elif style == 'i':
      price = float(8.49)
    elif style == 'p':
      price = float(9.99)
  if size == '3':
    if style == 't':
      price =  float(10.99)
    elif style == 'i':
      price = float(12.49)
    elif style == 'p':
      price = float(13.99)
  price = price + 0
  totPrice = totPrice + price
  print (f'The cost of your order so far is {totPrice}')

  order_more = input('Would you like to order another pizza? y/n ')

#option of delivery or Pickuup
print('\nChoose Delivery or Pickup.  There is a .99$ charge for delivery')
delivery = input('Enter 1 for Delivery or 2 for pickup at our store: ')

#option of rush on pizza
print ('\nIf you would like your order rushed we can do that for a small fee!   3.99$ for delivery orders and 1.99$ for pickup')
rush = input('would you like your order rushed: y/n ')

#deliveryFee = 0
#determine cost of delivery and rush

if delivery == '1':
  if rush.lower() == ('y'):
     deliveryFee = float(3.99)
  elif rush.lower() == ('n'):
     deliveryFee = float(.99)
  

if delivery == '2':
  if rush.lower() == ('y'):
    deliveryFee = float(1.99)
  elif rush.lower() == ('n'):
    deliveryFee = float(0.0)
  
#Calculate final price
finalCharge()