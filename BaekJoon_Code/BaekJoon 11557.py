import sys

i=int(sys.stdin.readline())
for _ in range(i):
    j = int(sys.stdin.readline())
    Val=""
    N=-9999
    for _ in range(j):
        val,n = sys.stdin.readline().split()
        if N<int(n):
            N=int(n)
            Val=val
    print(Val)
