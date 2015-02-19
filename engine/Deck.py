from random import shuffle as shuf
import Card as c

class Deck(object):
    """Represents one or more deck of cards

    Attributes:
        pile: the deck of cards. Defaults to 1 deck of cards, but can be more.
    """

    def __init__(self, num_of_decks = 1):
        """Creates the deck of cards

        @param num_of_decks is the amount of 52 card decks you want
        defaults to one 52 card deck
        """

        assert isinstance(num_of_decks, int), "num_of_decks is not an int"
        assert num_of_decks >= 0, "num_of_decks must be greater than 0"
        self.pile = [c.Card(r, s) for r in range(1, 14) for s in range(4)] * num_of_decks

    def __str__(self):
        """Return human readable representation of one or more deck of cards"""
        return str([str(card) for card in self.pile])

    def shuffle(self):
        """Shuffles the deck"""
        shuf(self.pile)

if __name__ == '__main__':
    pass

