## 미로탈출
import sys
from collections import deque
N,M =map(int, sys.stdin.readline().split())
graph= [ list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque([[x,y]])
    while queue:
        print(x,y)
        x,y=queue.popleft()
        for xx, yy in zip(dx,dy):
            moved_x=x+xx
            moved_y=y+yy
            if moved_x<=-1 or moved_x>=N or moved_y<=-1 or moved_y>=M:
                continue
            if graph[moved_x][moved_y]==0:
                continue

            if graph[moved_x][moved_y]==1: ## 방문 가능한 경우
                graph[moved_x][moved_y]=graph[x][y]+1
                queue.append([moved_x,moved_y])
bfs(0,0)
print(graph)
print(graph[N-1][M-1])
