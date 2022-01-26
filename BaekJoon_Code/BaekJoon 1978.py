## BaekJoon 1978 소수찾기

N=int(input())
data=list(map(int,input().split()))
cnt=0
for num in data:
    check_val=True
    if num==1:
        continue
    for j in range(2,num):
        if num%j==0:
            check_val=False
            break
    if check_val==True:
        cnt+=1
print(cnt)