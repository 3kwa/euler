"""
Probably doesn't cover all the possibilities but the test cases given in the
problem formulation and returns the expected result
"""

from collections import Counter

class Card(object):
    """
    >>> qh = Card('QH')
    >>> jc = Card('JC')
    >>> qh > jc
    True
    >>> qh < jc
    False
    >>> qh == Card('QD')
    True
    """

    ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, desc):
        self.value, self.suite = desc

    @property
    def score(self):
        return Card.ORDER.index(self.value)

    def __cmp__(self, other):
        return self.score - other.score

    def __repr__(self):
        return "Card('%s%s')" % (self.value, self.suite)

    def __str__(self):
        return "%s%s" % (self.value, self.suite)


class Hand(object):
    """
    >>> hand = Hand('5H 5C 6S 7S KD')
    >>> hand
    Hand('5H 5C 6S 7S KD')
    >>> hand.cards
    (Card('5H'), Card('5C'), Card('6S'), Card('7S'), Card('KD'))
    """

    def __init__(self, desc):
        self.cards = tuple(Card(card) for card in desc.split(' '))

    def __repr__(self):
        return "Hand('%s')" % ' '.join(map(str, self.cards))

    @property
    def high(self):
        """
        >>> hand = Hand('5H 5C 6S 7S KD')
        >>> hand.high
        'K'
        """
        return max(self.cards).value

    @property
    def pair(self):
        """
        >>> hand = Hand('5H 5C 6S 7S KD')
        >>> hand.pair
        ('5',)
        >>> hand = Hand('5H 5C 6S 6S KD')
        >>> hand.pair
        ('5', '6')
        >>> hand = Hand('5H 6C 7S 8S KD')
        >>> hand.pair
        ()
        """
        counter = Counter(card.value for card in self.cards)
        return tuple(value for value, count in counter.items() if count == 2)

    @property
    def three(self):
        """
        >>> hand = Hand('5H 5C 5S 7S KD')
        >>> hand.three
        '5'
        >>> hand = Hand('5H 5C 8S 7S KD')
        >>> hand.three
        False
        """
        counter = Counter(card.value for card in self.cards)
        try:
            return [value for value, count in counter.items() if count == 3][0]
        except IndexError:
            return False

    @property
    def straight(self):
        """
        >>> hand = Hand('5S 6D 7H 8S 9D')
        >>> hand.straight
        True
        >>> hand = Hand('5S 6D 6H 8S 9D')
        >>> hand.straight
        False
        """
        indexes = [card.score for card in self.cards]
        min_ = min(indexes)
        return sorted([index - min_ for index in indexes]) == [0, 1, 2, 3, 4]

    @property
    def flush(self):
        """
        >>> hand = Hand('5H 5C 6S 7S KD')
        >>> hand.flush
        False
        >>> hand = Hand('5C 5C 6C 7C KC')
        >>> hand.flush
        True
        """
        return len(set(card.suite for card in self.cards)) == 1

    @property
    def full(self):
        """
        >>> hand = Hand('5H 5C 5S KS KD')
        >>> hand.full
        ('5', 'K')
        >>> hand = Hand('5H 5C 6S KS KD')
        >>> hand.full
        False
        """
        if self.pair and self.three:
            return (self.three, self.pair[0])
        return False

    @property
    def four(self):
        """
        >>> hand = Hand('5H 5C 5S KS 5D')
        >>> hand.four
        '5'
        >>> hand = Hand('5H 5C 5S KS KD')
        >>> hand.four
        False
        """
        counter = Counter(card.value for card in self.cards)
        try:
            return [value for value, count in counter.items() if count == 4][0]
        except IndexError:
            return False

    @property
    def rank(self):
        """
        >>> Hand('TH JH QH KH AH').rank
        9
        >>> Hand('9H TH JH QH KH').rank
        8
        """
        if self.flush and self.straight and self.high == 'A':
            return 9
        if self.flush and self.straight:
            return 8
        if self.four:
            return 7
        if self.full:
            return 6
        if self.flush:
            return 5
        if self.straight:
            return 4
        if self.three:
            return 3
        if len(self.pair) == 2:
            return 2
        if len(self.pair) == 1:
            return 1
        return 0

    def __cmp__(self, other):
        """
        >>> player1 = Hand('5H 5C 6S 7S KD')
        >>> player2 = Hand('2C 3S 8S 8D TD')
        >>> player1 > player2
        False
        >>> player1 = Hand('5D 8C 9S JS AC')
        >>> player2 = Hand('2C 5C 7D 8S QH')
        >>> player1 > player2
        True
        >>> player1 = Hand('2D 9C AS AH AC')
        >>> player2 = Hand('3D 6D 7D TD QD')
        >>> player1 > player2
        False
        >>> player1 = Hand('4D 6S 9H QH QC')
        >>> player2 = Hand('3D 6D 7H QD QS')
        >>> player1 > player2
        True
        >>> player1 = Hand('2H 2D 4C 4D 4S')
        >>> player2 = Hand('3C 3D 3S 9S 9D')
        >>> player1 > player2
        True
        """
        if self.rank != other.rank:
            return self.rank - other.rank

        if self.full:
            return Card.ORDER.index(self.full[0]) - Card.ORDER.index(other.full[0])

        if self.pair:
            if self.pair == other.pair:
                return max(card.score for card in self.cards
                    if card.value not in self.pair) - \
                max(card.score for card in other.cards
                    if card.value not in other.pair)
            else:
                return max(Card.ORDER.index(value) for value in self.pair) - \
                max(Card.ORDER.index(value) for value in other.pair)


        return Card.ORDER.index(self.high) - Card.ORDER.index(other.high)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    total = 0
    with open('poker.txt') as f:
        for line in f:
            player1 = Hand(line[:14])
            player2 = Hand(line[15:-2])
            if player1 > player2:
                total += 1
    print total
