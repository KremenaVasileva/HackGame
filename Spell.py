import random
import json


class Spell:

    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__damage = kwargs['damage']
        self.__mana_cost = kwargs['mana_cost']
        self.__cost_range = kwargs['cost_range']

    @staticmethod
    def load_spell_from_file(filename):
        with open(filename) as f:
            contents = f.read()
            data = json.loads(contents)
            str_spell = data[random.randint(0, len(data) - 1)]
            return Spell(name=str_spell['name'], damage=str_spell['damage'], mana_cost=str_spell['mana_cost'], cost_range=str_spell['cost_range'])

    def prepare_json(self):
        data = {
            "name": self.__name,
            "damage": self.__damage
        }
        return data

    def save(self, filename):
        with open(filename, "w+") as f:
            f.write(json.dumps(self.prepare_json(), 4))

    def get_spell_damage(self):
        return self.__damage

    def get_cast_range(self):
        return self.__cast_range

    def get_mana_cost(self):
        return self.__mana_cost
