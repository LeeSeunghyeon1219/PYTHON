import sys

i = int(sys.stdin.readline())

data=[]
for _ in range(i):
    d=sys.stdin.readline().split()
    data.append((d[0],int(d[1])))

data=sorted(data,key=lambda x: x[1])
for d in data:
    print(d[0])