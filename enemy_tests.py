from enemy_class import Enemy
from Weapon import Weapon
from Spell import Spell
import unittest


class TestEnemyClass(unittest.TestCase):
    def setUp(self, **kwargs):
        self.enemy = Enemy(health=200, mana=100, damage=15)

    def test_init(self):
        self.assertEqual(self.enemy.health, 200)
        self.assertEqual(self.enemy.mana, 100)
        self.assertEqual(self.enemy.damage, 15)
        self.assertTrue(isinstance(self.enemy, Enemy))

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 200)
        self.enemy.health = 25
        self.assertEqual(self.enemy.get_health(), 25)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), 100)

    def test_is_alive(self):
        self.assertTrue(self.enemy.is_alive())
        self.enemy.health = 0
        self.assertFalse(self.enemy.is_alive())

    def test_can_cast(self):
        self.assertFalse(self.enemy.can_cast())
        self.enemy.current_spell = Spell(mana_cost=50, damage=30, name="Fireball", cast_range=2)
        self.assertTrue(self.enemy.can_cast())

    def test_take_damage(self):
        needed_result = 200 - 40  # current_health - the damage taken
        self.assertEqual(needed_result, self.enemy.take_damage(40))
        # health cannot be less than 0
        self.assertEqual(0, self.enemy.take_damage(250))

if __name__ == '__main__':
    unittest.main()
