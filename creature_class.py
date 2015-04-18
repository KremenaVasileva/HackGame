class Creature:
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.current_spell = None
        self.current_weapon = None

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def can_cast(self):
        if self.current_spell is None:
            return False
        else:
            spell_damage = (self.current_spell).get_damage()
            return (self.get_mana() - spell_damage)

    def take_damage(self, damage_points):
        return max(0, self.health - damage_points)

    def equip(self, weapon):
        self.current_weapon = weapon

    def learn(self, spell):
        self.current_spell = spell
