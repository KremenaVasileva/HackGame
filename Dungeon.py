from Treasure_generator import Treasure_generator


class Wrong_direction(Exception):
    pass


class Dungeon:

    def __init__(self, filename):
        # Position of our hero
        self.__hero_x = 0
        self.__hero_y = 0
        self.__map = []

        # making matrix
        with open(filename, "w+") as f:

            for line in f:
                row = []
                for char in line:
                    row.append(char)
                    # Finding hero's coordinates
                    if char == 'S':
                        self.__hero_y = len(self.__map)
                        self.__hero_x = len(self.__row)
                self.__map.append(row)

    def print_map(self):
        for line in map:
            row = ''
            for char in map:
                row += char
            print(row)

    def spawn(self, hero):
        hero.take_healing(hero.__starting_health)
        hero.take_mana(hero.__starting_mana)
        # Останалата част от spawn-а ми е мистерия :D

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

        if(is_treasure):
            Treasure_generator.get_treasure(hero)

        if(is_enemy):
            # Start Fighting Somehow!
            pass
