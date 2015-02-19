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

        __ERROR1 = "num_of_decks, '{}', is not an int".format(num_of_decks)
        __ERROR2 = ("num_of_decks, '{}', must be "
                    "greater than 0").format(num_of_decks)

        assert isinstance(num_of_decks, int), __ERROR1
        assert num_of_decks >= 0, __ERROR2

        self.__pile = [c.Card(r, s) for r in range(1, 14) for s in range(4)]
        self.__pile *= num_of_decks

    def __str__(self):
        """Return human readable representation of one or more deck of cards"""
        return str([str(card) for card in self.__pile])

    def shuffle(self):
        """Shuffles the deck."""
        shuf(self.__pile)

    def find(self, card):
        """Find index of a specic Card in deck. Return -1 if not found
        
        @param card is an instance of Card class
        """

        ERROR1 = "card, '{}', is not a Card type".format(card)
        assert isinstance(card, c.Card), ERROR1

        index = 0
        rank = card.getRank()
        suit = card.getSuit()

        for e in self.__pile:
            c_rank = e.getRank()
            c_suit = e.getSuit()

            if c_rank == rank and c_suit == suit:
                return index
            index += 1
        return -1
        
    def append(self, card):
        """Add a card to the deck.
       
        @param card is an instance of Card class
        """

        ERROR1 = "card, '{}', is not a Card type".format(card)
        assert isinstance(card, c.Card), ERROR1

        self.__pile.append(card)

    def pop(self):
        """Draw a card from the the deck."""

        return self.__pile.pop()

    def popCard(self, card):
        """Remove a specific card from the deck.
        
        @param card is an instance of Card class
        """

        ERROR1 = "card, '{}', is not a Card type".format(card)
        assert isinstance(card, c.Card), ERROR1

        index = self.find(card)
        if index == -1:
            return None
        else:
            return self.__pile.pop(index) 


if __name__ == '__main__':
    pass

