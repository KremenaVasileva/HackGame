from Treasure_generator import Treasure_generator


class Wrong_direction(Exception):
    pass


class Dungeon:

    def __init__(self, filename):
        # Position of our hero
        # He's nowherer if x and y are -1
        self.__hero_x = -1
        self.__hero_y = -1
        self.__map = []
        self.__spawning_points = []
        # making matrix
        with open(filename, "r") as f:
            for line in f:
                row = []
                for char in line:
                    row.append(char)
                    # Finding hero's first spawning points coordinates
                    if char == 'S':
                        coords = []
                        # Y
                        coords.append(len(self.__map))
                        # X
                        coords.append(len(self.__row))
                        self.__spawning_points.append(coords)
                self.__map.append(row)


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
            self.__hero_y = self.__spawning_points[0][1]
            self.__spawning_points = self.__spawning_points[1:]
            self.__map[self.__hero_y][self.__hero_x] = 'H'
            return True

    def move_hero(self, hero, direction):
        # Does hero exist? If it doesn't
        if self.__hero_y == -1 and self.__hero_x == -1:
            self.spawn(hero)

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



