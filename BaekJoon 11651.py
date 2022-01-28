## BaekJoon 11651 좌표정렬하기2

import sys

N=int(sys.stdin.readline())
data_list=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sort_data_list=sorted(data_list,key=lambda x:(x[1], x[0]))

for sort_data in sort_data_list:
    print(sort_data[0],sort_data[1])
