## 인접 행렬 사용
INF = 999999999  # 무한

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

## 인접 그래프 사용

graph = [[] for _ in range(3)]  # [[], [], []]

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)  # [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]