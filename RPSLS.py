import random

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

def number_to_name(number):
    # convert name to number using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"

    
def rpsls(player_choice):     
    # print a blank line to separate consecutive games
    print ("\n")
    # print out the message for the player's choice
    print ("Player chooses " + player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print ("Computer chooses " + comp_choice)
    # compute difference of comp_number and player_number modulo five
    determinant = (comp_number - player_number)%5
    # use if/elif/else to determine winner, print winner message
    if determinant == 1 or determinant == 2:
        print ("Computer wins!")
    elif determinant == 3 or determinant == 4:
        print ("Player wins!")
    else:
        print ("Player and computer tie!")


print ("To play this game, enter 'rpsls(player_choice)'")
print ("Choose from rock, paper, scissors, lizard, or Spock!")
print ("E.g. rpsls('Spock')")        
