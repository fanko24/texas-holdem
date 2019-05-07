# -*- coding: utf8 -*-

import sys
from game import *

if __name__ == "__main__":
    player_number = int(sys.argv[1])
    times = int(sys.argv[2])
    res_dict = {}
    fhole = open("best_hole.%s" %(player_number), "a")
    fflop = open("best_flop.%s" %(player_number), "a")
    for i in range(times):
        game = Game(player_number)
        #print game
        for key, player in enumerate(game.player_list):
            if key == game.winner:
                fhole.write(" ".join([str(ca) for ca in player.cards]) + " " + player.hand.hand_dict[player.hand.best_value[0]] + " 1\n")
                fflop.write(" ".join(str(ca) for ca in game.public_cards[:3]) + " " + str(player.hand) + " 1\n")
            else:
                fhole.write(" ".join([str(ca) for ca in player.cards]) + " " + player.hand.hand_dict[player.hand.best_value[0]] + " 0\n")
                fflop.write(" ".join(str(ca) for ca in game.public_cards[:3]) + " " + str(player.hand) + " 0\n")
    fhole.close()
    fflop.close()
