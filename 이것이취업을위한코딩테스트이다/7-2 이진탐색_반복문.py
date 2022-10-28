import sys

def binary_search(start, end,data,target):
    while start<=end:
        mid=(start+end)//2

        if data[mid]==target:
            return mid
        elif data[mid]>target:
            end=mid-1
        elif data[mid]<target:
            start=mid+1
    return -1


n,t=map(int,sys.stdin.readline().split())
n=int(n)

data=list(map(int,sys.stdin.readline().split()))
data.sort()
print(binary_search(0,n-1,data,t))

