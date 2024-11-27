import random

#Does the user want to play
roll_dice = input("Welcome to rolling dice; to start the game press Y. ")
if roll_dice == "Y":
    #Show this if they want to play
    print("Beginning Dice Rolls now. ")
else:
    #Quit the program if they do not want to play
    print("Closing game, come back soon. ")
    quit()

