## BaekJoon 1292 쉽게 푸는 문제

import sys
A, B = map(int, sys.stdin.readline().split())
data_list = []
num = 1
cnt = 0
result = 0
for i in range(B):
    cnt = cnt + 1
    if i + 1 >= A:
        result = result + num
    if cnt == num:
        num = num + 1
        cnt = 0
print(result)

