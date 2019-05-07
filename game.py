# -*- coding: utf-8 -*-

import sys
from poker import Poker
from player import Player
from hand import Hand

hand_dict = {
        9: "straight-flush",
        8: "quads",
        7: "full-house",
        6: "flush",
        5: "straight", 
        4: "three-kind",
        3: "two-pair",
        2: "pair",
        1: "high"
          }

class Game:
    def __init__(self, number):
        self.winner = -1
        self.player_number = number
        self.player_list = [Player(i+1) for i in range(self.player_number)]
        self.poker = Poker()
        self.public_cards = []
        self.__begin()
        self.__flop()
        self.__turn()
        self.__river()
        for player in self.player_list:
            player.hand = Hand(player.cards, self.public_cards)
        self.__winner()

    # deal a card with every player for two round
    def __begin(self):
        for round in range(2):
            for player in self.player_list:
                player.cards.append(self.poker.card_list.pop())

    # deal the flop card
    def __flop(self):
        self.poker.card_list.pop()
        for i in range(3):
            self.public_cards.append(self.poker.card_list.pop())

    # deal the turn card
    def __turn(self):
        self.poker.card_list.pop()
        self.public_cards.append(self.poker.card_list.pop())

    # deal the river card
    def __river(self):
        self.poker.card_list.pop()
        self.public_cards.append(self.poker.card_list.pop())
    
    # the winner
    def __winner(self):
        value = [0] * 6
        for key, player in enumerate(self.player_list):
            if player.hand.best_value > value:
                value = player.hand.best_value
                self.winner = key

    # show the process of the game
    def __str__(self):
        game_list = []
        game_list.append("-"*40)
        for key, player in enumerate(self.player_list):
            game_list.append("The hole cards for player No %d are : %s" %(key+1, " ".join([str(ca) for ca in player.cards])))
        game_list.append("The flop cards are : " + " ".join([str(ca) for ca in self.public_cards[:3]]))
        game_list.append("The turn card is : " + str(self.public_cards[3]))
        game_list.append("The river card is : " + str(self.public_cards[4]))
        for key, player in enumerate(self.player_list):
            game_list.append("The result for player NO %d is : %s" %(key+1, player.hand))
        game_list.append("The winner is NO %d player" %(self.winner+1))
        return "\n".join(game_list)

