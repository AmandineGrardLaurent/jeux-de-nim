#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim : Variante simple avec 21 allumettes.
Deux joueurs (ou un joueur contre l'ordinateur) retirent à tour de rôle entre 1 et 4 allumettes.
Celui qui est forcé de prendre la dernière allumette perd la partie.
"""
import random

TOTAL_STICKS = 21
MIN_REMOVE = 1
MAX_REMOVE = 4

def get_players_names():
    """
    Prompt two players to enter their names.
    This function asks for the names of two players via user input.

    :returns: tuple: A tuple containing the names of player 1 and player 2 (player_1, player_2).
    """
    player_1 = input("Joueur 1 : Saisissez votre nom ? ").strip()
    player_2 = ""

    while player_2.lower() not in ["computer", "ordinateur"] and not player_2:
        player_2 = input("Joueur 2 : Saisissez votre nom ? ").strip()

    return player_1, player_2


def ask_first_player(player_1, player_2):
    """
    Ask which player should start the game.

    :param player_1: str - Name of the first player.
    :param player_2: str - Name of the second player.
    :return: str - Name of the player who will start the game.
    """
    first_player = ""
    while first_player not in [player_1, player_2]:
        first_player = input(f"Qui commence ? ({player_1} ou {player_2}) : ").strip()

    return first_player


def ask_number_of_sticks(player, min_sticks, max_sticks):
    """
     Prompt the player to choose how many matches to remove.
    Ensures the input is valid and within the allowed range.

    :param player: str - The name of the current player.
    :param min_sticks: int - Minimum number of matches allowed to remove.
    :param max_sticks: int - Maximum number of matches allowed to remove.
    :return: int - Valid number of matches chosen by the player.
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
        print("-" * 50)
    else:
        print(f"Il reste une allumette, {player} vous avez perdu")


def player_turn(player, total_sticks, sticks_removed):
    """
    Execute a player's turn by displaying the move and updating the stick count.

    :param player: str - Name of the player.
    :param total_sticks: int - Current total of remaining sticks.
    :param sticks_removed: int - Number of sticks the player chooses to remove.
    :return: int - Updated number of remaining sticks after the move.
    """
    display_player_turn(player, sticks_removed, total_sticks)
    total_sticks -= sticks_removed
    return total_sticks


def nim_basic_game():
    total_sticks_in_game = TOTAL_STICKS
    p1, p2 = get_players_names()
    current_player = ask_first_player(p1, p2)
    user_removed_sticks_history = []

    # Determine who is the second player
    second_player = p2 if current_player == p1 else p1

    print("-" * 50)

    while total_sticks_in_game > 1:
        display_sticks(total_sticks_in_game)
        if current_player.lower() == "ordinateur":
            # Computer player's turn
            if user_removed_sticks_history:
                computer_removed_sticks = 5 - user_removed_sticks_history[-1]
            else:
                computer_removed_sticks = random.randint(MIN_REMOVE, MAX_REMOVE)

            total_sticks_in_game = player_turn(current_player, total_sticks_in_game, computer_removed_sticks)
        else:
            # Human player's turn
            sticks_removed = ask_number_of_sticks(current_player, MIN_REMOVE, MAX_REMOVE)
            total_sticks_in_game = player_turn(current_player, total_sticks_in_game, sticks_removed)
            user_removed_sticks_history.append(sticks_removed)

        if total_sticks_in_game <= 1:
            print(f"Il ne reste qu'une allumette. {second_player} a perdu !")
            print(f"{current_player} a gagné le jeu ! 🎉")
            break
        # Switch players
        current_player, second_player = second_player, current_player


def ask_pile_of_sticks(pile_history):
    valid_nb = False
    number = None

    print("Dans quel tas souhaitez-vous prendre des allumettes ?")

    while not valid_nb:
        pile_nb_str = input().strip()
        if pile_nb_str.isdigit():
            number = int(pile_nb_str)
            valid_nb = (number <= len(pile_history))
            if not valid_nb:
                print(f"Choisissez un autre tas d'allumettes")
        else:
            print("Merci de saisir un nombre.")

    return number


def display_sticks_by_pile(pile_history):
    """
    Display the current number of sticks for each pile using vertical bars.

    :param pile_history: list of int - The list of remaining sticks in each pile.
    """
    for pile in range(0, len(pile_history)):
        print(f"Pile n°{pile + 1} -> ", end="")
        print("|" * pile_history[pile])
    print("")


def display_sticks(total_sticks):
    """
    Display the total number of sticks using vertical bars.

    :param total_sticks: int - Current total of remaining sticks.
    """
    print("-> " + "|" * total_sticks)



if __name__ == '__main__':

    display_sticks_by_pile([1, 7, 5])
    display_sticks(6)
    #nim_basic_game()

