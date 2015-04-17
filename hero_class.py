class Hero:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.mana_regeneration_rate = kwargs['mana_regeneration_rate']
        self.starting_health = kwargs['health']
        self.starting_mana = kwargs['mana']

    def known_as(self):
        return "{} known as the {}".format(self.name, self.title)

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
        pass

    def take_damage(self, damage_points):
        return max(0, self.health - damage_points)

    def take_healing(self, healing_points):
        return min(self.starting_health, self.health + healing_points)

    def take_mana(self, *args):
        if len(args) == 0:
            mana_value = self.mana + self.mana_regeneration_rate
            return min(self.starting_mana, mana_value)
        else:
            mana_value = self.mana + args[0]
            return min(self.starting_mana, mana_value)
