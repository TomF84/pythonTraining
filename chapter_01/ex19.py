#This one is like your script with argv
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	
#Give numbers directly
print("We can just give the numbers directly:")
cheese_and_crackers(20, 30)

#Use variables
print("OR, we can give variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Do math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Math with variables
print("And we can combine the two, math with variables:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)