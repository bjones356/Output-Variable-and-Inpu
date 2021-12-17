list = ['pencil', 'calculator', 'eraser', 'ruler','pen']
itemLookingfor = input('What are you looking for? ')
counter = 0

#found = False

while counter < len(list):
  if list[counter] == itemLookingfor:
    found = True

  counter +=1
  if itemLookingfor not in list:
    print(itemLookingfor + ' has not been found on the list.')
    itemLookingfor = input('Try again. ')
#if found == True
  if itemLookingfor in list:
    print (itemLookingfor + ' has been found on the list.')
    break

  #else:
    #print (itemLookingfor + ' was not found on the the list.')