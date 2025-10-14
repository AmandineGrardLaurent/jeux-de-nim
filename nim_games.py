#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim : variante simple
"""


def get_players_names():
    """
    Prompt two players to enter their names.
    This function asks for the names of two players via user input.

    :returns: tuple: A tuple containing the names of player 1 and player 2 (player_1, player_2).
    """
    player_1 = input("Joueur 1 : Saisissez votre nom ? ")
    player_2 = input("Joueur 2 : Saisissez votre nom ? ")

    return player_1, player_2

def ask_first_player(player_1, player_2):
    """
    Prompts the user to choose which player goes first.

    :param player_1: str: The name of player 1.
    :param player_2: str: The name of player 2.
    :returns: str: The name of the player who will play first.
    """
    first_player = ""
    while first_player not in [player_1, player_2]:
        first_player = input(f"Qui commence ? ({player_1} ou {player_2}) : ").strip()

    return first_player


def ask_number_of_sticks(player, min_sticks, max_sticks):
    """
    Ask the player how many sticks they want to take, ensuring valid input.

    :param player: str: The name of the current player.
    :param min_sticks: int: Minimum number of sticks the player can take.
    :param max_sticks: int: Maximum number of sticks the player can take.
    :return: int: A valid number of sticks chosen by the player, between min_sticks and max_sticks (inclusive).
    """
    valid_nb = False
    number = None

    print(f"{player}, combien d'allumettes souhaitez-vous retirer :  ")
    while not valid_nb:
        number_str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_nb = (min_sticks <= number <= max_sticks)
            if not valid_nb:
                print(f"Choisissez un nombre entre {min_sticks} et {max_sticks}")
        else:
            print("Merci de saisir un nombre.")
    return number


def display_player_turn(player, user_sticks, total_sticks):
    """
    Display the action taken by the player and the number of sticks remaining.

    :param player: str: The name of the current player.
    :param user_sticks: int: The number of sticks the player chose to remove.
    :param total_sticks: int: The total number of sticks before the move.
    """
    print(f"{player}, vous avez retiré {user_sticks} allumettes")

    if total_sticks > 1:
        print(f"Total d'allumettes restantes : {total_sticks - user_sticks}")
    else:
        print(f"Il reste une allumette, {player} vous avez perdu")


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
    Execute a player's turn: ask how many sticks to take, show the result, and update the total.

    :param player: The name of the player taking the turn.
    :param total_sticks: The current number of sticks in the game.
    :return: int: The updated total number of sticks after the player's move.
    """
    sticks_removed = ask_number_of_sticks(player, 1, 4)
    display_player_turn(player, sticks_removed, total_sticks)
    return subtract_sticks(sticks_removed, total_sticks)


if __name__ == '__main__':
    total_sticks_in_game = 21
    p1, p2 = get_players_names()
    current_player = ask_first_player(p1, p2)

    second_player = p2 if current_player == p1 else p1

    while total_sticks_in_game > 1:
        total_sticks_in_game = player_turn(current_player, total_sticks_in_game)

        if total_sticks_in_game == 1:
            print(f"Il ne reste qu'une allumette. {second_player} a perdu !")
            break

        current_player, second_player = second_player, current_player


