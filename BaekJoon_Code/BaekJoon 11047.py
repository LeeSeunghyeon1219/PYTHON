## BaekJoon 11047 동전0
import sys

N,k=map(int,sys.stdin.readline().split())
coin_list=[]
for _ in range(N):
    coin_list.append(int(sys.stdin.readline().split()[0]))
coin_list.sort(reverse=True)
count=0

for coin in coin_list:
    if k==0: break
    c=k//coin
    count+=c
    k-=(coin*c)
print(count)
