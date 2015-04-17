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


if __name__ == '__main__':
    unittest.main()

