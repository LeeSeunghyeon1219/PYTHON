## BaekJoon_Code 10866 덱

import sys
N=int(sys.stdin.readline())
num_list=[]
for _ in range(N):
    str_val=(sys.stdin.readline())
    if "push_front " in str_val:
        num_list=[int(str_val[str_val.index(" "):])]+num_list
    elif "push_back " in str_val:
        num_list.append(int(str_val[str_val.index(" "):]))
    elif "pop_front" in str_val:
        print(-1) if num_list==[] else print(num_list.pop(0))
    elif "pop_back" in str_val:
        print(-1) if num_list==[] else print(num_list.pop())
    elif "size" in str_val:
        print(len(num_list))
    elif "empty" in str_val:
        print(1) if num_list==[] else print(0)
    elif "front" in str_val:
        print(-1) if num_list == [] else print(num_list[0])
    elif "back" in str_val:
        print(-1) if num_list == [] else print(num_list[-1])
