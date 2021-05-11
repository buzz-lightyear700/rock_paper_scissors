import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper, Scissors, Lizard, or Spock: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "sc"]:
        user_choice = "sc"
    elif user_choice in ["Spock", "spock", "sp"]:
        user_choice = "sp"
    elif user_choice in ["Lizard", "lizard", "l"]:
        user_choice = "l"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1, 5)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "sc"
    elif comp_choice == 4:
        comp_choice = "sp"
    else:
        comp_choice = "l"
    return comp_choice


def user_rock(player_wins,comp_wins):
    if comp_choice == "r":
        print("You chose rock. The computer chose rock. You tied.")
        return player_wins, comp_wins

    elif comp_choice == "p" or comp_choice == "sp":
        print("You chose rock. The computer chose paper. You lose.")
        comp_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "sc" or comp_choice == "l":
        print("You chose rock. The computer chose scissors. You win.")
        player_wins += 1
        return player_wins,comp_wins

def user_paper(player_wins,comp_wins):
    if comp_choice == "r" or comp_choice == "sp":
        print("You chose paper. The computer chose rock. You win.")
        player_wins += 1
        return player_wins,comp_wins


    elif comp_choice == "p":
        print("You chose paper. The computer chose paper. You tied.")
        return player_wins,comp_wins


    elif comp_choice == "sc" or comp_choice == "l":
        print("You chose paper. The computer chose scissors. You lose.")
        comp_wins += 1
        return player_wins,comp_wins

def user_scissors(player_wins, comp_wins):
    if comp_choice == "r" or comp_choice == "sp":
        print("You chose scissors. The computer chose rock. You lose.")
        comp_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "p" or comp_choice == "l":
        print("You chose scissors. The computer chose paper. You win.")
        player_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "sc":
        print("You chose scissors. The computer chose scissors. You tied.")
        return player_wins, comp_wins

def user_lizard(player_wins, comp_wins):
    if comp_choice == "r" or comp_choice == "sc":
        print("You chose lizard. The computer chose rock. You lose.")
        comp_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "p" or comp_choice == "sp":
        print("You chose lizard. The computer chose paper. You win.")
        player_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "l":
        print("You chose lizard. The computer chose lizard. You tie.")
        return player_wins, comp_wins

def user_spock(player_wins, comp_wins):
    if comp_choice == "r" or comp_choice == "sc":
        print("You chose spock. The computer chose rock. You win.")
        player_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "p" or comp_choice == "l":
        print("You chose spock. The computer chose paper/lizard. You lose.") #TODO do this later
        comp_wins += 1
        return player_wins, comp_wins

    elif comp_choice == "sp":
        print("You chose spock. The computer chose spock. You tied.")
        return player_wins, comp_wins

#==========================================================
#Main
while True:
    print("")

    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")
    #User Chooses Rock
    if user_choice == "r":
        player_wins, comp_wins = user_rock(player_wins,comp_wins)

    #User Chooses Paper
    elif user_choice == "p":
        player_wins, comp_wins = user_paper(player_wins,comp_wins)

    #User Chooses Scissors
    elif user_choice == "sc":
        player_wins, comp_wins = user_scissors(player_wins,comp_wins)

    #User Chooses Lizard
    elif user_choice == "l":
        player_wins, comp_wins = user_lizard(player_wins,comp_wins)

    #User Chooses Spock
    elif user_choice == "sp":
        player_wins, comp_wins = user_spock(player_wins,comp_wins)

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break