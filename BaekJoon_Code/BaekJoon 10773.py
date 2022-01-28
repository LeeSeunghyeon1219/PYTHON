## BaekJoon 10773 제로

import sys

N=int(sys.stdin.readline())
num_list=[]
for _ in range(N):
    num_val=int(sys.stdin.readline())
    if num_val==0 and num_list!=[]:
        num_list.pop()
    elif num_val!=0:
        num_list.append(num_val)
print(sum(num_list))
