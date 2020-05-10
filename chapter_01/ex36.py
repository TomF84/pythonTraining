from sys import exit
from random import random

teams = { "A" : [{"name" :"Jurian", "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]}, 
                 {"name" :"Giel"  , "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]},
                 {"name" :"Arnout", "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]},
                 {"name" :"Christ", "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]},
                 {"name" :"Martin", "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]}],

         "B" : [ {"name" :"Sander", "secondBallFail" : 20, "reception" : 70, "jump" : [60, 90], "float" : [80, 40] }, 
                 {"name" :"Casper", "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]}, 
                 {"name" :"Jasper", "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]},
                 {"name" :"Groen" , "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]},
                 {"name" :"Tom"   , "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]},
                 {"name" :"Ferry" , "spike" : 80, "reception" : 70, "jump" : [60, 90], "float" : [80, 40]}]}

score = { "A" : 0, "B" : 0 }
order = { "A" : 0, "B" : 0 }

def serve(team):
    if team == 'A':
        receptor = 'B'
    else:
        receptor = 'A'
        
    print("Team",team,"is about to serve.")
    print("It is player",teams[team][order[team]%6]["name"])
    
    if team == "A":
        print("Do you go for a jump or a float?")
        choice = input("> ")
    else:
        if random() > 0.24:
            choice = "float"
        else:
            choice = "jump"
            
    if "jump" in choice.lower():
        choice = 'jump'
    elif "float" in choice.lower():
        choice = 'float'
    else:
        print("You failed to choose a valid serve, point lost.")
        order[receptor]+=1
        point(receptor)
        
    if teams[team][order[team]%6][choice][0]/100.0 < random():
        print("The serve was not valid, point lost.")
        order[receptor]+=1
        point(receptor)        
    else:
        reception(receptor,teams[team][order[team]%6][choice][1]*random())

def reception(team,strength):
    avgReception = 0
    if team == 'A':
        server = 'B'
    else:
        server = 'A'
        
    for player in teams[team]:
        avgReception += player["reception"]/6.0
    
    if avgReception > strength:
        print('The reception was succesful:',avgReception,strength,'\nPoint scored')
        order[team]+=1
        point(team)
    else:
        print('The serve was to strong:',avgReception,strength,'\nAce scored')
        point(server)
        
def point(team):
    score[team]+=1
    print(f'''Score:
    team A    :   team B
 {score["A"]} : {score["B"]}
''')
    if score["A"] >= 25 or score["B"] >= 25:
        if abs(score["A"]-score["B"]) >= 2:
            print('set afgelopen.')
            finished(score)
        else:
            print('2 punten verschil nodig')
            serve(team)
    else:
        serve(team)

def finished(score):
    if score["A"] > score ["B"]:
        print("You won, well done!")
    else:
        print("You lost, too bad!")
        
    exit(0)

def start():
    print("You are the setter in a volleyball game.")
    print("I am the referee, what is your name?")
    
    name = input("> ")
    
    if 'jeroen' in name.lower():
        secondBallFail = 100
        floatServe = [80,40]
        jumpserve = [20,80]
    else:
        secondBallFail = 50
        floatServe = [70, 50]
        jumpserve = [40, 90]
    
    teams['A'].insert(0, {"name" : name.capitalize(), "secondBallFail" : secondBallFail, "reception" : 70, "jump" : jumpserve, "float" : floatServe })
    print("The toss is next, will you choose heads or tails?")
    toss_choice = input("> ")
    
    if random() > 0.5:
        print(f"It's {toss_choice}! Do you want to serve or receive the first serve?")
        first_serve = input("> ")
        if "serve" in first_serve:
            serve("A")
        else:
            serve("B")
    else:
        if "heads" in toss_choice:
            result = "tails"
        else:
            result = "heads"
        print(f"It's {result}! The opponent chooses to serve.")
        serve("B")
        
#oldserve = ''    
start()