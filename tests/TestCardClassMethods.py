#!/usr/bin/env python3
"""

    TestCardClassMethods.py is the unittest to test the
    implementation of the methods located within
    game/Card.py - using python3

    __authors__ = [
        "Jared Bosco",
        "Your name",
        ]
    Date Created:  Tuesday, February 17th, 2015

"""

import unittest
import engine.Card # The class we are testing

class TestCardClassMethods(unittest.TestCase):


    def setUp(self):
        self.card = engine.Card.Card(1, 0) # any initial set up that must be done

    # Test Methods Should Begin With "test_" followed by what it is testing
    # self.assertEqual(value, known_value) <- testing that output is what is should be equal to
    # self.assertTrue(condition) <- testing that the condition is True
    # self.assertRaises(TypeError) <- testing that the correct error is raised appropriately and handled

    def test_constructor(self):
        self.assertEqual(self.card.rank, 1)
        self.assertEqual(self.card.suit, 0)

    def test_print_card(self):
        self.assertEqual(str(self.card), "Ace of Clubs")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCardClassMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

