## BaekJoon 9012 괄호

import sys
N=int(sys.stdin.readline())
for _ in range(N):
    str_val=sys.stdin.readline()
    text_list=[]
    for text in str_val:
        text_list.append(text)
        if len(text_list)>=2 and text_list[-2:]==["(",")"]:
            text_list.pop()
            text_list.pop()
    if text_list==[]:
        print("YES")
    else:
        print("NO")
