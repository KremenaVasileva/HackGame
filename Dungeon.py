from Treasure_generator import Treasure_generator
import json
import random
from Weapon import Weapon
from Spell import Spell
from enemy_class import Enemy


class Wrong_direction(Exception):
    pass


class Dungeon:

    def __init__(self, filename):

        self.__level = filename[:-4]
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

    def load_rand_enemy(self):
        filename = self.__level + '__enemies.json'
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

    def spell_or_weapon(self, creature):
        if creature.can_cast() and creature.attack(by='magic') > creature.attack(by='weapon'):
            return creature.current_spell
        else:
            return creature.current_weapon

    def hero_attack(self, hero):

        found_enemy = False
        enemy_x = -1
        enemy_y = -1

        if self.__map[self.__hero_y][self.__hero_x] == 'E':
            found_enemy = True
            enemy_x = self.__hero_x
            enemy_y = self.__hero_y

        # Checking if attack can be done:
        if not hero.can_cast() and not found_enemy:
            print('Not enough mana to cast magic!')
            return 0



        # We search for an enemy only on a straight line
        #       .........
        #       ....Y....
        #       ....Y....
        #       ..XXHXX..
        #       ....Y....
        #       ....Y....
        #       .........

        while not found_enemy:
            cast_range = hero.current_spell.get_cast_range()
            for distance in range(-cast_range, cast_range + 1):

                if self.__map[self.__hero_y][self.__hero_x + distance] == 'E':
                    found_enemy = True
                    enemy_y = self.__hero_y
                    enemy_x = self.__hero_x + distance
                    break

                if self.__map[self.__hero_y + distance][self.__hero_x] == 'E':
                    found_enemy = True
                    enemy_y = self.__hero_y + distance
                    enemy_x = self.__hero_x
                    break

        if not found_enemy:
            print ('Nothing in range' + hero.current_spell.get_cast_range())
            return 0

        # Вече имаме координатите на героя, сега ще го генерираме
        # и ще му дадем на случаен принцип оръжие и магия
        enemy = self.load_rand_enemy()
        enemy.equip(Weapon.load_weapon_from_file('weapons.json'))
        enemy.learn(Spell.load_spell_from_file('spells.json'))

        # If we have found enemy, hero stats fighting until s.o. dies
        while hero.is_alive() and enemy.is_alive():

            # First move: Hero attacks
            fighting_tool = self.spell_or_weapon(hero)
            if isinstance(fighting_tool, Spell):
                enemy.take_damage(hero.attack(by='magic'))
                result = 'Hero casts a '
                result += fighting_tool.get_name()
                result += ', hits enemy for ' + hero.attack(by='magic')
                result += '. Enemy health is ' + enemy.get_health()
                print(result)
            else:
                enemy.take_damage(hero.attack(by='weapon'))
                result = 'Hero hits with '
                result += fighting_tool.get_name()
                result += ' for ' + hero.attack(by='weapon')
                result += '. Enemy health is ' + enemy.get_health()
                print(result)

            # Second move: enemy attacks or moves forward
            # If enemy has reached hero:
            if enemy_x == self.__hero_x and enemy_y == self.__hero_y:
                fighting_tool = self.spell_or_weapon(enemy)
                if isinstance(fighting_tool, Spell):
                    hero.take_damage(enemy.attack(by='magic'))
                    result = 'Enemy casts a '
                    result += fighting_tool.get_name()
                    result += ', hits hero for ' + enemy.attack(by='magic')
                    result += '. Hero health is ' + hero.get_health()
                    print(result)
                else:
                    hero.take_damage(enemy.attack(by='weapon'))
                    result = 'Enemy hits with '
                    result += fighting_tool.get_name()
                    result += ' for ' + enemy.attack(by='weapon')
                    result += '. Hero health is ' + hero.get_health()
                    print(result)
            else:
                # Enemy has not reached hero, so he moves
                moves = ''

                if enemy_x > self.__hero_x:
                    moves = 'to the left'
                    enemy_x -= 1
                elif enemy_x < self.__hero_x:
                    moves = 'to the right'
                    enemy_x += 1
                elif enemy_y > self.__hero_y:
                    moves = 'up'
                    enemy_y -= 1
                elif enemy_y < self.__hero_y:
                    moves = 'down'
                    enemy_y += 1
                print('Enemy moves one square ' + moves + ' in order to get to the hero. This is his move.')

        # Someone has died, let's check who
        if not hero.is_alive():
            print('Hero is dead')
            return -1
        else:
            print('Enemy is dead')
            return 1

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

            hero.take_mana()

            if(is_treasure):
                Treasure_generator.get_treasure(hero)

            if(is_enemy):
                duel = self.hero_attack(hero)
                if duel == -1:
                    return -1

            self.__map[self.__hero_y][self.__hero_x] = 'H'
            # BLAAA
            return True
        else:
            return False


# move връща True ако се е преместил, False, ако не и -1 ако е умрял :D
