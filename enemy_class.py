from creature_class import Creature
from Weapon import Weapon
from Spell import Spell


class Enemy(Creature):
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']

        self.damage = kwargs['damage']

        self.current_spell = None
        self.current_weapon = None

    def attack(self, **kwargs):
        if kwargs['by'] == "weapon":
            if self.current_weapon is None:
                return 0
            else:
                return self.current_weapon.get_damage()

        if kwargs['by'] == "magic":
            if self.current_spell is None:
                return 0
            else:
                return self.current_spell.get_damage()
