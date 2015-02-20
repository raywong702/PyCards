class Card(object):
    """Represents a playing card

    Attributes:
        rank: integer 1-13, Ace - King
        suit: integer 0-3, Clubs, Diamonds, Hearts, Spades

    Use the accessor methods getRank() and getSuit()
    """
    
    __suits = {0:None,
               1:'Clubs',
               2:'Diamonds',
               3:'Hearts',
               4:'Spades'}

    __ranks = {0:'Joker',
               1:'Ace',
               2:'2',
               3:'3',
               4:'4',
               5:'5',
               6:'6',
               7:'7',
               8:'8',
               9:'9',
               10:'10',
               11:'Jack',
               12:'Queen',
               13:'King'}

    def __init__(self, rank, suit):
        assert isinstance(rank, int), "rank is not an int"
        assert isinstance(suit, int), "suit is not an int"
        assert rank >= 0 and rank <= 13
        assert suit >= 0 and suit <= 4

        assert rank >= 0 and rank <= 14, "rank must be 1-14"
        assert suit >= 0 and suit <= 4, "suit must be 0-4"
        self.__rank = rank
        self.__suit = suit

    def __str__(self):
        """Return human readable representation"""
        if self.getSuit() > 0:
            return "{} of {}".format(self.__ranks[self.__rank],
                                     self.__suits[self.__suit])
        else:
            return "{}".format(self.__ranks[self.__rank])

    def getRank(self):
        return self.__rank

    def getSuit(self):
        return self.__suit

if __name__ == '__main__':
    pass
