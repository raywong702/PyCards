class Card(object):
    """Represents a playing card

    Attributes:
        rank: integer 1-13, Ace - King
        suit: integer 0-3, Clubs, Diamonds, Hearts, Spades

    Use the accessor methods getRank() and getSuit()

    @author Raymond Wong
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
        self.setCard(rank, suit)

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

    def getRankValue(self):
        return self.__ranks[self.__rank]

    def getSuitValue(self):
        return self.__suits[self.__suit]


    # Create new cards besides thes normal 52 card deck and Jokers
    def updateSuits(self, suit):
        """Add more suits

        @param suit creat a new card suit.
        It is an instance of string.
        """
        assert isinstance(suit, str), "suit '{}' is not a string".format(suit)
        assert suit, "suit is an empty string"
        self.__suits.update({len(self.__suits):suit})

    def updateRanks(self, rank):
        """Add more ranks

        @param rank creat a new card rank.
        It is an instance of string.
        """
        assert isinstance(rank, str), "rank '{}' is not a string".format(rank)
        self.__ranks.update({len(self.__ranks):rank})
        assert rank, "rank is an empty string"
        self.__ranks.update({len(self.__ranks):rank})

    # Set the card. Used for initialization, 
    # Can be used for setting up new cards
    # after running the updateSuits and updateRanks functions
    def setCard(self, rank, suit):
        """Set the card's rank and suit

        @param rank the card's rank
        @param suit the card's suit
        """
        assert isinstance(rank, int), "rank '{}' is not an int".format(rank)
        assert isinstance(suit, int), "suit '{}' is not an int".format(suit)

        __len_ranks = len(self.__ranks)
        __len_suits = len(self.__suits)
        __ERROR1 = "rank '{}' must be 0-{}".format(rank, __len_ranks)
        __ERROR2 = "suit '{}' must be 0-{}".format(suit, __len_suits)

        assert rank >= 0 and rank < __len_ranks, __ERROR1
        assert suit >= 0 and suit < __len_suits, __ERROR2

        self.__rank = rank
        self.__suit = suit

    def equals(self, card):
        """Returns true if card card equals passed in card. 
        Returns false otherwise
        
        @param card. Card type
        """
        ERROR = "card '{}' is not a Card type".format(card)
        assert isinstance(card, Card), ERROR

        if (self.getRank() == card.getRank() and 
                self.getSuit() == card.getSuit()):
            return True
        return False

    def printRanks(self):
        """Prints the card's possible ranks"""
        print(self.__ranks)

    def printSuits(self):
        """Prints the card's possible suits"""
        print(self.__suits)

if __name__ == '__main__':
    pass
