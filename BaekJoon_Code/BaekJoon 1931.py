## BaekJoon 1931 회의실 배정 - 그리디 알고리즘
import sys

N=int(sys.stdin.readline())

time_list=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
## 주어진 시작시간과 끝나는 시간들을 이용해서 가장 많은 회의의 수를 알기 위해서는
## 빨리 끝나는 회의 순서대로 정렬을 해야 한다.
## 이유는 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다. 빨리 시작하는 순서대로
## 정렬을 우선시 한다면, 오히려 늦게 끝날 수 있기 때문이다.
## 먼저 시작시간을 오름차순으로 정렬한 뒤, 끝나는 시간을 기준으로 한번 더 정렬을 해야 한다.
time_list=sorted(time_list,key=lambda x:x[0])
time_list=sorted(time_list,key=lambda x:x[1])

last=0
count=0
for start,end in time_list:
    if start>=last:
        count+=1
        last=end
print(count)