import sys

i=int(sys.stdin.readline())
data=[]
for _ in range(i):
    data.append(int(sys.stdin.readline()))

data.sort(reverse=True)
for d in data:
    print(d,end=" ")