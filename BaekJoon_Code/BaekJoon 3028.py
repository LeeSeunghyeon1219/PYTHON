## BaekJoon 3028 창영마을

import sys

str_val=sys.stdin.readline().strip()

ball=1

for val in str_val:
    if val=="A" and ball in [1,2]:
        ball=2 if ball==1 else 1
    elif val=="B" and ball in [2,3]:
        ball=3 if ball==2 else 2
    elif val=="C" and ball in [1,3]:
        ball=3 if ball==1 else 1
print(ball)
