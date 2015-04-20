import random
from Weapon import Weapon
from Spell import Spell


class Treasure_generator:

    @staticmethod
    def get_treasure(hero):

        rand = random.randint(1, 4)

        if rand == 1:
            # hero.get_starting_mana()
            mana_points = random.randint(10, 200)
            hero.take_mana(mana_points)

            if hero.get_mana() == hero.starting_mana:
                print('Found mana. Hero mana is max.')
            else:
                print('Found mana. Hero mana is {}').format(hero.get_mana())

        elif rand == 2:
            health_points = random.randint(10, 20)
            hero.take_healing(health_points)

            if hero.get_health() == hero.starting_health:
                print('Found health. Hero health is max.')
            else:
                print('Found health. Hero health is {}').format(
                    hero.get_health())

        elif rand == 3:
            w = Weapon.load_weapon_from_file('weapons.json')
            print('Hero took:')
            print(w)
            hero.equip(w)

        else:
            s = Spell.load_spell_from_file('spells.json')
            print('Hero learnt')
            print(s)
<<<<<<< HEAD
            hero.learn()
=======
            hero.learn(s)
>>>>>>> Dungeon-Spell-Weapon-Treasure
