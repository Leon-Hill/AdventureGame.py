
# This is a short text based adventure game, developed by Leon Hill. 15/10/2022.

# Game start
def ruinsCentre():
    directions = ["North", "East", "West"]
    print("After a breather, you look around and notice you are in the centre of the ruins, you know of at least one exit, the way you came in. There are three doorways surrounding you.")
    userInput = ""
    while userInput not in directions:
        print("Options: North / East / West")
        userInput = input()
        if userInput == "North":
            wineCellar()
        elif userInput == "East":
            livingArea()
        elif userInput == "West":
            Kitchen()
        else:
            print("Please enter a valid option.")

def wineCellar():
    print("Enter Code Here.")

def livingArea():
    print("Enter Code Here.")

def Kitchen():
    print("Enter Code Here.")

# Introduction
while True:
    print("Welcome to the Python adventure game")
    print("You are trying to follow a map through an abandoned ruin in rural England.")
    print("However, during your exploration, you find yourself lost.")
    print("Day is quickly turning into dusk.")
    print("Let's start with your name: ")
    name = input()
    print("Good luck " + name + ".")
    ruinsCentre()
