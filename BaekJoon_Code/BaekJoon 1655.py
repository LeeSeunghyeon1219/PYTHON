import sys
import heapq
N=int(sys.stdin.readline())

## min_heap: 오른쪽
left=[]
right=[]
for i in range(N):
    n=int(sys.stdin.readline())
    if len(left)==len(right):
        heapq.heappush(left,(-n,n))
    else:
        heapq.heappush(right,(n,n))

    # 왼쪽 첫번째 값이 오른쪽 첫번쨰 값보다 크면 바꾸기!
    if right and left[0][1]>right[0][1]:
        l_val=heapq.heappop(left)[1]
        r_val=heapq.heappop(right)[1]

        heapq.heappush(left,(-r_val,r_val))
        heapq.heappush(right,(l_val,l_val))

        # print("좌우바뀜")
    print(left[0][1])