"""

    DeckTest.py is the unittest to test the
    implementation of the methods located within
    game/Deck.py - using python3

    __authors__ = ["Raymond Wong",
                   "Your name",
                  ]

    Date Created:  Sunday March 1, 2015

"""


import unittest
from engine import Card as c
from engine import Deck as d


class DeckTest(unittest.TestCase):

    def get_deck_string(self):
        deck_string = ("'Ace of Clubs', "
                       "'Ace of Diamonds', "
                       "'Ace of Hearts', "
                       "'Ace of Spades', "
                       "'2 of Clubs', "
                       "'2 of Diamonds', "
                       "'2 of Hearts', "
                       "'2 of Spades', "
                       "'3 of Clubs', "
                       "'3 of Diamonds', "
                       "'3 of Hearts', "
                       "'3 of Spades', "
                       "'4 of Clubs', "
                       "'4 of Diamonds', "
                       "'4 of Hearts', "
                       "'4 of Spades', "
                       "'5 of Clubs', "
                       "'5 of Diamonds', "
                       "'5 of Hearts', "
                       "'5 of Spades', "
                       "'6 of Clubs', "
                       "'6 of Diamonds', "
                       "'6 of Hearts', "
                       "'6 of Spades', "
                       "'7 of Clubs', "
                       "'7 of Diamonds', "
                       "'7 of Hearts', "
                       "'7 of Spades', "
                       "'8 of Clubs', "
                       "'8 of Diamonds', "
                       "'8 of Hearts', "
                       "'8 of Spades', "
                       "'9 of Clubs', "
                       "'9 of Diamonds', "
                       "'9 of Hearts', "
                       "'9 of Spades', "
                       "'10 of Clubs', "
                       "'10 of Diamonds', "
                       "'10 of Hearts', "
                       "'10 of Spades', "
                       "'Jack of Clubs', "
                       "'Jack of Diamonds', "
                       "'Jack of Hearts', "
                       "'Jack of Spades', "
                       "'Queen of Clubs', "
                       "'Queen of Diamonds', "
                       "'Queen of Hearts', "
                       "'Queen of Spades', "
                       "'King of Clubs', "
                       "'King of Diamonds', "
                       "'King of Hearts', "
                       "'King of Spades'")
        return deck_string
	




    def test_init_zero(self):
        deck = d.Deck(0)
        self.assertEqual(str(deck), "[]")

    def test_init_default(self):
        deck_string = self.get_deck_string()
        deck_string = "[" + deck_string + "]"
        deck = d.Deck()
        self.assertEqual(str(deck), deck_string)

    def test_init_multideck(self):
        deck_string = self.get_deck_string()
        deck_string = "[" + deck_string + ", " + deck_string + "]"
        deck = d.Deck(2)
        self.assertEqual(str(deck), deck_string)

    def test_init_invalid1(self):
        with self.assertRaises(AssertionError):
            d.Deck("string")
    
    def test_init_invalid2(self):
        with self.assertRaises(AssertionError):
            d.Deck(-1)

    def test_shuffle(self):
        deck_string = self.get_deck_string()
        deck_string = "[" + deck_string + "]"
        deck = d.Deck()
        deck.shuffle()
        self.assertNotEqual(str(deck), deck_string)

    def test_find_aoc1(self):
        card = c.Card(1, 1)
        deck = d.Deck()
        self.assertEqual(deck.find(card), 0)

    def test_find_aoc2(self):
        card = c.Card(1, 1)
        deck = d.Deck(2)
        self.assertEqual(deck.find(card), 0)

    def test_find_aoc3(self):
        card = c.Card(1, 1)
        deck = d.Deck(2)
        deck.pop(card)
        self.assertEqual(deck.find(card), 51)

    def test_find_kos(self):
        card = c.Card(13, 4)
        deck = d.Deck()
        self.assertEqual(deck.find(card), 51)

    def test_find_7oh(self):
        card = c.Card(7, 3)
        deck = d.Deck()
        self.assertEqual(deck.find(card), 26)

    def test_find_joker(self):
        card = c.Card(0, 0)
        deck = d.Deck()
        self.assertEqual(deck.find(card), -1)

    def test_find_invalid(self):
        deck = d.Deck()
        with self.assertRaises(AssertionError):
            deck.find("string")

    def test_append1(self):
        card = c.Card(1, 4)
        deck = d.Deck(0)
        deck.append(card)
        self.assertEqual(str(deck), "['Ace of Spades']")

    def test_append2(self):
        with self.assertRaises(AssertionError):
            d.Deck("string")

    def test_pop1(self):
        card = c.Card(1, 4)
        deck = d.Deck()
        deck.append(card)
        self.assertEqual(deck.pop(), card)

    def test_pop1(self):
        card = c.Card(1, 4)
        deck = d.Deck()
        deck.append(card)
        self.assertEqual(deck.pop(), card)

    def test_pop2(self):
        deck = d.Deck()
        deck.shuffle()
        self.assertTrue(isinstance(deck.pop(), c.Card))

    def test_pop3(self):
        deck = d.Deck(0)
        self.assertEqual(deck.pop(), None)

    def test_pop4(self):
        card = c.Card(0, 0)
        deck = d.Deck()
        self.assertEqual(deck.pop(card), None)

    def test_pop5(self):
        with self.assertRaises(AssertionError):
            d.Deck().pop("string")

    def test_popRandomCard1(self):
        deck = d.Deck()
        self.assertTrue(isinstance(deck.popRandomCard(), c.Card))

    def test_popRandomCard2(self):
        deck = d.Deck(0)
        self.assertEqual(deck.popRandomCard(), None)

if __name__ == '__main__':
    unittest.main()
