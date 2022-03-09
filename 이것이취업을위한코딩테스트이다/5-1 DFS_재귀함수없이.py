## 재귀함수 사용하지 않고 dfs 구현하기
def dfs(graph,v, visited):
    need_visited=[v] ## 방문 예정인 곳
    while need_visited:
        v=need_visited.pop()
        if visited[v] ==False:
            visited[v]=True
            print(v, end=" ")
            need_visited.extend(sorted(graph[v],reverse=True))

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
dfs(graph,1,visited)