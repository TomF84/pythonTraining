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
    
    categories = {
                    "direction" : ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
                    "verb"      : ['go','stop','kill','eat'],
                    "stop"      : ['the','in','off','from','at','it'],
                    "noun"      : ['door','bear','princess','cabinet'],
                 }
    
    for word in words:
        found = False
        a = convert_number(word)
        if a != None:
            allWords.append(('number', a))
        else:
            for cat in categories:
                if word.lower() in categories[cat]:
                    allWords.append((cat, word))
                    found = True
                    break
                else:
                    pass
            
            if not found:
                allWords.append(('error', word))

    return allWords