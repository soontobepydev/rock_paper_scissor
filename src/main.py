# :TODO: rock paper scisors
# greet user
# ask user for input
# validate input
# make computer play
# check or winner
# if winner give appropriate response

import json
import os


def main():
    roles = load_roles()
    play_game(roles)


def play_game(roles):
    # :TODO: play a game
    show_header()
    p1 = get_player()

    winner = None
    while not winner:
        role = get_imput(roles)
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


def get_imput(roles):
    role = None
    
    available_roles = [key for key in roles]
    print(available_roles)
    while role not in available_roles:
        try:
            print()
            role = input(f"What do you want to play? ({available_roles})").strip()
            if role in available_roles:
                return role
            else:
                print(f"that's not a valid move! try any of these {available_roles} inside except")
        except TypeError:
            print(f"that's not a valid move! try any of these {available_roles} outside except")


def check_winner():
    #TODO:check for winner
    pass


if __name__ == '__main__':
    main()
