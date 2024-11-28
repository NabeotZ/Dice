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

#Get the results of the rolls
roll_list = roll()
#Show the first roll of the dice is occuring
print("Roll 1:", roll_list)
total = sum(roll_list)

#Check if all the dice have the same result
if different_results(roll_list) == 0:
    print("Zero Points")
else:
    while True:
        print(f"Roll one is {roll_list[0]}, roll two is {roll_list[1]}, roll three is {roll_list[2]}.")
        print(f"Total is {total}.")

#Find if there was dice that rolled different from the others
        different_dice = different_results(roll_list)
        # If all the dice have the same result
        if different_dice == 0:
            #Give zero points and tell the user
            print("All dice rolled the same. Tupled out, Zero points")
            #End the game
            break
        #If all the dice have different results
        elif different_dice[0] == "Dice are different":  
            #Tell the user
            print("Every dice has rolled differently.")

 #Ask if the user wants a reroll
            reroll = input("Reroll dice? (Roll/Stop) ")
            if reroll.lower() == "Roll":
            #Reroll the dice if user requests it
                roll_list = roll()  
                #Get the results of the reroll
                total = sum(roll_list)  
                #Show the results of the reroll
                print("New roll results:", roll_list)
                #Continue the game
                continue  
            #If user does not want a reroll
            else:
                print("Reroll not requested, final rolls:", roll_list)
                #Show the final total to the user
                print(f"Final total is {total}.")
                #End the game if user does not want a reroll
                break

#If one dice result is different
        else:  
        #Show the dice that is different and reroll it
            print(f"The die that rolled {different_dice[0]} is different from the other two dice.")
            go_again = input("Reroll die that had different result? (Yes/No) ")
            if go_again.lower() == "Yes":
                #Reroll the different die
                roll_list[different_dice[1]] = random.randint(1, 6)
                total = sum(roll_list)  
                #Get the new total
                print("After reroll:", roll_list)
            else:
            #If a reroll is not requested show the final result
                print("No reroll requested. Final rolls:", roll_list)
                print(f"Final total is {total}.")
                #Stop the game
                break
