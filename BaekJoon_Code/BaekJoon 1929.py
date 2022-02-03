import sys

N,M=map(int,sys.stdin.readline().split())

for i in range(N,M+1):
    check=True
    for j in range(2,i):
        if i%j==0:
            check=False
            break
    if check==True:
        print(i,end="\n")