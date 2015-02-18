<<<<<<< Updated upstream
class Card:
    """Represents a playing card

    Attributes:
        rank: integer 1-13, Ace - King
        suit: integer 0-3, Clubs, Diamonds, Hearts, Spades
    """
    
    suits = {0:'Clubs',
             1:'Diamonds',
             2:'Hearts',
             3:'Spades'}

    ranks = {1:'Ace',
             2: '2',
             3: '3',
             4: '4',
             5: '5',
             6: '6',
             7: '7',
             8: '8',
             9: '9',
             10: '10',
             11: 'Jack',
             12: 'Queen',
             13: 'King'}

    def __init__(self, rank, suit):
        assert isinstance(rank, int), "rank is not an int"
        assert isinstance(suit, int), "suit is not an int"
        assert rank >= 1 and rank <= 13
        assert suit >= 0 and suit <= 3
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Return human readable representation"""
<<<<<<< Updated upstream
        return "{} of {}".format(self.ranks[self.rank], self.suits[self.suit])
=======
<<<<<<< Updated upstream
        return "{} of {}".format(self.ranks[self.rank], self.suits[self.suit])
=======
        return "{} of {}".format(self.ranks[self.rank], self.suits[self.suit])
=======
#!/usr/bin/env python3
"""

    This class represents a Card Object that
    will be located in either a Deck or a
    Player's Hand.  The Card holds some
    information about the Card, namely
    the Name, Value, and Suit

    __authors__ = [
        "Jared Bosco",
        "Your name",
        ]

"""


class Card(object):
    """

    Very basic implementation of a Card ( acts as a Node ).

    Holds no data besides its state, and has a method for
    nicely printing out the Card's states / attributes

    """


    def __init__(self, name, value, suit):
        """

        Initialize the Card Object with given parameters

        :param name: (string) - The name of the card ("Ace", "One", "Jack")
        :param value: (int) - The integer value to compare card rankings
        :param suit: (string) - The suit of the card ("diamonds","clubs")

        :return: a newly initialized Card Object ( inherently None )
        """


        self.name = name
        self.value = value
        self.suit = suit

    def __str__(self):
        """

        Nicely print out the attributes of the referenced card object

        :return: (string) - The string displaying the attributes of the
                            Card Object

        """

        return self.name + " of " + self.suit

if __name__ == '__main__':
    pass
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
