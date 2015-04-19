import unittest
from Dungeon import Dungeon
from hero_class import Hero
from Dungeon import Wrong_direction
from Weapon import Weapon
from Spell import Spell


class Test_Dungeon(unittest.TestCase):

    def setUp(self):
        self.map = Dungeon("level1.txt")
        self.h = Hero(name="Bron", title="Dragonslayer",
                      health=100, mana=100, mana_regeneration_rate=2)

    def test_init(self):
        self.assertEqual(self.map.get_map(), [['S', '.', '#', '#', '.', '.', 'S', '.', '.', 'T'], ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'], [
                         '#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']])
        self.assertEqual(self.map.get_enemies(), [[2, 5], [2, 9], [3, 2]])

    def test_spawn(self):
        self.map.spawn(self.h)
        self.assertEqual(self.h.mana, self.h.starting_mana)
        self.assertEqual(self.h.health, self.h.starting_health)
        self.assertEqual(self.map.get_hero_x(), 0)
        self.assertEqual(self.map.get_hero_y(), 0)
        self.assertTrue(self.map.spawn(self.h))

    def test_move(self):
        self.map.spawn(self.h)
        self.h.take_damage(90)
        self.assertFalse(self.map.move_hero(self.h, 'up'))
        self.assertTrue(self.map.move_hero(self.h, 'right'))
        with self.assertRaises(Wrong_direction):
            self.assertTrue(self.map.move_hero(self.h, 'hihihi'))
        self.assertEqual(1, self.map.get_hero_x())
        self.assertEqual(0, self.map.get_hero_y())
        self.assertFalse(self.map.move_hero(self.h, 'right'))
        self.assertEqual(1, self.map.get_hero_x())
        self.assertEqual(0, self.map.get_hero_y())
        # self.map.move_hero(self.h, 'down')

    def test_spell_or_weapon(self):
        self.h.equip(Weapon(name="The Axe of Destiny", damage=20))
        self.h.learn(
            Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2))
        self.assertTrue(isinstance(self.map.spell_or_weapon(self.h), Spell))
        self.h.equip(Weapon(name="The Axe of Destiny", damage=120))
        self.assertTrue(isinstance(self.map.spell_or_weapon(self.h), Weapon))

    def test_hero_attack(self):
        self.h.equip(Weapon(name="The Axe of Destiny", damage=20))
        self.h.learn(
            Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2))
        self.map.spawn(self.h)
        self.map.print_map()
        self.map.move_hero(self.h, 'right')
        self.map.print_map()
        self.map.move_hero(self.h, 'down')
        self.map.print_map()
        self.map.move_hero(self.h, 'down')
        self.map.print_map()
        self.map.move_hero(self.h, 'down')
        self.map.print_map()
        # self.assertEqual(self.map.move_hero(self.h, 'right'), True)
        self.map.hero_attack(self.h)
        self.map.print_map()
        for x in range(5):
            self.map.move_hero(self.h, 'right')
        self.map.print_map()
        self.map.move_hero(self.h, 'up')
        self.map.print_map()
        self.map.spawn(self.h)
        self.map.print_map()

if __name__ == '__main__':
    unittest.main()
