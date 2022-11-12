import sys

N,M=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

start=0
end=max(data)

result=0
while start<=end:
    total=0
    mid=(start+end)//2

    for d in data:
        if d>mid:
            total+=(d-mid)

    if total<M: # 더 많이 떡을 잘라야 한다!
        end=mid-1
    else:
        start=mid+1
        result=mid

print(result)

