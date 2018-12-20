import random
crimes = ["theft", "arson", "murder", "robbery", "treason"]

print("There are five men that need to be judged this day.")
print("The first man is guilty of " + random.choice(crimes) + ".")

count = 0

def crimejudge():
    if count == 1:
       print("You have judged " + str(count) + " man.")
       print("The next man is guilty of " + random.choice(crimes) + ".")
    else:
       print("You have judged " + str(count) + " men.")
       print("The next man is guilty of " + random.choice(crimes) + ".")

def windowthrow():
   if Response == "yes":
       print("The man has been successfully thrown out of the window.")
   elif Response == "no":
       print("The man has been spared a fate most gruesome.")
   else:
       print("The man has fled.")

def closecourt():
    response2 = input("Would you like to close court?")
    if response2 == "yes":
        exit(1)
    else: exit(1)


for x in range (0,6):
    Response = input("Would you like to throw this man out of the window? Type yes or no: ")
    count = count + 1
    windowthrow()
    crimejudge()
print("All men have been judged and peace restored to the land.")
closecourt()
