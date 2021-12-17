customersrental = [] 
customers=[]

try:  
  f = open('gamerentals.txt', 'r')
  customersrental = eval(f.readline())
  f.close()
  f = open('customer.txt', 'r')
  customers= eval(f.readline())
  f.close()
except:
  pass
  
def customerRent():
  customerName = input('Name: ')
  game= input('Game: ')
  phone=  int(input('Phone #: '))

  row = [customerName, game, phone]
  customersrental.append (row)
  row1 = [customerName, phone]
  customers.append(row1)

customerRent()

print (customers)

f= open('gamerentals.txt', 'w')
f.write (str(customersrental))
f.close()

f= open('customer.txt', 'w')
f.write(str(customers))
f.close()

#if new_name in names:  
  #names.remove (new_name)
  #names.append (new_name)
#else:
  #names.append (new_name)