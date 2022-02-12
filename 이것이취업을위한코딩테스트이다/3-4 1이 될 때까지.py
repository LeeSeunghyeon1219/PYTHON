## 1이 될 때까지
### 어떠한 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
### 1. N에서 1을 뺀다.
### 2. N을 K로 나눈다.(단, N이 K로 나누어 떨어짐)
### 이와같은 고ㅘ정을 수행해야 한느 최소 횟수를 구하시오
import sys
N,K=map(int,sys.stdin.readline().split())
count=0
while True:
    if N==1:
        break
    elif N%K==0:
       count+=1
       N //=K
    else:
        count += 1
        N-=1
print(count)