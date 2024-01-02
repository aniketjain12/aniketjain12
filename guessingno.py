import math
import random

num1 = True
num2 = True
while num1 and num2 == True:

  try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
  except:
    print('Please enter Number!!!')
    continue
  else:
    break
x = random.randint(num1,num2)
c=round(math.log(num2-num1+1,2))
print("You have {} chances".format(c))
count = 0
while count < c:
  count +=1
  guess=int(input("Enter Guess no."))
  
  if x == guess:
    print("You won by {} chances".format(count-1))
    break
  elif x>guess:
    print("You are short")

  elif x<guess:
    print("You are Higher")

if count >= c:
  print("Wrong")

  