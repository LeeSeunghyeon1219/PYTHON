# LCA 2번
import sys
sys.setrecursionlimit(100000)
LOG=21 # 2^20=10000000 제한 줌

n=int(sys.stdin.readline())
parent=[[0]*LOG for _ in range(n+1)] # 부모
d=[0]*(n+1) # 깊이
c=[0]*(n+1) # 방문
graph=[[] for _ in range(n+1)] # 그래프

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    c[x]=True
    d[x]=depth
    for y in graph[x]:
        if c[y]: # 이미 루트의 깊이를 구한경우
            continue
        parent[y][0]=x
        dfs(y,depth+1)


# 모든 노드의 전체 부모 관계 갱신
def set_parent():
    dfs(1,0)
    ## 나머지 정보에 대한 PARENT 저장하기!
    for i in range(1,LOG):
        for j in range(1,n+1):
            parent[j][i]=parent[parent[j][i - 1]][i - 1]
            if parent[j][i]==0:
                break

def lca(a,b):
    if d[a]>d[b]:# b가 더 깊도록 설정하기
        a,b=b,a

    # 깊이 동일하도록 설정하기
    for i in range(LOG-1,-1,-1):
        if d[b]-d[a]>=2**i:
            b=parent[b][i]

    if a==b:
        return a

    # 올라가면서 공통조상 찾기
    for i in range(LOG-1,-1,-1):
        if parent[a][i]!=parent[b][i]:
            a=parent[a][i]
            b=parent[b][i]

    return parent[a][0]

set_parent()
m = int(sys.stdin.readline())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))