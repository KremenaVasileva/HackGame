from hero_class import Hero
from enemy_class import Enemy
from Dungeon import Dungeon

import os


if __name__ == '__main__':
    our_hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    game_dungeon = Dungeon.load_from_file("level1.txt")

    print("Welcome to Dungeons and Pythons!")
    print("You can move your hero by using the W(up), A(left), S(down) and D(right) keys on your keyboard.")
    print("To attack your enemies, use L.")
    print("Have fun! ;)\n")

    player_choice = input("Do you want to start a new game?[y/n]: ")

    # if player_choice == "H" or player_choice == "h":
    #     print("Dungeons and Pythons' rules:")
    #     print("Your hero is {}".format(our_hero.known_as()) + ". ")
    #     print("Starting health: {}".format(our_hero.get_health()))
    #     print("Starting mana: {}".format(our_hero.get_mana) + "\n")
# 
    #     print("You can move your hero up, down, left and right across the ", )
    #     print("map using the keys on your keyboard.", )
    #     print("")

    if player_choice == "Y" or player_choice == "y":

        game_dungeon.spawn(our_hero)

        while our_hero.is_alive() or game_dungeon.spawn(our_hero):

            game_dungeon.print_map()

            player_move = input("Choose your move: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            is_at_gate = False

            if player_move == "W" or player_move == "w":
                is_at_gate = game_dungeon.move_hero(our_hero, "up")

            elif player_move == "A" or player_move == "a":
                is_at_gate = game_dungeon.move_hero(our_hero, "left")

            elif player_move == "S" or player_move == "s":
                is_at_gate = game_dungeon.move_hero(our_hero, "down")

            elif player_move == "D" or player_move == "d":
                is_at_gate = game_dungeon.move_hero(our_hero, "right")

            elif player_move == "L" or player_move == "l":
                game_dungeon.hero_attack(our_hero)

            # if our hero (has beaten all its enemies and) is at G
            if is_at_gate:
                game_dungeon = Dungeon.load_from_file("level2.txt")
                game_dungeon.spawn(our_hero)

        print("Game over .. :(")

    else:
        print("\nWhy the *** you no wanna start a game?! ;(")
