## BaekJoon 4344 평균은 넘겠지
import sys

N=int(sys.stdin.readline())
for i in range(N):
  data_list=list(map(int, sys.stdin.readline().split()))
  avg=sum(data_list[1:])/data_list[0]
  count=0
  for val in data_list[1:]:
    if val>avg: count+=1
  print("%.3f%%"% round(count/data_list[0]*100,3))
