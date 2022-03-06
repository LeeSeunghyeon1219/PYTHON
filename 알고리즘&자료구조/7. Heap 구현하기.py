MAX_HEAP_SIZE = 101


class Heap:
    def __init__(self):
        self.heap = [None] * MAX_HEAP_SIZE
        self.heap_count = 0

    def compare_with_parent(self, index):
        if index <= 1:
            return False
        parent_index = index // 2 ## 부모 Node 계산
        if self.heap[index] < self.heap[parent_index]:  ## 부모 Node 값>자식 Node 값이면 SWAP
            return True
        else:
            return False

    ## Heap에 Data 삽입하기
    def insert(self, data):
        self.heap_count += 1
        if self.heap_count == 1: ## Root Node일 경우
            self.heap[self.heap_count] = data
            return

        self.heap[self.heap_count] = data
        insert_index = self.heap_count

        while self.compare_with_parent(insert_index): ## 부모 Node 값과 자식 Node 값 비교
            parent = insert_index // 2
            ## 부모 node 값>자식 node 값 이면 두 값을 변경
            val=self.heap[insert_index]
            self.heap[insert_index]=self.heap[parent]
            self.heap[parent]=val
            insert_index = parent ## 변경한 Node를 다시 비교함
        return True

    def compare_with_child(self, index):
        left = 2 * index
        right = 2 * index + 1

        ## 현재 Heap의 왼쪽과 오른쪽에 연결된 node가 없는 경우
        if self.heap[left] == None and self.heap[right] == None:
            return False

        ## heap의 왼쪽에 연결된 Node가 있는 경우
        if self.heap[right] == None:
            if self.heap[left] < self.heap[index]: ## 현재 Node 값>왼쪽 Node의 값이면
                return left
            else:
                return False
        ## heap의 왼쪽가 오른쪽에 연결된 Node가 있는 경우
        if self.heap[left] < self.heap[right]: ## heap의 왼쪽 값<오른쪽 값이면
            return left
        else:
            return right

    def pop(self):
        index = 1
        root = self.heap[1] ## Root의 값을 추출한다.

        ## 맨 마지막 Heap data를 Root로 옮긴다.
        terminal_data = self.heap[self.heap_count]
        self.heap[self.heap_count] = None
        self.heap[index] = terminal_data
        self.heap_count -= 1

        while True:
            child_index = self.compare_with_child(index)
            if not child_index:
                break
            ## child node 값<현재 node 값 이면 두 값을 변경
            val = self.heap[child_index]
            self.heap[child_index] = self.heap[index]
            self.heap[index]= val
            index = child_index

        return root

heap = Heap()
heap.insert(1)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(9)
heap.insert(10)
heap.insert(11)
heap.insert(2)

print(heap.heap)
heap.pop()
print(heap.heap)
