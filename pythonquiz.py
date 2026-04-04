name = input("What is your name? ")
print ("Hello " + str(name))
done = False
def quiz():
  right = 0
  firstq = int(input("Whats 5+1? "))
  if(firstq == int(6)):
    right = right+1
  else:
    print("Try again")
    quiz()
  secondq = int(input("Whats 6+1? "))
  if(secondq == int(7)):
    right = right+1
  else:
    print("Try again")
    quiz()
  thirdq = int(input("Whats 50+17? "))
  if(thirdq == int(67)):
    right = right+1
  else:
    print("Try again")
    quiz()
  fourthq = int(input("10? "))
  if(fourthq == int(10)):
    right = right+1
  else:
    print("Try again")
    quiz()
  fifthq = int(input("Whats 2+5? "))
  if(fifthq == int(7)):
    right = right+1
  else:
    print("Try again")
    quiz()
  sixthq = int(input("Whats 9+2? "))
  if(sixthq == int(11)):
    right = right+1
  else:
    print("Try again")
    quiz()
  print (str(name) + ", you got " + str(right) + " right." )
  if(right == 6):
    print("67!!!!")
    done = True
if (done == False):
  quiz()
  
