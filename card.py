# -*- coding: utf-8 -*-
# author: fanko24@gmail.com

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s%s" %(self.suit.symbol, self.rank.symbol)
    # compare of cards for
    def __lt__(self, other):
        return self.rank.order < other.rank.order

    def __eq__(self, other):
        return self.rank.order == other.rank.order

    def __gt__(self, other):
        return self.rank.order > other.rank.order
