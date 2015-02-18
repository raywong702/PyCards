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
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Return human readable representation"""
        return "{} of {}".format(self.ranks[self.rank], self.suits[self.suit])