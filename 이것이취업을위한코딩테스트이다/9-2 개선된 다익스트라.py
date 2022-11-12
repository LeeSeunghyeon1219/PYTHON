import heapq
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a].append((b, c))


def dikstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            ## 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dikstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("IFINITY")
    else:
        print(distance[i])