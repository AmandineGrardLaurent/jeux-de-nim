#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""

# possibilités de prendre entre 1 à 4 allumettes par tour
# perdant est celui qui prend la dernière allumette
# 2 joueurs humains ou 1 joueur humain vs ordinateur


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


def ask_number_of_sticks(player):
    """
    Ask the given player how many sticks they want to take.
    Prompts the player to input a number of sticks to remove.

    :param player: str: The name of the current player.
    :return: int: The number of sticks chosen by the player.
    """
    nb_sticks = int(input(f"{player}, combien d'allumettes souhaitez-vous retirer :  "))
    return nb_sticks


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
    player_choice = ask_number_of_sticks(player)
    display_player_turn(player, player_choice, total_sticks)
    return subtract_sticks(player_choice, total_sticks)


"""def verify_input_name():
    return


def verify_input_stick():
    return"""


if __name__ == '__main__':
    total_sticks_in_game = 21
    p1, p2 = ask_players()

    while total_sticks_in_game > 1:
        total_sticks_in_game = player_turn(p1, total_sticks_in_game)
        """if total_sticks_in_game == 1 :
            break"""
        total_sticks_in_game = player_turn(p2, total_sticks_in_game)