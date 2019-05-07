# -*- coding: utf-8 -*-
# author: fanko24@gmail.com

class Rank:
    # name, symbol and order of the rank
    __rank_dict = {
            "ace": ("A", 14),
            "king": ("K", 13),
            "queen": ("Q", 12),
            "jack": ("J", 11),
            "ten": ("10", 10),
            "nine": ("9", 9),
            "eight": ("8", 8),
            "seven": ("7", 7),
            "six": ("6", 6),
            "five": ("5", 5),
            "four": ("4", 4),
            "three": ("3", 3),
            "two": ("2", 2)
            }
    
    def __init__(self, name):
        if name in self.__rank_dict:
            self.name = name
            self.symbol = self.__rank_dict[name][0]
            self.order = self.__rank_dict[name][1]
