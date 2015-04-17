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
        pass
