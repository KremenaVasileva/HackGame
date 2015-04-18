import unittest
from hero_class import Hero
from Treasure import Treasure


class Test_Treasure(unittest.TestCase):

    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer",
                      health=100, mana=100, mana_regeneration_rate=2)

    def test_get_treasure(self):
        pass
        # I cant make it :D

if __name__ == '__main__':
    unittest.main()
