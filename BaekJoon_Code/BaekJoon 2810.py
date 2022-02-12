## BaekJoon 2810 컵홀더

import sys
people=int(sys.stdin.readline())
seat=sys.stdin.readline()

result_val=seat.count("S")+seat.count("LL")+1
print(min(result_val,people))
