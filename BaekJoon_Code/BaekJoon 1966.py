## BaekJoon 1966 프린터 큐
from collections import deque
import sys

N=int(sys.stdin.readline())

for _ in range(N):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count=0
    while queue:
        max_val=max(queue)
        val=queue.popleft()
        m-=1
        if max_val==val:
            count+=1
            if m<0:
                print(count)
                break
        else:
            queue.append(val)
            if m<0: m=len(queue)-1


