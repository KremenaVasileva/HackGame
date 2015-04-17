import unittest
from Spell import Spell


class Test_Spell(unittest.TestCase):

    def setUp(self):
        self.s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

    def test_init(self):
        self.assertEqual(self.s.get_name(), "Fireball")
        self.assertEqual(self.s.get_damage(), 30)
        self.assertEqual(self.s.get_mana_cost(), 50)
        self.assertEqual(self.s.get_cast_range(), 2)

    def test_save(self):
        self.assertEqual(self.s.prepare_json(), {
            "name": "Fireball",
            "damage": 30,
            "mana_cost": 50,
            "cast_range": 2
        })

if __name__ == '__main__':
    unittest.main()
