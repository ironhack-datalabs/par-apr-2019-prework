#ROCK PAPER SCISSORS
    
import random
possible_options = ["stone", "paper", "scissors"]
maximum_number_of_games = int(input("Enter the maximum number of games\n"))
while maximum_number_of_games %2 == 0:
    maximum_number_of_games = int(input("It has to be an odd number. Try again!\n"))

number_of_wins_to_win = int((maximum_number_of_games + 1) / 2)


def machine_play_generator():
    return random.choice(possible_options)


def user_choice():
    user_input = input("Stone, paper or scissors? Enter your play\n")
    while user_input not in possible_options:
        user_input = input("Try again\n")
    return user_input


def combat(m_play, u_play):
    if m_play == u_play:
        return 0
    elif (m_play == 'stone' and u_play == 'scissors') or (m_play == 'scissors' and u_play == 'paper') or (m_play == 'paper' and u_play == 'stone'):
        return 1
    else:
        return 2


def game_status(m_choice, u_choice):
    print("Machine's play is: ", m_choice, " and it has won ", machine_wins, " round(s)")
    print("Your play is: ", u_choice, " and you have won ",user_wins," round(s)")


machine_wins = 0
user_wins = 0

while machine_wins < number_of_wins_to_win and user_wins < number_of_wins_to_win:
    machine_play = machine_play_generator()
    user_play = user_choice()
    if combat(machine_play, user_play) == 1:
        machine_wins += 1
        game_status(machine_play, user_play)
        print("Machine wins this round")
    elif combat(machine_play, user_play) == 2:
        user_wins += 1
        game_status(machine_play, user_play)
        print("You win this round")
    elif combat(machine_play, user_play) == 0:
        print("It is a tie. Let's do it again!")

if machine_wins == number_of_wins_to_win:
    print("\nMachine has accumulated ", number_of_wins_to_win, " victories.")
    print("\nMachine is the winner!")
elif user_wins == number_of_wins_to_win:
    print("\nYou have accumulated ", number_of_wins_to_win, " victories.")
    print("\nYou are the winner!")


#Improved

    
import random
possible_options1 = ["stone", "paper", "scissors", "lizard", "spock"]


def max_number_of_games_checker(number):
    while number %2 == 0:
        number = int(input("It has to be an odd number. Try again!\n"))
    return number


maximum_number_of_games1 = max_number_of_games_checker(int(input("Enter the maximum number of games wanted\n")))
number_of_wins_to_win1 = int((maximum_number_of_games1 + 1) / 2)


def machine_play_generator1():
    return random.choice(possible_options1)
 

def user_choice1():
    user_input = input("Stone, paper, scissors, lizard or spock? Enter your play\n")
    while user_input not in possible_options1:
        user_input = input("Try again\n")
    return user_input


def combat1(m_play, u_play):
    if m_play == u_play:
        return 0
    elif (m_play == 'stone' and u_play == 'scissors') or (m_play == 'scissors' and u_play == 'paper') or (m_play == 'paper' and u_play == 'stone') or (m_play == 'stone' and u_play == 'lizard') and (m_play == 'lizard' and u_play == 'spock') or (m_play == 'spock' and u_play == 'stone') or (m_play == 'scissors' and u_play == 'lizard') or (m_play == 'lizard' and u_play == 'paper') or (m_play == 'paper' and u_play == 'spock') or (m_play == 'spock' and u_play == 'scissors'):
        return 1
    else:
        return 2


def game_status1(m_choice, u_choice):
    print("Machine's play is: ", m_choice, " and it has won ", machine_wins1, " round(s)")
    print("Your play is: ", u_choice, " and you have won ",user_wins1," round(s)")


machine_wins1 = 0
user_wins1 = 0

while machine_wins1 < number_of_wins_to_win1 and user_wins1 < number_of_wins_to_win1:
    machine_play = machine_play_generator1()
    user_play = user_choice1()
    if combat1(machine_play, user_play) == 0:
        print("It is a tie. Let's do it again!\n")
    elif combat1(machine_play, user_play) == 1:
        machine_wins1 += 1
        game_status1(machine_play, user_play)
        print("Machine wins this round\n")
    elif combat1(machine_play, user_play) == 2:
        user_wins1 += 1
        game_status1(machine_play, user_play)
        print("You win this round\n")

if machine_wins1 == number_of_wins_to_win1:
    print("\nMachine has accumulated ", number_of_wins_to_win1, " victories.")
    print("\nMachine is the winner!")
elif user_wins1 == number_of_wins_to_win1:
    print("\nYou have accumulated ", number_of_wins_to_win1, " victories.")
    print("\nYou are the winner!")
