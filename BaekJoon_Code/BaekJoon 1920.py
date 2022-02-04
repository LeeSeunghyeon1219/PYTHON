## BaekJoon 1920 수찾기

import sys
import collections
N=int(sys.stdin.readline())
data=sys.stdin.readline().split()
M=int(sys.stdin.readline())
data1=sys.stdin.readline().split()


card_dict=collections.Counter(data)

for val in data1:
    print(1) if val in card_dict else print(0)