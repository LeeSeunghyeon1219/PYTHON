## BaekJoon 7568 덩치

import sys
N= int(sys.stdin.readline())
people=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result_list=[]
for i_w,i_h in people:
    count=1
    for j_w, j_h in people:
        if i_h<j_h and i_w<j_w:
            count+=1
    result_list.append(count)

for result in result_list:
    print(result,end=" ")