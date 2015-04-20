from creature_class import Creature
from Weapon import Weapon
from Spell import Spell


class Hero(Creature):
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.mana_regeneration_rate = kwargs['mana_regeneration_rate']

        self.starting_health = kwargs['health']
        self.starting_mana = kwargs['mana']

        self.current_spell = None
        self.current_weapon = Weapon(name="Hands", damage=20)

    def known_as(self):
        return "{} known as the {}".format(self.name, self.title)

    def take_healing(self, healing_points):
        self.health = min(self.starting_health, self.health + healing_points)

    def take_mana(self, *args):
        if len(args) == 0:
            mana_value = self.mana + self.mana_regeneration_rate
            self.mana = min(self.starting_mana, mana_value)
        else:
            mana_value = self.mana + args[0]
            self.mana = min(self.starting_mana, mana_value)

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
