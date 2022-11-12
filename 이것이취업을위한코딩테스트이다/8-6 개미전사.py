import sys

N=int(sys.stdin.readline().rstrip())
K=list(map(int,sys.stdin.readline().split()))

dp=[0]*N

dp[0]=K[0]
dp[1]=max(K[0],K[1])
for i in range(2,N):
    dp[i]=max(dp[i-1],dp[i-2]+K[i])
print(dp)

