import random
import time

crimes = ["theft", "arson", "murder", "robbery", "treason"]
punishments = ["hanged", "drawn and quartered", "beheaded", "jailed"]

count = 0

def crimejudge():
    if count == 1:
       print("You have judged " + str(count) + " man.")
       time.sleep(2)
       print("The next man is guilty of " + random.choice(crimes) + ".")
       time.sleep(2)
    else:
       print("You have judged " + str(count) + " men.")
       time.sleep(2)
       print("The next man is guilty of " + random.choice(crimes) + ".")
       time.sleep(2)

def condemnation():
   if Response == "yes":
       print("The man has been condemned and sentenced to be " + random.choice(punishments) + ".")
   elif Response == "no":
       print("The man has been spared a fate most gruesome.")
   else:
       print("The man has fled.")

def closecourt():
    response2 = input("Would you like to close court?")
    if response2 == "yes":
        exit(1)
    else: exit(1)


print("There are ten men that need to be judged this day.")
time.sleep(2.5)
print("The first man is guilty of " + random.choice(crimes) + ".")
time.sleep(2)
for x in range (0,10):
    Response = input("Would you like to condemn this man? Type yes or no: ")
    count = count + 1
    condemnation()
    crimejudge()
print("All men have been judged and peace restored to the land.")
closecourt()
