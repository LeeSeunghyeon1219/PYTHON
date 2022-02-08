## BaekJoon 2108번 통계학

import sys
from collections import Counter

N= int(sys.stdin.readline())
data=[int(sys.stdin.readline()) for _ in range(N)]
data.sort()
### 1. 산술평균 구하기
print(round(sum(data)/N))
### 2. 중앙값 구하기
print(data[N//2])
### 3. 최빈값 구하기
cnt_data =Counter(data).most_common()
if len(cnt_data) > 1 and cnt_data[0][1]==cnt_data[1][1]: #최빈값 2개 이상
    print(cnt_data[1][0])
else:
    print(cnt_data[0][0])
### 4. 범위 출력
print(max(data)-min(data))