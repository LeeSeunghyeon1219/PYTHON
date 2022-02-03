## BaekJoon 1765 듣보잡
import sys

N,M=map(int,sys.stdin.readline().split())

A_list=[sys.stdin.readline().strip() for _ in range(N)]
B_list=[sys.stdin.readline().strip() for _ in range(M)]

result_list=list(set(A_list).intersection(set(B_list))) ### 교집합 구하기

result_list.sort()
print(len(result_list))
for val in result_list:
    print(val)
