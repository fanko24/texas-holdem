# -*- coding: utf-8 -*-
# author: fanko24@gmail.com

# standard library
import sys
import random
from card import Card
from suit import Suit
from rank import Rank


class Poker:
    suit_list = ["heart", "spade", "club", "diamond"]
    rank_list = ["ace", "king", "queen", "jack", "ten", "nine", "eight", "seven", "six", "five", "four", "three", "two"]
    
    # inintial the pokers
    def __init__(self):
        self.card_list = [Card(Suit(s), Rank(r)) for s in self.suit_list for r in self.rank_list]
        random.shuffle(self.card_list)

    def __str__(self):
        return " ".join([str(item) for item in self.card_list])
