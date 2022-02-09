## BaekJoon 2720 세탁기 사장 동혁 - 그리디 알고리즘
import sys

N=int(sys.stdin.readline())
coin_list=[25,10,5,1]
for _ in range(N):
    result_list=[0,0,0,0]
    C=int(sys.stdin.readline())
    for i in range(len(coin_list)):
        count=C//coin_list[i]
        result_list[i]=count
        C-=count*coin_list[i]
    print("{0} {1} {2} {3}".format(result_list[0],result_list[1],result_list[2],result_list[3]))