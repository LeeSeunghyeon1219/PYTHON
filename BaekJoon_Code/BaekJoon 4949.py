## BaekJoon 4949 균형잡힌 세상

import re

while True:
    str_val=input()
    if str_val==".":
        break
    text = re.sub('[a-zA-Z0-9 .]','',str_val).strip()
    text_list=[]

    for text_val in text:
        if len(text_list)==0:
            text_list.append(text_val)
            continue
        if text_val=="(" or text_val=="[":
            text_list.append(text_val)
        else:
            check_val="(" if text_val==")" else "["
            text_list.pop() if text_list[-1]==check_val else text_list.append(text_val)
    if text_list==[]:
        print("yes")
    else:
        print("no")
