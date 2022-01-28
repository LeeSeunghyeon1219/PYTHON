## BaekJoon 10828 스택

import sys
N=int(sys.stdin.readline())
num_list=[]
for _ in range(N):
    str_val=sys.stdin.readline()
    if "push" in str_val:
        num_list.append(int(str_val[str_val.index(" "):]))
    elif "pop" in str_val:
        print(-1) if num_list==[] else print(num_list.pop())
    elif "size" in str_val:
        print(len(num_list))
    elif "empty" in str_val:
        print(1) if num_list==[] else print(0)
    elif "top" in str_val:
        print(-1) if num_list == [] else print(num_list[-1])
