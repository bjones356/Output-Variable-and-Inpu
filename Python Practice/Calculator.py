

def add(num_1):
    print (final)
    print (first + second)
def subtract(num_2):
    print (final)
    print (first - second)
def multiply (num_3):
    print (final)
    print (first * second)
def divide (num_4):
    print (final)
    print (first / second)

while True:
  
  first = int(input("Enter first number: "))
  second = int(input("Enter the second number: ")) 
  final = ('Your final answer is ')
  choice = int(input('Enter a number a number 1-4 for the following choices:\n'
  "1 = add\n"
  "2 = subtract\n"  
  "3 = multiply\n"
  "4 = divide\n"))
  if choice == 1:
    add(first)
  if choice == 2:
    subtract(first)
  if choice == 3:
    multiply(first)
  if choice == 4:
    divide(first)
  


  cont = input("Another one? yes/no > ")
  while cont.lower() not in ("yes","no"):
        cont = input("Another one? yes/no > ")
  if cont == "no":
    break



