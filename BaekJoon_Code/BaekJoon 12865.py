import sys
N,K=map(int,sys.stdin.readline().split(" "))

data=[[0,0]]
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split(" "))))
d=[[0 for _ in range(K+1)] for _ in range(N+1)]

## 모든 무게를 다 가져와야 한다.
for i in range(1,N+1): #### 물건 개수
    w = data[i][0]
    v = data[i][1]

    for j in range(1,K+1): #### 무게 개수
        if j<w: ## 현재 물건을 선택 안하는 경우 윗칸에서 가져옴
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j],d[i-1][j-w]+v)
            print(i,j,j-w)
print(d[-1][-1])

import sys

N, K = map(int, sys.stdin.readline().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])