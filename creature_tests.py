from Spell import Spell
from creature_class import Creature
import unittest


class TestCreatureClass(unittest.TestCase):
    def setUp(self, **kwargs):
        self.creature = Creature(health=200, mana=100)

    def test_init(self):
        self.assertEqual(self.creature.health, 200)
        self.assertEqual(self.creature.mana, 100)

        self.assertEqual(self.creature.current_spell, None)

    def test_get_health(self):
        self.assertEqual(self.creature.get_health(), 200)

    def test_get_mana(self):
        self.assertEqual(self.creature.get_mana(), 100)

    def test_is_alive(self):
        self.assertTrue(self.creature.is_alive())
        self.creature.health = 0
        self.assertFalse(self.creature.is_alive())

    def test_can_cast(self):
        self.assertFalse(self.creature.can_cast())
        self.creature.current_spell = Spell(mana_cost=50, damage=30, name="Fireball", cast_range=2)
        self.assertTrue(self.creature.can_cast())

    def test_take_damage(self):
        damage_points = 60
        needed_result = self.creature.get_health() - damage_points
        self.assertEqual(needed_result, self.creature.take_damage(60))
        self.assertEqual(0, self.creature.take_damage(220))

if __name__ == '__main__':
    unittest.main()
