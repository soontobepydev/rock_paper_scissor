# :TODO: rock paper scisors
# greet user
# ask user for input
# validate input
# make computer play
# check or winner
# if winner give appropriate response

import os
import json


def main():
    roles = load_roles()
    play_game(roles)


def play_game(roles):
    # :TODO: play a game
    show_header()

    role = get_imput(roles)


def get_imput(roles):
    role = None
    values = [x for x in roles.items()]
    while role not in roles.items():
        try:
            role = input('What do you want to play?')
            if role in any(roles.items()):
                print(roles.items())
                return role
            else:
                print(roles.items())
                print(f"that's not a valid move! try any of these {values} inside except")
        except:
            print(f"that's not a valid move! try any of these {values} outside except")
    return role

def show_header():
    print('-' * 35)
    print('' * 10, 'Welcome to rock paper scissors!')
    print('-' * 35)


def load_roles():
    # gets path of current file then gets path o the file directory inside src
    file_path = os.path.dirname(__file__)
    file_name = os.path.join(file_path, 'files/roles.json')

    # loads the file in memory
    with open(file_name, 'r', encoding='utf-8') as fin:
        data = dict(json.load(fin))
    fin.close()

    return data


if __name__ == '__main__':
    main()
