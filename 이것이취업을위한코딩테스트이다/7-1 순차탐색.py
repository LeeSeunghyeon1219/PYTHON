import sys

def sequence_serach(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1
    return -1

n,t=sys.stdin.readline().split()
n=int(n)

data=list(sys.stdin.readline().split())
print(sequence_serach(n,t,data))
