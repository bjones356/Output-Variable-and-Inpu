name_Input = input('Enter your name: ')

myFile= open('test.txt','a')
myFile.write (name_Input + "\n")
myFile.close ()

nameList = []
while name_Input in nameList:
  print ("We already have that name in our list.")
  name_Input = input('Enter your name: ')
if name_Input in nameList:  
  nameList.remove (name_Input)
  nameList.append (name_Input)
else:
  nameList.append (name_Input)
print (nameList)
#print ("Thankyou for you input. Would you like to add another game?")
myFile=open ('test.txt', 'r')
for line in myFile:
  print (line)
myFile.close ()