## BaekJoon 1026 보물
import sys

N=int(sys.stdin.readline())
A_list=list(map(int,sys.stdin.readline().split()))
B_list=list(map(int,sys.stdin.readline().split()))

B_list=sorted(B_list,reverse=True)
A_list=sorted(A_list)

result=0
for A,B in zip(A_list,B_list):
    result+=A*B

print(result)