## BaekJoon 10816 숫자카드 2

import sys
import collections
N = int(sys.stdin.readline())
card_list = sys.stdin.readline().split()
M = int(sys.stdin.readline())
find_card_list = sys.stdin.readline().split()

card_dict=collections.Counter(card_list)

for find_card in find_card_list:
    if find_card in card_dict:
        print(card_dict[find_card],end=" ")
    else:
        print(0,end=" ")
