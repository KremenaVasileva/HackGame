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
