class Card(object):
    """Represents a playing card

    Attributes:
        rank: integer 1-13, Ace - King
        suit: integer 0-3, Clubs, Diamonds, Hearts, Spades
    """
    
    __suits = {0:'Clubs',
             1:'Diamonds',
             2:'Hearts',
             3:'Spades'}

    __ranks = {1:'Ace',
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

        assert rank >= 1 and rank <= 13, "rank must be 1-13"
        assert suit >= 0 and suit <= 3, "suit must be 0-3"
        self.__rank = rank
        self.__suit = suit

    def __str__(self):
        """Return human readable representation"""
        return "{} of {}".format(self.__ranks[self.rank], self.__suits[self.suit])

    def getRank():
        return self.__rank

    def getSuit():
        return self.__suit

if __name__ == '__main__':
    pass
