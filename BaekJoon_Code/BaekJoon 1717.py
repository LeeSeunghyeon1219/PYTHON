import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def union(x,y):
    x = find(x)
    y = find(y)
    # 번호가 낮은 순서대로 트리의 상위 부모 노드로 위치하도록
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

n,m = map(int,input().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    c,a,b = map(int,input().split())
    if c:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a,b)
