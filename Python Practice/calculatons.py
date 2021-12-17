def Total_price():
  total_price = (itemPrice * itemQuantity) 
  print (f'Total Price = {round(total_price,2)}$')
#Simple Cost calculaor
itemName = input('Input item name: ')
while itemName == (''):
  print ('ERROR: you must enter an item.')
  itemName = input('Input item name: ')
 
#itemPrice= float(input('Input item price: '))
while (True):
  try: 
    itemPrice = float(input('Input item price: '))
    break
  except ValueError:
    print ('ERROR: you must enter a price.')
    continue

itemQuantity= int(input('Input quantity needed: '))
while itemQuantity == (''):
  print ('ERROR:  You must enter a quantity.')
  itemQuantity= int(input('Input quantity needed: '))
  

Total_price ()
if itemQuantity > 10:
  total_price = (itemPrice * itemQuantity) 
  discount = total_price * .1 
  finalPrice= total_price - discount
  print (f'With your 10% discount you get {round (discount,2)} dollars off.')
  print (f'Your final price is {round(finalPrice,2)}$. ')
else:
  print ('Thankyou for your business.')