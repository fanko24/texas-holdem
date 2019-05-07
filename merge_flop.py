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

if __name__ == "__main__":
    for number in range(6,10):
        win_dic = {}
        dic = {}
        fin = open("best_flop.%d" %number)
        fout = open("best_flop.%d.result" %number, "w")
        for line in fin:
            lst = line.strip().split()
            if len(lst) != 5:
                continue
            key = lst[0] + lst[1] + lst[2]
            hand_rank = lst[3]
            win_loss = lst[4]
            
            if key not in dic:
                dic[key] = {hand_rank:1}
            elif hand_rank not in dic[key]:
                dic[key][hand_rank] = 1
            else:
                dic[key][hand_rank] += 1
             
            if win_loss == "1":
                if key not in win_dic:
                    win_dic[key] = {hand_rank:1}
                elif hand_rank not in win_dic[key]:
                    win_dic[key][hand_rank] = 1
                else:
                    win_dic[key][hand_rank] += 1

        for key in dic:
            win_total = sum([win_dic[key][hand_rank] for hand_rank in win_dic[key]])
            win_list = sorted(win_dic[key].items(), key=lambda d:d[1], reverse=True)
            win_str = "||".join(["%s:%d:%.4f" %(item[0], item[1], 1.0*item[1]/win_total) for item in win_list])
            all_total = sum([dic[key][hand_rank] for hand_rank in dic[key]])
            all_list = sorted(dic[key].items(), key=lambda d:d[1], reverse=True)
            all_str = "||".join(["%s:%d:%.4f" %(item[0], item[1], 1.0*item[1]/all_total) for item in all_list])
            fout.write("%s\t%s\t%s\n" %(key, win_str, all_str))
        
        fin.close()
        fout.close()
