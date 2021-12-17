import time, os

phoneSales = []

try: 
  f = open('sales.txt', 'r')
  phoneSales = eval(f.readline())
  f.close()
except:
  pass
  
def addSale():
  item = input ('Item: ')
  price= float(input('Price: '))
  quantity = int(input('Quantity: '))
  total = round(price*quantity, 2)

  row = [item, price, quantity, total]
  phoneSales.append (row)

  print ('Add Successfully')
  time.sleep(1)

def viewSales():
  print ('SALES HISTORY')
  for row in phoneSales:
    for item in row:
      print (item, end="\t")
    print()
  time.sleep(1)

while (True):
  print ('PHONE SALES')
  print ('===========')
  print ('Press 1 to add new Sale')
  print ('Press 2 to view Sales')
  menuChoice = input('> ')

  if (menuChoice == '1'):
    addSale()
  elif (menuChoice == '2'):
    viewSales()
  else: 
    print('ERROR: unknown option')
    time.sleep(1)

  time.sleep(1)
  os.system('clear')

  f = open('sales.txt', 'w')
  f.write (str(phoneSales))
  f.close()
