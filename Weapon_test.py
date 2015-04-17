import unittest
from Weapon import Weapon


class Test_Weapon(unittest.TestCase):

    def setUp(self):
        self.w = Weapon(name="The Axe of Destiny", damage=20)

    def test_init(self):
        self.assertEqual(self.w.get_name(), "The Axe of Destiny")
        self.assertEqual(self.w.get_damage(), 20)

    def test_save(self):
        self.assertEqual(self.w.prepare_json(), {
            "name": "The Axe of Destiny",
            "damage": 20
        })

if __name__ == '__main__':
    unittest.main()
