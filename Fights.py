from enemy_class import Enemy
import json
import random
from Spell import Spell
from Weapon import Weapon


class Fights:

    @staticmethod
    def load_rand_enemy():
        filename = 'enemies.json'
        with open(filename) as f:
            contents = f.read()
            data = json.loads(contents)
            str_enemy = data[random.randint(0, len(data) - 1)]
            mana = str_enemy['mana']
            health = str_enemy['health']
            damage = str_enemy['damage']
            return Enemy(health=health, mana=mana, damage=damage)

    @staticmethod
    def make_enemy():
        enemy = Fights.load_rand_enemy()
        enemy.equip(Weapon.load_weapon_from_file('weapons.json'))
        enemy.learn(Spell.load_spell_from_file('spells.json'))
        return enemy

    @staticmethod
    def attack_by_spell(attacked_creature, attacking_creature, type_creature, type_creature_attacked, fighting_tool):
        result = ''
        attacked_creature.take_damage(
            attacking_creature.attack(by='magic'))
        result = '{} casts a '.format(type_creature)
        result += fighting_tool.get_name()
        result += ', hits {} for '.format(type_creature_attacked)
        result += str(attacking_creature.attack(by='magic'))
        result += '. {} health is '.format(type_creature_attacked)
        result += str(attacked_creature.get_health())

        return result

    @staticmethod
    def attack_by_weapon(attacked_creature, attacking_creature, type_creature, type_creature_attacked, fighting_tool):
        result = ''
        attacked_creature.take_damage(
            attacking_creature.attack(by='weapon'))
        result = '{} hits with '.format(type_creature)
        result += fighting_tool.get_name()
        result += ' for ' + str(attacking_creature.attack(by='weapon'))
        result += '. {} health is '.format(type_creature_attacked)
        result += str(attacked_creature.get_health())

        return result

    @staticmethod
    def spell_or_weapon(creature):
        if creature.can_cast() and creature.attack(by='magic') > creature.attack(by='weapon'):
            return creature.current_spell
        else:
            return creature.current_weapon

    @staticmethod
    def move_enemy(hero_y, hero_x, enemy_y, enemy_x, level_map, enemy_char, path_char):
        moves = ''
        if enemy_x > hero_x:
            moves = 'to the left'
            enemy_x -= 1
        elif enemy_x < hero_x:
            moves = 'to the right'
            enemy_x += 1
        elif enemy_y > hero_y:
            moves = 'up'
            enemy_y -= 1
        elif enemy_y < hero_y:
            moves = 'down'
            enemy_y += 1
        print('Enemy moves one square ' + moves +
              ' in order to get to the hero. This is his move.')
        return [enemy_y, enemy_x]

    @staticmethod
    def attack_enemy(hero, enemy, on_same_field, hero_y, hero_x, enemy_y, enemy_x, level_map):
        isFightingOn = hero.is_alive() and enemy.is_alive()
        level_map[enemy_y][enemy_x] = '.'
        while isFightingOn:

            # First move: Hero attacks
            fighting_tool = Fights.spell_or_weapon(hero)
            if not on_same_field:
                print(
                    Fights.attack_by_spell(enemy, hero, 'Hero', 'Enemy', hero.current_spell))
            else:
                if isinstance(fighting_tool, Spell):
                    print(
                        Fights.attack_by_spell(enemy, hero, 'Hero', 'Enemy', hero.current_spell))
                else:
                    print(
                        Fights.attack_by_weapon(enemy, hero, 'Hero', 'Enemy', hero.current_weapon))

            isFightingOn = hero.is_alive() and enemy.is_alive()
            if not isFightingOn:
                break

            # Second move: enemy attacks or moves forward
            # If enemy has reached hero:
            if on_same_field:
                fighting_tool = Fights.spell_or_weapon(enemy)
                if isinstance(fighting_tool, Spell):
                    print(
                        Fights.attack_by_spell(hero, enemy, 'Enemy', 'Hero', enemy.current_spell))
                else:
                    print(Fights.attack_by_weapon(
                        hero, enemy, 'Enemy', 'Enemy', enemy.current_weapon))
            else:
                # Enemy has not reached hero, so he moves

                enemy_cords = Fights.move_enemy(hero_y, hero_x, enemy_y, enemy_x, level_map, 'E', '.')
                enemy_y = enemy_cords[0]
                enemy_x = enemy_cords[1]

            isFightingOn = hero.is_alive() and enemy.is_alive()
            if not isFightingOn:
                break

        if enemy.is_alive():
            level_map[hero_y][hero_x] = 'E'


