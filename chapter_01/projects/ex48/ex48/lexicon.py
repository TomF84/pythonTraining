def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
        
def scan(userInput):
    #This function should create from the userinput a list of tuples with a description of the user input. 
    #Word by word.    
    #First we give it a direction and it should return a tuple as ('direction', userInput), userInput should 
    #be a string.
    
    words = userInput.split()
    allWords = []
    
    Directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    
    for word in words:
        if userInput in Directions:
            allWords.append(('direction', userInput))
        else:
            pass

    return allWords