# -*- coding: utf-8 -*-
# author: fanko24@gmail.com

class Suit:
    # name and symbol for the suit
    __suit_dict = {
            "heart": "♥",
            "spade": "♠",
            "club": "♣",
            "diamond": "◇"
            }
    
    def __init__(self, name):
        if name in self.__suit_dict:
            self.name = name
            self.symbol = self.__suit_dict[name]
