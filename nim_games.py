#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""


def ask_players():
    """
    Prompt two players to enter their names.
    This function asks for the names of two players via user input.

    Returns:
        tuple: A tuple containing the names of player 1 and player 2 (player_1, player_2).
    """
    player_1 = input("Joueur 1 : Saisissez votre nom ? ")
    player_2 = input("Joueur 2 : Saisissez votre nom ? ")

    return player_1, player_2

def ask_first_player(player_1, player_2):
    first_player = ""
    while first_player not in [player_1, player_2]:
        first_player = input(f"Qui commence ? ({player_1} ou {player_2}) : ").strip()

    if first_player == player_1:
            return player_1
    else:
            return player_2


def ask_number_of_sticks(player, min_int, max_int):
    """
    Ask the given player how many sticks they want to take.
    Prompts the player to input a number of sticks to remove, ensuring the input
    is a valid positive integer within the allowed range.

    :param player: str: The name of the current player.
    :param min_int: int: The minimum number of sticks the player is allowed to take.
    :param max_int: int: The maximum number of sticks the player is allowed to take.
    :return: int: A valid number of sticks chosen by the player, between min_int and max_int (inclusive).
    """
    valid_nb = False
    number = None

    print(f"{player}, combien d'allumettes souhaitez-vous retirer :  ")
    while not valid_nb:
        number_str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_nb = (min_int <= number <= max_int)
            if not valid_nb:
                print(f"Choisissez un nombre entre {min_int} et {max_int}")
        else:
            print("Merci de saisir un nombre.")
    return number


def display_player_turn(current_player, user_sticks, total_sticks):
    """
    Display the action taken by the player and the number of sticks remaining.

    :param current_player: str: The name of the current player.
    :param user_sticks: int: The number of sticks the player chose to remove.
    :param total_sticks: int: The total number of sticks before the move.
    """
    print(f"{current_player}, vous avez retiré {user_sticks} allumettes")

    if total_sticks > 1:
        print(f"Total d'allumettes restantes : {total_sticks - user_sticks}")
    else:
        print(f"Il reste une allumette, {current_player} vous avez perdu")


def subtract_sticks(nb_sticks, total_sticks):
    """
    Subtract the specified number of sticks from the total.
    :param nb_sticks: The number of sticks to subtract.
    :param total_sticks: The current total number of sticks.
    :return: int: The new total after subtraction.
    """
    total_sticks = total_sticks - nb_sticks
    return total_sticks


def player_turn(player, total_sticks):
    """
    Handle a complete turn for one player: ask for a move, display it, and update the total.
    :param player: The name of the player taking the turn.
    :param total_sticks: The current number of sticks in the game.
    :return: int: The updated total number of sticks after the player's move.
    """
    player_choice = ask_number_of_sticks(player, 1, 4)
    display_player_turn(player, player_choice, total_sticks)
    return subtract_sticks(player_choice, total_sticks)


if __name__ == '__main__':
    total_sticks_in_game = 21
    p1, p2 = ask_players()
    current_player = ask_first_player(p1, p2)

    second_player = p2 if current_player == p1 else p1

    while total_sticks_in_game > 1:
        total_sticks_in_game = player_turn(current_player, total_sticks_in_game)

        if total_sticks_in_game == 1:
            print(f"Il ne reste qu'une allumette. {second_player} a perdu !")
            break

        current_player, second_player = second_player, current_player


