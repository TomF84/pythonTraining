from sys import exit

def gold_room():
    print("This room is full of gold.  How much do you take?")
    
    choice = input("> ")
    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number")
    
    if how_much < 50:
        print("Nice, you are not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
        

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear had moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def serve(team):
    print("Team",team,"is about to serve.")
    print("It is player",teams[team][order])
    print("Do you flee for your live, or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def finished(score):
    if score[0] > score [1]:
        print(why, "You won, well done!")
    else:
        print(why, "You lost, too bad!")
        
    exit(0)

def start():
    print("You are the setter in a volleyball game.")
    print("I am the referee, what ia your name?")
    
    choice = input("> ")
    
    if 'jeroen" in choice.lower():
        secondBallFail = 100
    else:
        secondBallFail = 50

    
start()