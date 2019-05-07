# -*- coding: utf-8 -*-

import sys

rank_dict = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }

def get_key(c1, c2):
    key = None
    if c1[0] == c2[0]:
        if rank_dict[c1[1:]] > rank_dict[c2[1:]]:
            key = ("^"+c1[1:]+"^"+c2[1:]).encode("utf-8")
        else:
            key = ("^"+c2[1:]+"^"+c1[1:]).encode("utf-8")
    else: 
        if rank_dict[c1[1:]] > rank_dict[c2[1:]]:
            key = ("*"+c1[1:]+"^"+c2[1:]).encode("utf-8")
        else:
            key = ("*"+c2[1:]+"^"+c1[1:]).encode("utf-8")
    return key, c1+c2

if __name__ == "__main__":
    for number in range(6,10):
        win_dic = {}
        dic = {}
        fin = open("best_hole.%d" %number)
        fwin = open("best_hole.%d.winner" %number, "w")
        fall = open("best_hole.%d.all" %number, "w")
        hands = 0
        for line in fin:
            lst = line.strip().split()
            if len(lst) != 4:
                continue
            key, card = get_key(lst[0].decode("utf-8"), lst[1].decode("utf-8"))
            hand_rank = lst[2]
            win_loss = lst[3]
            
            if key not in dic:
                dic[key] = {card:{hand_rank:1}}
            elif card not in dic[key]:
                dic[key][card] = {hand_rank:1}
            elif hand_rank not in dic[key][card]:
                dic[key][card][hand_rank] = 1
            else:
                dic[key][card][hand_rank] += 1
             
            if win_loss == "1":
                if key not in win_dic:
                    win_dic[key] = {card:{hand_rank:1}}
                elif card not in win_dic[key]:
                    win_dic[key][card] = {hand_rank:1}
                elif hand_rank not in win_dic[key][card]:
                    win_dic[key][card][hand_rank] = 1
                else:
                    win_dic[key][card][hand_rank] += 1
                hands += 1
        ranks = sum([len(win_dic[key]) for key in win_dic])

        for key in dic:
            total = sum([dic[key][card][hand_rank] for card in dic[key] for hand_rank in dic[key][card]])
            length = len(dic[key])
            temp_dict = {}
            for card in dic[key]:
                for hand_rank in dic[key][card]:
                    if hand_rank not in temp_dict:
                        temp_dict[hand_rank] = dic[key][card][hand_rank]
                    else:
                        temp_dict[hand_rank] += dic[key][card][hand_rank]
            temp_list = sorted(temp_dict.items(), key=lambda d:d[1], reverse=True)
            temp_str = "||".join(["%s:%d:%.4f" %(item[0], item[1], 1.0*item[1]/total) for item in temp_list])
            fall.write("%s\t%d\t%d\t%lf\t%s\n" %(key.encode("utf-8"), total, length, 1.0*total/length, temp_str))
        
        for key in win_dic:
            total = sum([win_dic[key][card][hand_rank] for card in win_dic[key] for hand_rank in win_dic[key][card]])
            length = len(win_dic[key])
            temp_dict = {}
            for card in win_dic[key]:
                for hand_rank in win_dic[key][card]:
                    if hand_rank not in temp_dict:
                        temp_dict[hand_rank] = win_dic[key][card][hand_rank]
                    else:
                        temp_dict[hand_rank] += win_dic[key][card][hand_rank]
            temp_list = sorted(temp_dict.items(), key=lambda d:d[1], reverse=True)
            temp_str = "||".join(["%s:%d:%.4f" %(item[0], item[1], 1.0*item[1]/total) for item in temp_list])
            fwin.write("%s\t%d\t%d\t%.1f\t%.3f\t%s\n" %(key.encode("utf-8"), total, length, 1.0*total/length, (1.0*total/length)/(1.0*hands/ranks), temp_str))
        
        fin.close()
        fwin.close()
        fall.close()
