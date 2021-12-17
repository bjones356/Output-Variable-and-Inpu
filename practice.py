#finding the smallest value in list
smallest = None
print ('Before')
for value in [9,15,21,5,76,91]:
  if smallest is None:
    smallest = value
  elif value < smallest:
     smallest = value
  print (smallest, value)
    
print ('After',smallest)

num = 0
tot =0.0
while True:
  sval = input('Enter a number: ')
  if sval == 'done':
    break
  try:
    fval = float(sval)
  except:
    print ('Invalid Input')
    continue
  #print (fval)
  num = num + 1
  tot = tot + fval
#print ('Done')
print (num, tot, tot/num)