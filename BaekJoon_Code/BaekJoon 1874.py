## BaekJoon 1874 스택 수열
import sys

N=int(sys.stdin.readline())
data_list=[int(sys.stdin.readline())for _ in range(N)]
result_list=[]
stack_list=[]
cnt=1
success_flag=True

for push_val in data_list:
  while cnt<=push_val:
    stack_list.append(cnt)
    cnt=cnt+1
    result_list.append("+")
  if stack_list[-1]==push_val:
    stack_list.pop()
    result_list.append("-")
  else:
    print("NO")
    success_flag=False
    break

if success_flag==True:
  for val in result_list:print(val)