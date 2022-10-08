import sys

n=int(sys.stdin.readline())

A=100
B=100
for _ in range(n):
    n,m=map(int,sys.stdin.readline().split())
    if n==m:
        continue
    elif n<m:
        A=A-m
    else:
        B=B-n

print(A)
print(B)