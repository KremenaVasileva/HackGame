from Treasure_generator import Treasure_generator
from Spell import Spell
from Fights import Fights


class Wrong_direction(Exception):
    pass


class Dungeon:

    hero_char = 'H'
    treasure_char = 'T'
    rocks_char = '#'
    path_char = '.'
    gate_char = 'G'
    enemy_char = 'E'
    spawning_char = 'S'

    @staticmethod
    def find_points(char, level_map):
        points = []
        j = -1
        for line in level_map:
            j += 1
            i = -1
            for current_char in line:
                i += 1
                if current_char == char:
                    coords = []
                    # Y
                    coords.append(j)
                    # X
                    coords.append(i)
                    points.append(coords)
        return points

    @staticmethod
    def load_from_file(filename):
        hero_x = -1
        hero_y = -1
        level_map = []
        spawning_points = []
        enemies = []

        # making matrix
        with open(filename, "r") as f:
            contents = f.read().split("\n")
            level_map = [list(line) for line in contents if line.strip() != ""]

            spawning_points = Dungeon.find_points(
                Dungeon.spawning_char, level_map)
            enemies = Dungeon.find_points(
                Dungeon.enemy_char, level_map)

            return Dungeon(hero_x, hero_y, level_map, spawning_points, enemies)

    def __init__(self, x, y, level_map, spawning_points, enemies):
        self.__hero_x = x
        self.__hero_y = y
        self.__map = level_map
        self.__spawning_points = spawning_points
        # Coordinates of enemies
        self.__enemies = enemies

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
            self.__map[self.__hero_y][self.__hero_x] = Dungeon.hero_char
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
        on_same_field = False
        cast_range = 0

        # Check if hero and enemy are on the same field
        enemy_cords = self.finding_enemy(0)
        on_same_field = enemy_cords is not None
        found_enemy = on_same_field

        # Checking if attack can be done:
        if not hero.can_cast() and not found_enemy:
            print('Cannot cast magic!')
            return 0

        # while not found_enemy:
        if hero.current_spell is None:
            cast_range = 0
        else:
            cast_range = hero.current_spell.get_cast_range()

        enemy_cords = self.finding_enemy(cast_range)
        found_enemy = enemy_cords is not None

        if not found_enemy:
            print (
                'Nothing in range' + str(hero.current_spell.get_cast_range()))
            return 0

        enemy_y = enemy_cords[0]
        enemy_x = enemy_cords[1]
        enemy = Fights.make_enemy()

        # If we have found enemy, hero stats fighting until s.o. dies
        Fights.attack_enemy(hero, enemy, on_same_field, self.__hero_y, self.__hero_x, enemy_y, enemy_x, self.__map)

        # Someone has died, let's check who
        if not hero.is_alive():
            self.__map[self.__hero_y][self.__hero_x] = Dungeon.enemy_char
            print('Hero is dead')
            return -1
        else:
            print('Enemy is dead')
            self.__map[self.__hero_y][self.__hero_x] = Dungeon.hero_char
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

        is_treasure = False
        is_enemy = False
        is_gate = False

        is_accessible = False
        is_in_matrix = self.__hero_x + \
            dx < len(self.__map[0]) and self.__hero_y + dy < len(self.__map)

        if is_in_matrix:
            checked_points = self.check_accessble_field(dx, dy)
            is_accessible = checked_points[0]
            is_treasure = checked_points[1]
            is_enemy = checked_points[2]
            is_gate = checked_points[3]

        if is_in_matrix and is_accessible:
            self.__map[self.__hero_y][self.__hero_x] = Dungeon.path_char
            self.__hero_x += dx
            self.__hero_y += dy

            hero.take_mana()

            if(is_treasure):
                Treasure_generator.get_treasure(hero)

            if(is_enemy):
                self.hero_attack(hero)
                return False

            if(is_gate):
                # If move hero returns True, we load new level
                return True

            self.__map[self.__hero_y][self.__hero_x] = Dungeon.hero_char

        return False


# move връща True ако се е преместил, False, ако не и -1 ако е умрял :D
    def finding_enemy(self, cast_range):
        for distance in range(0, cast_range + 1):
            cols = len(self.__map[0])
            rows = len(self.__map)

            is_stopped_left = self.__hero_x - distance < 0
            is_stopped_right = self.__hero_x + distance >= cols
            is_stopped_down = self.__hero_y + distance >= rows
            is_stopped_up = self.__hero_y - distance < 0

            if not is_stopped_left and self.__map[self.__hero_y][self.__hero_x - distance] == self.rocks_char:
                is_stopped_left = True

            if not is_stopped_left and self.__map[self.__hero_y][self.__hero_x - distance] == Dungeon.enemy_char:
                enemy_y = self.__hero_y
                enemy_x = self.__hero_x - distance
                return [enemy_y, enemy_x]

            if not is_stopped_right and self.__map[self.__hero_y][self.__hero_x + distance] == self.rocks_char:
                is_stopped_right = True

            if not is_stopped_right and self.__map[self.__hero_y][self.__hero_x + distance] == Dungeon.enemy_char:
                enemy_y = self.__hero_y
                enemy_x = self.__hero_x + distance
                return [enemy_y, enemy_x]

            if not is_stopped_down and self.__map[self.__hero_y + distance][self.__hero_x] == self.rocks_char:
                is_stopped_down = True

            if not is_stopped_down and self.__map[self.__hero_y + distance][self.__hero_x] == Dungeon.enemy_char:
                enemy_y = self.__hero_y + distance
                enemy_x = self.__hero_x
                return [enemy_y, enemy_x]

            if not is_stopped_up and self.__map[self.__hero_y - distance][self.__hero_x] == self.rocks_char:
                is_stopped_up = True

            if not is_stopped_up and self.__map[self.__hero_y - distance][self.__hero_x] == Dungeon.enemy_char:
                enemy_y = self.__hero_y - distance
                enemy_x = self.__hero_x
                return [enemy_y, enemy_x]

    def check_accessble_field(self, dx, dy):
        is_dot = self.__map[
            self.__hero_y + dy][self.__hero_x + dx] == Dungeon.path_char
        is_treasure = self.__map[
            self.__hero_y + dy][self.__hero_x + dx] == Dungeon.treasure_char
        is_enemy = self.__map[
            self.__hero_y + dy][self.__hero_x + dx] == Dungeon.enemy_char
        is_gate = self.__map[
            self.__hero_y + dy][self.__hero_x + dx] == Dungeon.gate_char
        is_spawn_point = self.__map[
            self.__hero_y + dy][self.__hero_x + dx] == Dungeon.spawning_char

        is_accessible = is_dot or is_treasure or is_enemy or is_gate or is_spawn_point

        return [is_accessible, is_treasure, is_enemy, is_gate]
