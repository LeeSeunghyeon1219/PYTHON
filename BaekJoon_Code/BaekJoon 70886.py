import sys

i=int(sys.stdin.readline())

t=0
for _ in range(i):
    v = int(sys.stdin.readline())
    if v==1:
        t=t+1

if i-t<t:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
