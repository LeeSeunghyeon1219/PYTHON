## BaekJoon 거스름돈 - 그리디 알고리즘
import sys

money=1000-int(sys.stdin.readline())

coin_count=0
coin_list=[500,100,50,10,5,1]

for coin in coin_list:
    count=money//coin
    money-=count*coin
    coin_count+=count
print(coin_count)