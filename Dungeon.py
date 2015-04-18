from Treasure_generator import Treasure_generator
import json
import random


class Wrong_direction(Exception):
    pass


class Enemy:
    pass


class Dungeon:

    def __init__(self, filename):
        # Position of our hero
        # He's nowherer if x and y are -1
        self.__hero_x = -1
        self.__hero_y = -1
        self.__map = []
        self.__spawning_points = []
        # Coordinates of enemies
        self.__enemies = []
        # making matrix
        j = -1
        with open(filename, "r") as f:
            for line in f:
                j += 1
                i = -1
                row = []
                for char in line:
                    i += 1
                    row.append(char)
                    # Finding hero's first spawning points coordinates
                    if char == 'S':
                        coords = []
                        # Y
                        coords.append(j)
                        # X
                        coords.append(i)
                        self.__spawning_points.append(coords)
                    elif char == 'E':
                        coords = []
                        # Y
                        coords.append(j)
                        # X
                        coords.append(i)
                        self.__enemies.append(coords)
                self.__map.append(row[:-1])

    def load_rand_enemy(filename):
        with open(filename) as f:
            contents = f.read()
            data = json.loads(contents)
            str_enemy = data[random.randint(0, len(data) - 1)]
            mana = str_enemy['mana']
            health = str_enemy['health']
            damage = str_enemy['damage']
            return Enemy(health=health, mana=mana, damage=damage)

    def get_enemies(self):
        return self.__enemies

    def get_hero_x(self):
        return self.__hero_x

    def get_hero_y(self):
        return self.__hero_y

    def print_map(self):
        current_map = self.get_map()
        for line in current_map:
            row = ''
            for char in line:
                row += char[0]
            print(row)

    def get_map(self):
        return self.__map

    def spawn(self, hero):
        hero.take_healing(hero.starting_health)
        hero.take_mana(hero.starting_mana)
        # The real spawning:
        if len(self.__spawning_points) == 0:
            return False
        else:
            self.__hero_y = self.__spawning_points[0][0]
            self.__hero_x = self.__spawning_points[0][1]
            self.__spawning_points = self.__spawning_points[1:]
            self.__map[self.__hero_y][self.__hero_x] = 'H'
            return True

    def move_hero(self, hero, direction):

        dx = 0
        dy = 0

        if direction == 'up':
            dy = -1
        elif direction == 'down':
            dy = 1
        elif direction == 'left':
            dx = -1
        elif direction == 'right':
            dx = 1
        else:
            raise Wrong_direction

        is_in_matrix = self.__hero_x + \
            dx < len(self.__map[0]) and self.__hero_y + dy < len(self.__map)
        is_dot = self.__map[self.__hero_y + dy][self.__hero_x + dx] == '.'
        is_treasure = self.__map[self.__hero_y + dy][self.__hero_x + dx] == 'T'
        is_enemy = self.__map[self.__hero_y + dy][self.__hero_x + dx] == 'E'

        is_accessible = is_dot or is_treasure or is_enemy

        if is_in_matrix and is_accessible:
            self.__map[self.__hero_y][self.__hero_x] = '.'
            self.__hero_x += dx
            self.__hero_y += dy
            self.__map[self.__hero_y][self.__hero_x] = 'H'
            hero.take_mana()

            if(is_treasure):
                Treasure_generator.get_treasure(hero)

            if(is_enemy):
                # Start Fighting Somehow!
                pass

            #BLAAA
            return True
        else:
            return False
