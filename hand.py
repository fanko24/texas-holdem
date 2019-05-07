# -*- coding: utf-8 -*-
# author: fanko24@gmail.com

# standard library
import copy

#  library
from poker import Poker


class Hand:
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
    def __init__(self, hole_list, public_list):
        self.lst = hole_list + public_list
        self.best_hand, self.best_value = self.__get_best_hand()
    
    # pick the best five cards from seven
    def __get_best_hand(self):
        hand = None
        value = [0]*6
        for i in range(len(self.lst)):
            for j in range(i+1, len(self.lst)):
                tmp_lst = copy.copy(self.lst)
                del tmp_lst[j]
                del tmp_lst[i]
                res_value = self.__get_value(tmp_lst)
                if res_value > value:
                    hand = tmp_lst
                    value = res_value
        return hand, value
    
    # get value of the five cards, from 9 to 1: straight flush, quads, full house, flush, straight, three kind, tow pair, pair, high
    def __get_value(self, tmp_lst):
        value = self.__get_straight_flush(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_quads(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_full_house(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_flush(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_straight(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_three_kind(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_two_pair(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_pair(tmp_lst)
        if value[0] != 0:
            return value

        value = self.__get_high(tmp_lst)
        return value

    # get the result of straight flush
    def __get_straight_flush(self, lst):
        value = [0] * 6
        straight_value = self.__get_straight(lst)
        flush_value = self.__get_flush(lst)
        if straight_value[0] != 0 and flush_value[0] != 0:
            value[0] == 9
            value [1] = straight_value[1]
        return value

    # get the result of quads
    def __get_quads(self, lst):
        value = [0] * 6
        order_lst, time_lst = self.__get_order_times(lst)
        if time_lst[0] == 4 and time_lst[1] == 1:
            value [0] = 8
            value[1] = order_lst[0]
            value[2] = order_lst[1]
        return value
    
    # get the result of full house
    def __get_full_house(self, lst):
        value = [0] * 6
        order_lst, time_lst = self.__get_order_times(lst)
        if time_lst[0] == 3 and time_lst[1] == 2:
            value[0] = 7
            value[1] = order_lst[0]
            value[2] = order_lst[1]
        return value
    
    # get the order dict for 5 cards
    def __get_order_times(self, lst):
        dic = {}
        for card in lst:
            if card.rank.order not in dic:
                dic[card.rank.order] = 1
            else:
                dic[card.rank.order] += 1
        
        sort_list = sorted(dic.items(), key=lambda d:d[1], reverse=True)
        order_lst = [item[0] for item in sort_list]
        times_lst = [item[1] for item in sort_list]
        return order_lst, times_lst

    # get the result of straight
    def __get_straight(self, lst):
        value = [0] * 6
        ordinary_straight_value = self.__get_ordinary_straight(lst)
        if ordinary_straight_value[0] != 0:
            value[0] = 5
            value[1] = ordinary_straight_value[1]
        special_straight_value = self.__get_special_straight(lst)
        if special_straight_value[0] != 0:
            value[0] = 5
            value[1] = special_straight_value[1]

        return value

    # if it is a ordinary straight
    def __get_ordinary_straight(self, lst):
        value = [0] * 6
        rank_list = [card.rank.order for card in lst]
        rank_list.sort()
        for i in range(len(rank_list) - 1):
            if rank_list[i] + 1 != rank_list[i+1]:
                return value
        value[0] = 5
        value[1] = rank_list[-1]
        return value

    # if it is a special straight
    def __get_special_straight(self, lst):
        value = [0] * 6
        rank_list = [card.rank.order for card in lst]
        for order in [2, 3, 4, 5, 14]:
            if order not in rank_list:
                return value
        value[0] = 5
        value[1] = 5
        return value

    # if it is a flush
    def __get_flush(self, lst):
        value = [0] * 6
        suit_list = [card.suit.name for card in lst]
        suit_set = set(suit_list)
        if len(suit_set) == 1:
            value[0] = 6
            rank_list = [item.rank.order for item in lst]
            rank_list.sort()
            rank_list.reverse()
            value[1:] = rank_list
        return value
   
    # get the result of three kind
    def __get_three_kind(self, lst):
        value = [0] * 6
        order_lst, time_lst = self.__get_order_times(lst)
        if time_lst[0] == 3:
            value[0] = 4
            value[1] = order_lst[0]
            tmp_order = order_lst[1:]
            tmp_order.sort()
            tmp_order.reverse()
            value[2] = tmp_order[0]
            value[3] = tmp_order[1]
        return value

    # get the result of two pair
    def __get_two_pair(self, lst):
        value = [0] * 6
        order_lst, time_lst = self.__get_order_times(lst)
        if time_lst[0] == 2 and time_lst[1] == 2:
            value[0] = 3
            tmp_order = order_lst[:2]
            tmp_order.sort()
            tmp_order.reverse()
            value[1] = tmp_order[0]
            value[2] = tmp_order[1]
            value[3] = order_lst[2]
        return value

    # get the result of pair
    def __get_pair(self, lst):
        value = [0] * 6
        order_lst, time_lst = self.__get_order_times(lst)
        if time_lst[0] == 2:
            value[0] = 2
            value[1] = order_lst[0]
            tmp_order = order_lst[1:]
            tmp_order.sort()
            tmp_order.reverse()
            value[2] = tmp_order[0]
            value[3] = tmp_order[1]
            value[4] = tmp_order[2]
        return value

    # get the result of high
    def __get_high(self, lst):
        value = [0] * 6
        order_lst, time_lst = self.__get_order_times(lst)
        value[0] = 1 
        order_lst.sort()
        order_lst.reverse()
        value[1] = order_lst[0]
        value[2] = order_lst[1]
        value[3] = order_lst[2]
        value[4] = order_lst[3]
        value[5] = order_lst[4]
        return value
    
    # print the hand
    def __str__(self):
        hand, value = self.__get_best_hand()     
        #return "%-15s " %self.hand_dict[value[0]] + " ".join([str(ca) for ca in hand])
        return self.hand_dict[value[0]]

    # compare with other
    def __lt__(self, other):
        hand, value = self.__get_best_hand()     
        o_hand, o_value = other.__get_best_hand()
        if value < o_value:
            return True
        return False

    # compare with other
    def __gt__(self, other):
        hand, value = self.__get_best_hand()     
        o_hand, o_value = other.__get_best_hand()
        if value > o_value:
            return True
        return False

    # compare with other
    def __eq__(self, other):
        hand, value = self.__get_best_hand()     
        o_hand, o_value = other.__get_best_hand()
        if value == o_value:
            return True
        return False
