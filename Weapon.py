import random
import json


class Weapon:

    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__damage = kwargs['damage']

    def __str__(self):
        return "Weapon {} with damage {}".format(self.__name, self.__damage)

    @staticmethod
    def load_weapon_from_file(filename):
        with open(filename) as f:
            contents = f.read()
            data = json.loads(contents)
            str_weapon = data[random.randint(0, len(data) - 1)]
            return Weapon(name=str_weapon['name'], damage=str_weapon['damage'])

    def prepare_json(self):
        data = {
            "name": self.__name,
            "damage": self.__damage
        }
        return data

    def save(self, filename):
        with open(filename, "w+") as f:
            f.write(json.dumps(self.prepare_json(), 4))

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage
