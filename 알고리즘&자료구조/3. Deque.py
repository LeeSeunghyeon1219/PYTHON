from collections import deque

deq = deque([3]) # 3이 있는 deque 생성
print(deq)
deq.appendleft(10)
deq.append(0)

print(deq)  # deque([10, 3, 0])
print(deq.popleft())
print(deq.pop())
print(deq)  # deque([5, 1, 2, 3, 4])


######### deque 회전 ###########
deq = deque([1, 2, 3, 4, 5])
print(deq)
deq.rotate(1)
print("오른쪽으로 회전:",deq) # deque([5, 1, 2, 3, 4])


deq.rotate(-1)
print("왼쪽으로 회전:",deq) # deque([1, 2, 3, 4, 5])
