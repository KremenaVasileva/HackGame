import random
from Weapon import Weapon
from Spell import Spell


class Treasure_generator:

    @staticmethod
    def get_treasure(hero):

        rand = random.randint(1, 4)

        if rand == 1:
            mana_points = random.randint(hero.__mana)
            hero.take_mana(mana_points)

            if hero.get_mana() == hero.__starting_mana:
                print('Found mana. Hero mana is max.')
            else:
                print('Found mana. Hero mana is {}').format(hero.get_mana())

        elif rand == 2:
            health_points = random.randint(hero.__health)
            hero.take_healing(health_points)

            if hero.get_health() == hero.__starting_health:
                print('Found health. Hero health is max.')
            else:
                print('Found health. Hero health is {}').format(
                    hero.get_health())

        elif rand == 3:
            hero.equip(Weapon.get_random_weapon())

        else:
            hero.learn(Spell.get_random_spell())
