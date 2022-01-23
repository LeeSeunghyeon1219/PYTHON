## 10250번 ACM 호텔

T = int(input())
data= [list(map(int,input().split())) for _ in range(T)]
for H,W,N in data:
    A=N%H
    B=int(N//H)+1
    if A==0:
        A=H
        B=B-1
    print(A*100+B)
