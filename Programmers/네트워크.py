from collections import deque

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:  # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1  # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))

#### 유니온파인드
def FindRoot(parents,node):
    parentNode=parents[node]
    if parentNode!=node:
        return FindRoot(parents,parentNode)
    else:
        return parentNode
def UnionSet(parents,node1,node2):
    rootNode1=FindRoot(parents,node1)
    rootNode2=FindRoot(parents,node2)

    if rootNode1==rootNode2: ## 이미 묶임
        return
    else:
        parents[rootNode1]=rootNode2
        return

def CountRoot(parents,n): ## 루트 노드 갯수를 샌다
    roots=set()
    for i in range(n):
        roots.add(FindRoot(parents,i))
    return len(set(roots))

def solution1(n, computers):
    parents = [i for i in range(n)] ## 초기값은 자기 자신을 가지고 있는다!
    for node1 in range(n):
        for node2 in range(node1+1,n):
            print(node1,node2)
            if computers[node1][node2]: ## 연결되있다면 하나로 뭉치기!
                UnionSet(parents,node1,node2)
                print(parents)

    return CountRoot(parents,n)

print(solution1(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# solution1(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])