import unittest
from Dungeon import Dungeon


class Test_Dungeon(unittest.TestCase):

    def setUp(self):
        self.map = Dungeon("level1.txt")

    def test_init(self):
        pass

    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
