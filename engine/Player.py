import Deck as d

class Player(object):
    """Represents a player

    Attributes:
        name: player's name. string type.
        hand: player's hand. Deck type.

    @author Raymond Wong
    """
    
    def __init__(self, name, hand):
        assert isinstance(name, str), "name '{}' is not a string".format(name)
        assert isinstance(hand, d.Deck), ("hand '{}' is not an instance "
                                        "of Deck").format(hand)
        assert name, "name is empty string"

        self.__name = name
        self.hand = hand

    def __str__(self):
        """Return human readable representation"""
        return "Name: {}\nHand: {}".format(self.getName(), str(self.hand))

    def getName(self):
        """Return player's name"""
        return self.__name

if __name__ == '__main__':
    pass
