## BaekJoon 11650 좌표 정렬하기

import sys

N=int(sys.stdin.readline())
data_list=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

sort_data_list=sorted(data_list,key=lambda x:(x[0],x[1]))

for sort_data in sort_data_list:
    print(sort_data[0],sort_data[1])
    
