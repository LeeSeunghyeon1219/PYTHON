import sys
from collections import deque


n, m = map(int,sys.stdin.readline().split()) # n 과 m에 대한 입력을 받음

graph = [] # 2차원 list
for i in range(n): # n개의 rows에 대해서 map에 대한 정보를 얻음
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 너비 우선 탐색
def bfs(x,y): # BFS 선언, 입력으로 x와 y의 정보를 받음
    queue = deque() # queue 초기화
    queue.append((x,y)) # 초기 위치

    while queue:
        x, y = queue.popleft() # queue에서 꺼내기

        for i in range(4): # 4 방향에 대해서 이동 check

            nx = x+ dx[i] # 이동
            ny = y+ dy[i] # 이동

            if nx < 0 or ny < 0 or nx >=n or ny >= m: # 밖으로 넘어가는 경우,
                continue # continue
            if graph[nx][ny] == 0: # 이동 할 수 없는경우
                continue # continue

            if graph[nx][ny] == 1: # nx, ny에 처음으로 이동했을 때에,
                graph[nx][ny] = graph[x][y] + 1 # graph[x][y]는 최소의 거리를 저장, 1을 더한 값을 graph[nx][ny에 저장
                queue.append((nx,ny)) # 이동 된 nx, ny를 queue에 집어 넣기

    return graph[n-1][m-1] # 최종 n, m 위치에서의 graph 값 즉, 최소 거리를 반환함

print(bfs(0,0))

# DFS 사용, 런타임 에러 발생
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

visited = [[False] * m for _ in range(n)]

# N줄 만큼 입력
graph = [list(map(int, input().strip())) for _ in range(n)]

count = 1


def dfs(x, y):
    global count
    if 0 <= x < n and 0 <= y < m:
        # 우리가 찾는 조건이 되면 count를 UP!
        if visited[x][y] == False and graph[x][y] == 1:
            visited[x][y] = True
            count += 1

            dfs(x + graph[x][y], y)  # 오른쪽으로 이동
            dfs(x - graph[x][y], y)  # 왼쪽으로 이동
            dfs(x, y + graph[x][y])  # 아래로으로 이동
            dfs(x, y - graph[x][y])  # 위로으로 이동

            # 타겟한 위치에 도착하면 리턴!
            if x == n - 1 and y == m - 1:
                print(count)
                return
