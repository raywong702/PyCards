"""

    PlayerTest.py is the unittest to test the
    implementation of the methods located within
    game/Player.py - using python3

    __authors__ = ["Raymond Wong",
                   "Your name",
                  ]

    Date Created:  Monday March 4, 2015

"""


import unittest
from engine import Player as p
from engine import Deck as d


class PlayerTest(unittest.TestCase):

    def test_get_name(self):
        deck = d.Deck(0)
        player1 = p.Player("player1", deck)
        self.assertEqual(player1.getName(), "player1")

    def test_init1(self):
        deck = d.Deck(0)
        with self.assertRaises(AssertionError):
            p.Player(1, deck)

    def test_init2(self):
        deck = d.Deck(0)
        with self.assertRaises(AssertionError):
            p.Player("", deck)

    def test_init3(self):
        with self.assertRaises(AssertionError):
            p.Player("player1", "string")

    def test_init4(self):
        with self.assertRaises(AssertionError):
            p.Player("player1", None)



if __name__ == '__main__':
    unittest.main()
