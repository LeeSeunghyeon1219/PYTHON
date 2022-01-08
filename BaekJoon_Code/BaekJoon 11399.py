# BaekJoon 11399 ATM 최소시간 구하기
N=int(input())
P_list=list(map(int,input().split()))
P_list=sorted(P_list)
T=0
for i in range(len(P_list)):
    T=T+sum(P_list[:i+1])
print(T)