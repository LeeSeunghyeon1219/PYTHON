#1.탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
#2. 큐에 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
#3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.
from collections import deque

def bfs(graph,v, visited):
    need_visited=[v] ## 방문 예정인 곳
    visited[v]=True
    while need_visited:
        v=need_visited.pop(0)
        print(v, end=" ")
        for i in graph[v]:
            if visited[i]==False:
                need_visited.append(i)
                visited[i]=True

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
bfs(graph,1,visited)