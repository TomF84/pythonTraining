i = 0
numbers = []

while i < 6:
    print(f"At the top it is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ",numbers)
    print(f"At the bottom it is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)