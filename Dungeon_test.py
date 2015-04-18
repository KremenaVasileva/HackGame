import unittest
from Dungeon import Dungeon
from hero_class import Hero
from Dungeon import Wrong_direction


class Test_Dungeon(unittest.TestCase):

    def setUp(self):
        self.map = Dungeon("level1.txt")
        self.h = Hero(name="Bron", title="Dragonslayer",
                      health=100, mana=100, mana_regeneration_rate=2)

    def test_init(self):
        self.assertEqual(self.map.get_map(), [['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'], ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'], [
                         '#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']])
        self.assertEqual(self.map.get_enemies(), [[2, 5], [2, 9], [3, 2]])

    def test_spawn(self):
        self.map.spawn(self.h)
        self.assertEqual(self.h.mana, self.h.starting_mana)
        self.assertEqual(self.h.health, self.h.starting_health)
        self.assertEqual(self.map.get_hero_x(), 0)
        self.assertEqual(self.map.get_hero_y(), 0)
        self.assertFalse(self.map.spawn(self.h))

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
        self.map.move_hero(self.h, 'down')




if __name__ == '__main__':
    unittest.main()
