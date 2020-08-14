# :TODO: rock paper scisors
# greet user
# ask user for input
# validate input
# make computer play
# check or winner
# if winner give appropriate response

import json
import os
import random


def main():
    roles = load_roles()
    play_game(roles)


def play_game(roles):
    # :TODO: play a game
    show_header()
    p1 = get_player()

    winner = None
    player_index = pick_first()
    while not winner:
        role = make_a_play(roles)
        player_index = toggle_player(player_index)
        if check_winner():
            print(f"Congratulations, {winner}! you won!")


def load_roles():
    # gets path of current file then gets path o the file directory inside src
    file_path = os.path.dirname(__file__)
    file_name = os.path.join(file_path, 'files/roles.json')

    # loads the file in memory
    with open(file_name, 'r', encoding='utf-8') as fin:
        data = dict(json.load(fin))
    fin.close()

    return data


def show_header():
    print('-' * 35)
    print('' * 10, 'Welcome to rock paper scissors!')
    print('-' * 35)
    print()


def get_player():
    player = ''
    while not player.strip():
        player = input("What's your name?")
        if not player.strip():
            print("You cannot put an empty name")


def pick_first():
    player_input = ['me', '0']
    computer_input = ['pc', '1']
    random_input = ['rand', 'random']

    pick = None

    print(f'Who goes first? you or computer ({player_input[0]} / {computer_input[0]}) or ({player_input[1]}) '
                 f'/ {computer_input[1]}) or even ({random_input[0]} / {random_input[1]})')
    while pick not in player_input or pick not in computer_input or pick not in random_input:
        pick = input('feel free to pick').strip()
        if pick in player_input:
            return 0
        elif pick in computer_input:
            return 1
        elif pick in random_input:
            return random.randint(0,1)
        elif not pick or pick not in [player_input,computer_input,random_input]:
            print(f"if you don't want to pick anything just say {random_input[0]} or {random_input[1]} "
                  f"but not an empty string")
            print()
            continue


def make_a_play(roles):
    role = ''
    available_roles = [key for key in roles]
    #TODO: make sure to split this func into 2 for human and computer player
    while role not in available_roles:
        print()
        role = input(f"What do you want to play? ({available_roles})")
        print(role)
        if role in available_roles:
            return role
        else:
            print(f"that's not a valid move! try any of these {available_roles} inside except")


def toggle_player(player_index):
    return (player_index + 1) % 2


def check_winner():
    #TODO: make the function to check if there is a winner
    pass


if __name__ == '__main__':
    main()
