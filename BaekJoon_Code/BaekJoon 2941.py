## BaekJoon 2941 크로아티아 알파벳

import sys

str_val=sys.stdin.readline().strip()
croatia_alpha_list=['c=','c-','dz=','d-','lj','nj','s=','z=']

for croatia_alpha in croatia_alpha_list:
  count_num = str_val.count(str_val)
  if count_num!=0: str_val=str_val.replace(croatia_alpha,"_")
print(len(str_val))
