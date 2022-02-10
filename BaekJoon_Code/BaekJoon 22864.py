## BaekJoon 22864 피로도 - 그리디 알고리즘
import sys
A,B,C,M=map(int,sys.stdin.readline().split())

work=0
tired=0
for _ in range(24):
    if tired<0: tired=0
    if tired+A<=M: ## 일할 수 있음
        work+=B
        tired+=A
    else:## 일할 수 없음
        tired-=C
print(work)
