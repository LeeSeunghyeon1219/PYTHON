def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]

    costs.sort(key=lambda x: x[2])
    print(costs)

    def Find(node):
        parent_node = parent[node]

        if parent_node != node:
            return Find(parent_node)
        else:
            return parent_node

    def union(node1, node2):
        xx = Find(node1)
        yy = Find(node2)

        if xx > yy:
            parent[xx] = yy
        else:
            parent[yy] = xx

    def check_node(node1, node2):
        xx = Find(node1)
        yy = Find(node2)

        if xx == yy:  ## 연결되있음
            return False
        return True

    for x, y, w in costs:
        if check_node(x, y):
            union(x, y)
            answer += w

    return answer