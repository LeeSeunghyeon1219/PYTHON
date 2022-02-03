## BaekJoon 11866 요세푸스 문제 0

from collections import deque
import sys

N,k=map(int,sys.stdin.readline().split())

data_list=deque([ i for i in range(1,N+1)])
result_list=[]
while data_list:
  data_list.rotate(-(k-1))
  result_list.append(data_list.popleft())

print("<",end="")
for i in range(N):
  print("{0}, ".format(result_list[i]),end="") if i<N-1 else print("{0}>".format(result_list[i]))