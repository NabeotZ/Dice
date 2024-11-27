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

#Roll the dice
def roll():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    third_dice = random.randint(1, 6)
    return [first_dice, second_dice, third_dice]

#Find the dice with the different result
def different_results(list_of_dice_rolls):
    #For example, (5, 5, 5)
    if list_of_dice_rolls[0] == list_of_dice_rolls[1] == list_of_dice_rolls[2]:  #All three have the same number
        return 0
    #For example, (2, 2, 5)
    elif list_of_dice_rolls[0] == list_of_dice_rolls[1]:  #Third dice has a different result
        return list_of_dice_rolls[2], 2
    #For example, (1, 5, 1)
    elif list_of_dice_rolls[0] == list_of_dice_rolls[2]:  #Second dice has a different result
        return list_of_dice_rolls[1], 1
    #For example, (5, 3, 3)
    elif list_of_dice_rolls[1] == list_of_dice_rolls[2]:  #First dice has a different result
        return list_of_dice_rolls[0], 0
    #All three dice have different results
    #For example, (1, 2, 3)
    else:  
        return "Dice are different", list_of_dice_rolls


