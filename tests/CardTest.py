"""

    CardTest.py is the unittest to test the
    implementation of the methods located within
    game/Card.py - using python3

    __authors__ = ["Raymond Wong",
                   "Your name",
                  ]

    Date Created:  Saturday, February 28th, 2015

"""


import unittest
from engine import Card as c

class CardTest(unittest.TestCase):

    def test_joker(self):
        self.assertEqual(str(c.Card(0, 0)), 'Joker')

    def test_ace(self):
        self.assertEqual(str(c.Card(1, 4)), 'Ace of Spades')

    def test_joker_rank(self):
        self.assertEqual(c.Card(0, 0).getRank(), 0)
    
    def test_joker_suit(self):
        self.assertEqual(c.Card(0, 0).getSuit(), 0)
    
    def test_ace_rank(self):
        self.assertEqual(c.Card(1, 4).getRank(), 1)
    
    def test_ace_suit(self):
        self.assertEqual(c.Card(1, 4).getSuit(), 4)

    def test_ace_rank_value(self):
        self.assertEquals(c.Card(1, 4).getRankValue(), 'Ace')

    def test_ace_rank_suit(self):
        self.assertEquals(c.Card(1, 4).getSuitValue(), 'Spades')

    def test_set_rank_string(self):
#        self.assertRaises(AssertionError, lambda: c.Card("string", 1))
        with self.assertRaises(AssertionError):
            c.Card("string", 1)

    def test_set_suit_string(self):
        with self.assertRaises(AssertionError):
            c.Card(1, "string")

    def test_set_rank_value1(self):
        with self.assertRaises(AssertionError):
            c.Card(-1, 0)

    def test_set_rank_value2(self):
        with self.assertRaises(AssertionError):
            c.Card(14, 0)

    def test_set_suit_value1(self):
        with self.assertRaises(AssertionError):
            c.Card(1, -1)

    def test_set_suit_value2(self):
        with self.assertRaises(AssertionError):
            c.Card(1, 5)

    def blue_eyes_white_dragon(self):
        blue_eyes = c.Card(0, 0)
        blue_eyes.updateRanks("Blue Eyes White Dragon")
        blue_eyes.setCard(14, 0)
        return blue_eyes

    def test_update_rank1(self):
        text = "Blue Eyes White Dragon"
        blue_eyes = self.blue_eyes_white_dragon()
#        blue_eyes.printRanks()
        self.assertEquals(str(blue_eyes), text)
        
    def test_update_rank2(self):
        joker = c.Card(0, 0)
        with self.assertRaises(AssertionError):
            joker.updateRanks(0)

    def test_update_rank3(self):
        joker = c.Card(0, 0)
        with self.assertRaises(AssertionError):
            joker.updateRanks("")

    def test_update_suit1(self):
        text = "Cups"
        joker = c.Card(0, 0)
        joker.updateSuits(text)
        joker.setCard(0, 5)
        r = joker.getRankValue()
        self.assertEquals(str(joker), "{} of {}".format(r, text))

    def test_update_suit2(self):
        joker = c.Card(0, 0)
        with self.assertRaises(AssertionError):
            joker.updateSuits(0)

    def test_update_suit3(self):
        joker = c.Card(0, 0)
        with self.assertRaises(AssertionError):
            joker.updateSuits("")

    def test_equals1(self):
        ace1 = c.Card(1, 4)
        ace2 = c.Card(1, 4)
        self.assertTrue(ace1.equals(ace2))

    def test_equals2(self):
        ace1 = c.Card(1, 4)
        ace2 = c.Card(1, 3)
        self.assertFalse(ace1.equals(ace2))

    def test_equals3(self):
        ace1 = c.Card(1, 4)
        two = c.Card(2, 4)
        self.assertFalse(ace1.equals(two))

    def test_equals4(self):
        ace1 = c.Card(1, 4)
        with self.assertRaises(AssertionError):
            ace1.equals("string")

if __name__ == '__main__':
    unittest.main()
