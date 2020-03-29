people = 30
cars =40
trucks =15

#Test to see if we can take cars or not
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")

#Test to see if we could take trucks    
if trucks > cars:
    print("That's to many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide")
    
# Check if we gave enough people for trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")