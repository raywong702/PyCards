from random import shuffle as shuf
from random import randint as rint
import Card as c

class Deck(object):
    """Represents one or more deck of cards

    Attributes:
        pile: the deck of cards. Defaults to 1 deck of cards, but can be more.

    @author Raymond Wong
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

        self.__pile = [c.Card(r, s) for r in range(1, 14) for s in range(1, 5)]
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

        for index, cur_card in enumerate(self.__pile):
            if cur_card.equals(card):
                return index
        return -1

    def append(self, card):
        """Add a card to the deck.
       
        @param card is an instance of Card class
        """

        ERROR1 = "card, '{}', is not a Card type".format(card)
        assert isinstance(card, c.Card), ERROR1

        self.__pile.append(card)

    def pop(self, card = None):
        """Draw a card

        @param if nothing passed, take the last card in deck
        @param card, return specific card from deck
        @return returns an instance of Card or None
        """
        if card == None: # no arguments passed
            try:
                return  self.__pile.pop()
            except IndexError:
                return None
        else:
            ERROR1 = "card, '{}', is not a Card type".format(card)
            assert isinstance(card, c.Card), ERROR1

            index = self.find(card)
            if index == -1:
                return None
            else:
                return self.__pile.pop(index) 

    def popRandomCard(self):
        """Draw a random card from the deck

        @return returns an instance of Card or None
        """
        if self.__pile:         # not empty
            index = rint(0, len(self.__pile) - 1)
            return self.__pile.pop(index)
        return None


if __name__ == '__main__':
    pass

