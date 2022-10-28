import sys

def binary_search(start, end,data,target):
    if start>end:
        return -1

    mid=(start+end)//2
    if data[mid]==target:
        return mid
    elif data[mid]>target: # 중간점보다 찾고자 하는 값이 작은 경우
        return binary_search(start,mid-1,data,target)
    elif data[mid]<target: # 중간점보다 찾고자 하는 값이 큰 경우
        return binary_search(mid+1,end,data, target)


n,t=map(int,sys.stdin.readline().split())
n=int(n)

data=list(map(int,sys.stdin.readline().split()))
data.sort()
print(binary_search(0,n-1,data,t))

