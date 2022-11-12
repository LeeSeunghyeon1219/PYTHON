# LCA
import sys
sys.setrecursionlimit(int(1e5))
# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x,depth):
    c[x]=True
    d[x]=depth
    for y in graph[x]:
        if c[y]: # 이미 루트의 깊이를 구한경우
            continue
        parent[y]=x
        dfs(y,depth+1)

# A,B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    while d[a]!=d[b]: ## 높이가 불일치하는 경우 높이가 같아질때까지 반복
        if d[a]>d[b]: # 노드 타고 올라가기
            a=parent[a]
        else:
            b=parent[b]

    while a!=b: ## 부모노드가 같아질 때까지 반복
        a=parent[a]
        b=parent[b]
    return a

n=int(sys.stdin.readline())

parent=[0]*(n+1) # 부모노드정보
d=[0]*(n+1) # 각 노드 까지의 깊이
c=[0]*(n+1) # 각 노드 깊이가 계산되었는지 여부
graph=[[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)
dfs(1,0)
m=int(sys.stdin.readline())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))