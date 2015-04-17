from hero_class import Hero
import unittest


class TestHeroClass(unittest.TestCase):
    def setUp(self, **kwargs):
        self.hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        # self.hero.name = "Bron"
        # self.hero.title = "Dragonslayer"
        # self.hero.health = 100
        # self.hero.mana = 100
        # self.hero.mana_regeneration_rate = 2

    def test_init(self):
        self.assertEqual(self.hero.name, "Bron")
        self.assertEqual(self.hero.title, "Dragonslayer")
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.mana, 100)
        self.assertEqual(self.hero.mana_regeneration_rate, 2)
        self.assertTrue(isinstance(self.hero, Hero))

        self.assertEqual(self.hero.starting_health, 100)
        self.assertEqual(self.hero.starting_mana, 100)

    def test_known_as(self):
        needed_result = "Bron known as the Dragonslayer"
        self.assertEqual(self.hero.known_as(), needed_result)

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), 100)

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())
        self.hero.health = 0
        self.assertFalse(self.hero.is_alive())

    def test_can_cast(self):
        pass

    def test_take_damage(self):
        needed_result = 100 - 60
        self.assertEqual(needed_result, self.hero.take_damage(60))
        self.assertEqual(0, self.hero.take_damage(120))

    def test_take_healing(self):
        self.assertEqual(100, self.hero.take_healing(20))
        self.hero.health = 20
        needed_result = 20 + 50
        self.assertEqual(needed_result, self.hero.take_healing(50))

    def test_take_mana_no_args(self):
        self.assertEqual(100, self.hero.take_mana())
        self.hero.mana = 90
        needed_result = self.hero.mana + self.hero.mana_regeneration_rate
        self.assertEqual(needed_result, self.hero.take_mana())

    def test_take_mana_with_arg(self):
        self.assertEqual(100, self.hero.take_mana(20))
        self.hero.mana = 20
        mana_points = 60
        needed_result = self.hero.mana + mana_points
        self.assertEqual(needed_result, self.hero.take_mana(60))

if __name__ == '__main__':
    unittest.main()
