# Import the choice function of the random module

import random

# Define a function that asks for an odd number on the keyboard, until it is not valid
# will keep asking

number_of_games = int(input("Enter an odd number: "))
while number_of_games%2 == 0:
    number_of_games = int(input("Enter an odd number: "))

# Assign a list of 5 possible options.

play = [ 'stone', 'paper', 'scissors', 'lizard', 'spock']

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...
# This time the previously defined function is used

max_games = number_of_games

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

max_to_win = 2

# Define a function that randomly returns one of the 5 options.
# This will correspond to the play of the machine. Totally random.

machine_player = random.choice(play)

# Print by console the winner of the game based on who has more accumulated wins

'''scissors > paper
paper > stone
stone > scissors
paper > spock
lizard > paper
spock > stone
lizard > spock
scissors > lizard
spock > scissors
stone > lizard
'''


nb_of_game = 0
machine_wins = 0
human_wins = 0
tie = 0

while machine_wins <= max_to_win and human_wins <= max_to_win and nb_of_game <= max_games:
    nb_of_game +=1
    machine_player = random.choice(play)
    human_player = str(input("Enter your choice (stone, paper, scissors, lizard or spock): "))
    while human_player != str('stone') and human_player != str('paper') and human_player != str('scissors') and human_player != str('spock') and human_player != str('lizard'):
        human_player = str(input("Enter your choice (stone, paper, scissors, lizard or spock): "))

    if (machine_player == 'scissors' and human_player == "paper") or (machine_player == "paper" and human_player == "stone") or (machine_player == "stone" and human_player == "scissors") or (machine_player == "paper" and human_player == "spock") or (machine_player == "lizard" and human_player == "paper") or (machine_player == "spock" and human_player == "stone") or (machine_player == "lizard" and human_player == "spock") or (machine_player == "scissors" and human_player == "lizard") or (machine_player == "spock" and human_player == "scissors") or (machine_player == "stone" and human_player == "lizard"):
        machine_wins +=1
        print("The choice of the player is: ", human_player)
        print("The choice of the machine is: ", machine_player)
        print("The machine wins")

    elif (human_player == 'scissors' and machine_player == "paper") or (human_player == "paper" and machine_player == "stone") or (human_player == "stone" and machine_player == "scissors") or (human_player == "paper" and machine_player == "spock") or (human_player == "lizard" and machine_player == "paper") or (human_player == "spock" and machine_player == "stone") or (human_player == "lizard" and machine_player == "spock") or (human_player == "scissors" and machine_player == "lizard") or (human_player == "spock" and machine_player == "scissors") or (human_player == "stone" and machine_player == "lizard"):
        human_wins +=1
        print("The choice of the player is: ", human_player)
        print("The choice of the machine is: ", machine_player)
        print("The player wins")

    elif human_player == machine_player:
        tie +=1
        print("The choice of the player is: ", human_player)
        print("The choice of the machine is: ", machine_player)
        print("Tie")

# Print by console the winner of the game based on who has more accumulated wins
if machine_wins < human_wins:
    print("The winner of the game is the human player")
else:
    print("The winner of the game is the machine")
