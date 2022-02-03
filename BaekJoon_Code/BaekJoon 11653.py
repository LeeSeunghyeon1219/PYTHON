## BaekJoon 11653 소인수분해

import sys

N=int(sys.stdin.readline())
while N!=1:
  for i in range(2,N+1):
    if N%i==0:
      print(i)
      N=N//i
      break