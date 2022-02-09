## BaekJoon 1929 - 소수구하기 (에라토스테네스의 체)
import sys

M,N=map(int,sys.stdin.readline().split())

check_list=[False,False] + [True]*(N-1)
for i in range(2,int((N+1)**0.5)+1):
    if check_list[i]==True:
        for j in range(2*i,N+1,i):
            check_list[j]=False


for j in range(M,N+1):
    if check_list[j]==True: print(j)
