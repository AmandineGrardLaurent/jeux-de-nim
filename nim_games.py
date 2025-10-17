#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim : Variante simple avec 21 allumettes.
Deux joueurs (ou un joueur contre l'ordinateur) retirent à tour de rôle entre 1 et 4 allumettes.
Celui qui est forcé de prendre la dernière allumette perd la partie.
"""
import random

# Constants for the basic Nim game
TOTAL_STICKS = 21
MIN_STICKS_REMOVE = 1
MAX_STICKS_REMOVE = 4

# Constants for the Marienbad variant
TOTAL_STICKS_BY_PILES = [1, 3, 5, 7]
MIN_PILE = 1
MAX_PILE = 4

def get_players_names():
    """
    Prompt players to enter their names.

    Player 1 always enters a name. Player 2 can either enter a name or type 'computer'/'ordinateur'
    to play against the computer.

    :returns: tuple - (player_1, player_2) names as strings.
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


def ask_version_game():
    """
    Prompt the user to choose the game mode.

    Options:
        1 → Basic version (single pile of 21 sticks)
        2 → Marienbad version (four piles)
    :return: str - 'basic' or 'marienbad'
    """
    version_game = {1 : "basic", 2 : "marienbad"}
    valid_nb = False
    number = None

    print(f"Quelle version du jeu : 1 pour {version_game[1]}, 2 pour {version_game[2]} ? ")
    while not valid_nb:
        number_str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_nb = (number in version_game)
            if not valid_nb:
                print(f"Choisissez 1 ou 2.")
        else:
            print("Merci de saisir un nombre.")

    return version_game[number]


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

    print(f"{player}, combien d'allumettes souhaitez-vous retirer (max {max_sticks}) : ")
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

#----------------basic game--------------------------------------------------------------------------------------

def display_player_turn(player, sticks_removed, total_sticks):
    """
    Display the action taken by the player and the number of sticks remaining.

    :param player: str: The name of the current player.
    :param user_sticks: int: The number of sticks the player chose to remove.
    :param total_sticks: int: The total number of sticks before the move.
    """
    print(f"{player}, vous avez retiré {sticks_removed} allumettes")

    if total_sticks > 1:
        print(f"Total d'allumettes restantes : {total_sticks - sticks_removed}")
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


def nim_basic_game(total_sticks, removed_sticks_history, current_player, second_player):
    """
    Run the basic Nim game: a single pile of 21 sticks.

    Players alternate turns removing 1–4 sticks. The player forced to take
    the last stick loses.
    :param total_sticks: int - Starting number of sticks.
    :param removed_sticks_history: list - History of the player's moves.
    :param current_player: str - Name of the player starting the game.
    :param second_player: str - Name of the other player.
    """
    while total_sticks > 1:

        display_sticks(total_sticks)
        if current_player.lower() == "ordinateur":
            # Computer player's turn
            if removed_sticks_history:
                sticks_removed = 5 - removed_sticks_history[-1]
            else:
                sticks_removed = random.randint(MIN_STICKS_REMOVE, MAX_STICKS_REMOVE)

        else:
            # Human player's turn
            sticks_removed = ask_number_of_sticks(current_player, MIN_STICKS_REMOVE, MAX_STICKS_REMOVE)
            removed_sticks_history.append(sticks_removed)

        total_sticks = player_turn(current_player, total_sticks, sticks_removed)

        if total_sticks <= 1:
            print(f"Il ne reste qu'une allumette. {second_player} a perdu !")
            print(f"{current_player} a gagné le jeu ! 🎉")
            break

        # Switch players
        current_player, second_player = second_player, current_player


def display_sticks(total_sticks):
    """
    Display the total number of sticks using vertical bars.

    :param total_sticks: int - Current total of remaining sticks.
    """
    print("-> " + "|" * total_sticks)


#----------------marienbad game--------------------------------------------------------------------------------------

def nim_marienbad_game(current_player, second_player):
    """
    Run the Marienbad version of Nim: four piles of sticks.

    Players take turns removing 1–4 sticks from one pile.
    The player forced to take the last stick loses.
    :param current_player: str - Name of the player starting the game.
    :param second_player: str - Name of the other player.
    """
    total_sticks = TOTAL_STICKS_BY_PILES.copy()
    sticks_removed_nb = None
    pile_nb = None

    while sum(total_sticks) > 1:
        display_sticks_by_pile(total_sticks)

        if current_player.lower() == "ordinateur":
            valid_pile_nb = False
            valid_sticks_nb = False

            while not valid_pile_nb:
                pile_nb = random.randint(MIN_PILE, MAX_PILE)
                valid_pile_nb = (total_sticks[pile_nb - 1] != 0)

            while not valid_sticks_nb:
                sticks_removed_nb = random.randint(1, total_sticks[pile_nb - 1])
                valid_sticks_nb = (MIN_STICKS_REMOVE <= sticks_removed_nb <= MAX_STICKS_REMOVE)

        else:
            pile_nb = ask_pile_of_sticks(current_player, total_sticks)
            sticks_removed_nb = ask_number_of_sticks(current_player, 1, total_sticks[pile_nb-1])

        total_sticks[pile_nb-1] -= sticks_removed_nb
        print(f"{current_player} a retiré {sticks_removed_nb} d'allumettes dans le tas n°{pile_nb}")

        if sum(total_sticks) == 1:
            print(f"Il ne reste qu'une allumette. {second_player} a perdu !")
            print(f"{current_player} a gagné le jeu ! 🎉")
            break

        current_player, second_player = second_player, current_player


def ask_pile_of_sticks(player, pile_history):
    """
    Ask the player which pile they want to remove sticks from.

    Only non-empty piles are valid choices.
    :param player: str - Current player's name.
    :param pile_history: str - Current state of the piles.
    :return: The selected pile number.
    """
    valid_nb = False
    pile_number = None

    print(f"{player}, dans quel tas souhaitez-vous prendre des allumettes ?")

    while not valid_nb:
        pile_nb_str = input().strip()
        if pile_nb_str.isdigit():
            pile_number = int(pile_nb_str)
            valid_nb = ((pile_number <= len(pile_history)) and pile_history[pile_number - 1] != 0)
            if not valid_nb:
                print(f"Choisissez un tas d'allumettes non vide")
        else:
            print("Merci de saisir un nombre.")

    return pile_number


def display_sticks_by_pile(total_sticks_by_pile):
    """
    Display the current number of sticks for each pile using vertical bars.

    :param total_sticks_by_pile: list of int - The list of remaining sticks in each pile.
    """
    for pile in range(0, len(total_sticks_by_pile)):
        print(f"Pile n°{pile + 1} -> ", end="")
        print("|" * total_sticks_by_pile[pile])
    print("")


def nim_games():
    """
    Launch the game: choose version, get player names, and start the selected mode.
    """
    total_sticks_in_game = TOTAL_STICKS
    p1, p2 = get_players_names()
    current_player = ask_first_player(p1, p2)
    removed_sticks_history = []

    # Determine who is the second player
    second_player = p2 if current_player == p1 else p1

    print("-" * 50)
    version = ask_version_game()

    if version == "basic":
        nim_basic_game(total_sticks_in_game, removed_sticks_history, current_player, second_player)
    else:
        nim_marienbad_game(current_player, second_player)


if __name__ == '__main__':

    nim_games()

