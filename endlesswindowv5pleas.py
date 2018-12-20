import random
import time

crimes = ["theft", "arson", "murder", "robbery", "treason"]
punishments = ["hanged", "drawn and quartered", "beheaded", "jailed", "thrown from a window until dead"]
pleas = ["guilty", "not guilty"]

count = 0

# Next man is ... Pleads...
def crimejudge():
    if count == 1:
        print("The first man is guilty of " + random.choice(crimes) + ".")
        time.sleep(2)
        print("He pleads " + random.choice(pleas) + ".")
    else:
        print("The next man is guilty of " + random.choice(crimes) + ".")
        time.sleep(2)
        print("He pleads " + random.choice(pleas) + ".")
        time.sleep(1.5)

#Condemnation and result
def condemnation():
   if Response == "yes":
        print("The man has been condemned and sentenced to be " + random.choice(punishments) + ".")
        time.sleep(2)
   elif Response == "no":
        print("The man has been spared a fate most gruesome.")
        time.sleep(2)
   else:
        print("The man has fled.")
        time.sleep(2)

#You have judged X men
def judgmentcounter():
    if count == 1:
        print("You have judged " + str(count) + " man.")
        time.sleep(2)
    else:
        print("You have judged " + str(count) + " men.")
        time.sleep(2)

#Peace restored, close court
def closecourt():
    print("All men have been judged and peace restored to the land.")
    response2 = input("Would you like to close court?")
    if response2 == "yes":
        exit(1)
    else: exit(1)


print("There are 10 men that need to be judged this day.")
time.sleep(2.5)
for x in range (0,10):
    count = count + 1
    crimejudge()
    Response = input("Would you like to condemn this man? Type yes or no: ")
    condemnation()
    judgmentcounter()
closecourt()
