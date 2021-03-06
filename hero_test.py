from hero_class import Hero
from Weapon import Weapon
from Spell import Spell
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
        self.assertFalse(self.hero.can_cast())
        self.hero.current_spell = Spell(mana_cost=50, damage=30, name="Fireball", cast_range=2)
        self.assertTrue(self.hero.can_cast())

    def test_take_damage(self):
        needed_result = 100 - 60  # current_health - damage taken
        self.hero.take_damage(60)
        self.assertEqual(needed_result, self.hero.get_health())
        # hero health cannot be less than 0
        self.hero.take_damage(2000)
        self.assertEqual(0, self.hero.get_health())

    def test_take_healing(self):
        # hero's current_health cannot be over his starting_healthe
        self.hero.take_healing(20)
        self.assertEqual(100, self.hero.get_health())
        self.hero.health = 20
        needed_result = 20 + 50  # current_health + healing taken
        self.hero.take_healing(50)
        self.assertEqual(needed_result, self.hero.get_health())

    def test_take_mana_no_args(self):
        # hero's current_mana cannot be over his starting_mana
        self.hero.take_mana()
        self.assertEqual(100, self.hero.get_mana())
        self.hero.mana = 90
        needed_result = self.hero.get_mana() + self.hero.mana_regeneration_rate
        self.hero.take_mana()
        self.assertEqual(needed_result, self.hero.get_mana())

    def test_take_mana_with_arg(self):
        # hero's current_mana cannot be over his starting_mana
        self.hero.take_mana(20)
        self.assertEqual(100, self.hero.get_mana())

        self.hero.mana = 20
        mana_points = 70
        needed_result = self.hero.get_mana() + mana_points
        self.hero.take_mana(mana_points)
        self.assertEqual(needed_result, self.hero.get_mana())

    def test_attack_no_weapon(self):
        self.assertEqual(0, self.hero.attack(by="weapon"))

    def test_attack_with_weapon(self):
        weapon = Weapon(name="The Axe of Destiny", damage=20)
        self.hero.equip(weapon)
        self.assertEqual(20, self.hero.attack(by="weapon"))

    def test_attack_no_spell(self):
        self.assertEqual(0, self.hero.attack(by="magic"))

    def test_attack_with_spell(self):
        spell = Spell(mana_cost=50, damage=30, name="Fireball", cast_range=2)
        self.hero.learn(spell)
        self.assertEqual(30, self.hero.attack(by="magic"))

if __name__ == '__main__':
    unittest.main()
