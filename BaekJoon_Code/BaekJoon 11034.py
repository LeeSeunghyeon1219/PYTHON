## BaekJoon 11034 캥거루 세마리2

import sys
while True:
    try:
        A, B, C = map(int, sys.stdin.readline().split())
        print(max(B-A, C-B)-1)
    except:
        break