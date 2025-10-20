# 🎮 Jeu de Nim – Version Terminal en Python

Ce projet propose deux variantes du **Jeu de Nim**, jouables en ligne de commande :

- **Version classique** : un tas de 21 allumettes.
- **Version Marienbad** : quatre tas d'allumettes (1, 3, 5, 7).

Le joueur qui prend **la dernière allumette perd** la partie.  
Tu peux affronter un autre joueur ou l'ordinateur (IA basique).

---

## 📂 Structure du jeu

- `nim_games.py` : fichier principal contenant toute la logique du jeu.
- Jeu en mode **texte** dans le terminal.

---

## 🚀 Lancer le jeu

### ▶️ Prérequis

- Python 3 installé sur votre machine.

### ▶️ Exécution

```bash
python nim_games.py
```
---
# 🕹️ Règles du jeu

## 🔹 Mode classique

- Il y a **21 allumettes**.
- À chaque tour, un joueur peut retirer **entre 1 et 4 allumettes**.
- Le joueur qui est **forcé de prendre la dernière allumette perd**.

---

## 🔹 Mode Marienbad

- Il y a **4 tas d’allumettes** : `[1, 3, 5, 7]`.
- À chaque tour, un joueur choisit **un seul tas** et y retire **entre 1 et 4 allumettes**.
- Le joueur qui **prend la dernière allumette perd**.

---

## 🤖 Mode contre l'ordinateur

- Lors du choix du joueur 2, entrez `ordinateur` ou `computer` pour affronter une IA.

### Comportement de l'IA :
- En **mode classique** : stratégie simple basée sur la **règle des 5**.
- En **mode Marienbad** : choix **aléatoire** d’un tas non vide et d’un nombre valide d’allumettes.

---

# Explication des fonctions du jeu de Nim

#### `get_players_names()`
Demande aux joueurs d'entrer leur nom. Le joueur 2 peut saisir un nom ou taper "ordinateur" ou "computer" pour jouer contre l'IA.

#### `ask_first_player(player_1, player_2)`
Demande quel joueur doit commencer la partie parmi les deux joueurs fournis.

#### `ask_version_game()`
Demande à l'utilisateur de choisir la version du jeu : mode "basic" (classique) ou "marienbad" (avec 4 tas).

#### `ask_number_of_sticks(player, min_sticks, max_sticks)`
Invite un joueur à choisir combien d'allumettes retirer, en s'assurant que la valeur est valide et dans la plage autorisée.

#### `display_player_turn(player, sticks_removed, total_sticks)`
Affiche le nombre d’allumettes retirées par le joueur ainsi que le nombre restant.

#### `player_turn(player, total_sticks, sticks_removed)`
Exécute le tour du joueur en affichant le mouvement et en mettant à jour le nombre total d’allumettes restantes.

#### `nim_basic_game(total_sticks, removed_sticks_history, current_player, second_player)`
Lance le mode classique avec une seule pile de 21 allumettes. Les joueurs jouent à tour de rôle jusqu'à ce qu'il ne reste qu'une allumette.

#### `display_sticks(total_sticks)`
Affiche visuellement les allumettes restantes sous forme de barres verticales.

#### `nim_marienbad_game(current_player, second_player)`
Lance le mode Marienbad avec 4 tas d'allumettes. Chaque joueur choisit un tas non vide et retire entre 1 et 4 allumettes.

#### `ask_pile_of_sticks(player, pile_history)`
Demande au joueur de choisir un tas non vide parmi les piles disponibles.

#### `display_sticks_by_pile(total_sticks_by_pile)`
Affiche les allumettes restantes dans chaque tas sous forme de barres verticales.

#### `nim_games()`
Fonction principale qui lance le jeu : récupère les noms, demande la version du jeu, et démarre la partie selon la version choisie.


---

## ▶️ Exemple d'exécution - Mode classique

```bash
$ python nim_game.py

Joueur 1 : Saisissez votre nom ? Alice
Joueur 2 : Saisissez votre nom ? ordinateur
--------------------------------------------------
Quelle version du jeu : 1 pour basic, 2 pour marienbad ?
1
Qui commence ? (Alice ou ordinateur) : Alice
-> |||||||||||||||||||||

Alice, combien d'allumettes souhaitez-vous retirer (max 4) :
3
Alice, vous avez retiré 3 allumettes
Total d'allumettes restantes : 18
--------------------------------------------------
-> |||||||||||||||||||

ordinateur a retiré 2 allumettes
Total d'allumettes restantes : 16
--------------------------------------------------
-> ||||||||||||||||||

Alice, combien d'allumettes souhaitez-vous retirer (max 4) :
4
Alice, vous avez retiré 4 allumettes
Total d'allumettes restantes : 12
--------------------------------------------------

...

Il ne reste qu'une allumette. ordinateur a perdu !
Alice a gagné le jeu ! 🎉

```
## ▶️ Exemple d'exécution — Mode Marienbad

```bash
$ python nim_game.py

Joueur 1 : Saisissez votre nom ? Bob
Joueur 2 : Saisissez votre nom ? Alice
--------------------------------------------------
Quelle version du jeu : 1 pour basic, 2 pour marienbad ?
2
Qui commence ? (Bob ou Alice) : Bob

Pile n°1 -> |
Pile n°2 -> |||
Pile n°3 -> |||||
Pile n°4 -> |||||||

Bob, dans quel tas souhaitez-vous prendre des allumettes ?
3
Bob, combien d'allumettes souhaitez-vous retirer (max 5) :
2
Bob a retiré 2 d'allumettes dans le tas n°3

Pile n°1 -> |
Pile n°2 -> |||
Pile n°3 -> |||
Pile n°4 -> |||||||

Alice, dans quel tas souhaitez-vous prendre des allumettes ?
4
Alice, combien d'allumettes souhaitez-vous retirer (max 4) :
4
Alice a retiré 4 d'allumettes dans le tas n°4

Pile n°1 -> |
Pile n°2 -> |||
Pile n°3 -> |||
Pile n°4 -> |

...

Il ne reste qu'une allumette. Alice a perdu !
Bob a gagné le jeu ! 🎉

