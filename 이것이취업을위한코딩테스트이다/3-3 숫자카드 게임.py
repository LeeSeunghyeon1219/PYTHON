##  숫자카드 게임
### 여러개의 숫자카드 중 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
### 1. 숫자가 쓰인 카드들이 N*M 형태로 되어있음
### 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행 선택
### 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 선태
### 4. 처음 카드를골라낼 행을 선택할 때, 이후 해당 행에서 낮은 카드를 뽑을 것을 고려하여
###    최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함
import sys

N,M=map(int,sys.stdin.readline().split())
result=0
for _ in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    min_value=min(data)
    result=max(result,min_value)
print(result)
