import sys

N,i = map(int,sys.stdin.readline().split())
d1=list(map(int,sys.stdin.readline().split()))
d2=list(map(int,sys.stdin.readline().split()))

d1=sorted(d1)
d2=sorted(d2,reverse=True)

for ii in range(i):
    if d1[ii]<d2[ii]:
        d1[ii],d2[ii]=d2[ii],d1[ii]
    else:
        break
print(sum(d1))