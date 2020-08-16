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
    best_of = 3
    show_header()
    player = get_player()
    computer = 'computer'

    player_score = 0
    computer_score = 0

    winner = None
    while not winner:
        throw = get_throw(roles)

        print()

        throw_winner = check_throw_winner(player, computer, throw, roles)

        if throw_winner == player:
            player_score += 1
            print(f"{player} won this throw!")
        elif throw_winner == computer:
            computer_score += 1
            print(f"{computer} won this throw!")
        else:
            print('this throw as a tie!')

        print(f"{player} threw {throw[0]} and {computer} threw {throw[1]}")
        print(f"The score is {player_score} : {computer_score}")

        winner = get_winner(player, computer, player_score, computer_score, best_of)
        if winner == player:
            print(f"congratulations {player}! you won with the score of {player_score} : {computer_score}")
        elif winner == computer:
            print(f"You lost! the {computer} won with a score of {computer_score} : {player_score}")


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
        player = input("What's your name?").strip()
        if not player.strip():
            print("You cannot put an empty name")
        else:
            return player


def get_throw(roles):
    available_roles = [key for key in roles]

    plays = []

    computers_play = None
    users_play = None
    while not users_play and not computers_play:
        users_play = user_play(available_roles)
        computers_play = computer_play(available_roles)
    plays.append(users_play)
    plays.append(computers_play)
    return plays


def computer_play(available_roles):
    return random.choice(available_roles)


def user_play(available_roles):
    role = None
    while role not in available_roles:
        print()
        role = input(f"What do you want to play? {available_roles}")
        if role in available_roles:
            return role
        else:
            print(f"that's not a valid move! try any of these {available_roles} inside except")


def check_throw_winner(player1, player2, throws, roles):
    winner = None
    player_throw = throws[0]
    computer_throw = throws[1]

    outcome = roles.get(player_throw, {})
    if computer_throw in outcome.get('defeats'):
        return player1
    elif computer_throw in outcome.get('defeated_by'):
        return player2

    return winner


def get_winner(player1, player2, player1_score, player2_score, best_of):
    if player1_score > best_of or player2_score > best_of:
        raise ValueError('score cannot exceed the best of')
    if player1_score == best_of:
        return player1
    elif player2_score == best_of:
        return player2
    else:
        pass


if __name__ == '__main__':
    main()
