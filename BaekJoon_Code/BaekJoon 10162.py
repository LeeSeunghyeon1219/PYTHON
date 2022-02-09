## BaekJoon 10162 전자레인지-그리디 알고리즘
import sys

time_list=[300, 60,10]
click_list=[0,0,0]
T=int(sys.stdin.readline())

for i in range(len(time_list)):
    count=T//time_list[i]
    T-=count*time_list[i]
    click_list[i]=count
    if T==0:
        break
print(-1) if T!=0 else print("{0} {1} {2}".format(click_list[0],click_list[1],click_list[2]))
