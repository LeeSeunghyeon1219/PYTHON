## 음료수 얼려 먹기
import sys
N,M =map(int, sys.stdin.readline().split())
graph= [ list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

ice_count=0

def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if graph[x][y]==0:
        graph[x][y]=True
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True: # 현재 위치에서 DFS 수행
            ice_count += 1
print(ice_count)