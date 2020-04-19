def makeNumbers(n,inc=1):
    i = 0
    numbers = []
    while i < n:
        print(f"At the top it is {i}")
        numbers.append(i)
    
        i = i + inc
        print("Numbers now: ",numbers)
        print(f"At the bottom it is {i}")
    return numbers
        

N = int(input("How many numbers would you like to add?\n  >"))
INC = input("What should be the increment?\n  >")

if INC:
    numbers = makeNumbers(N,int(INC))
else:
    numbers = makeNumbers(N)
    
print("The numbers: ")

for num in numbers:
    print(num)