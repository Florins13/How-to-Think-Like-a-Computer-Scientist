

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
    # Suits are the same... check ranks
    # Ex 1
        if self.rank == 1 and other.rank == 1:
            return 0
        if self.rank == 1 and other.rank != 1:
            return 1
        if self.rank != 1 and other.rank == 1:
            return -1
    #
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
    # Ranks are the same... it's a tie
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s


# Ex 2
card2 = Card(1, 1)
card1 = Card(1, 13)
print(card2, card1)
print(card2 > card1)
# print(card2.suits[2])


red_deck = Deck()
# print(red_deck)
