print("There are five men that need to be judged this day.")

count = 0

for x in range (0,5):
    Response = input("Would you like to throw this man out of the window? Type yes or no: ")

    if Response == "yes":
        print("The man has been successfully thrown out of the window.")
    elif Response == "no":
        print("The man has been spared a fate most gruesome.")
    else:
        print("The man has fled.")
    count = count + 1
    
    if count == 1:
        print("You have judged " + str(count) + " man.")
    else:
        print("You have judged " + str(count) + " men.")

print("All men have been judged and peace restored to the land.")

response2 = input("Would you like to close court?")

if response2 == "yes":
    exit(1)
else: exit(1)
