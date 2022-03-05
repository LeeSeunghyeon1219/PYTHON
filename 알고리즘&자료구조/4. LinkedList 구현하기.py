# 노드 Class
class Node:
    def __init__(self, data, pointer=None):
        self.data = data
        self.next = pointer

# Linked List Class
# Class 객체 생성시, 데이터가 존재하지 않는노드를 생성. 해당 Node가 바로 Head
class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def get(self, idx): # idx 위치에 존재하는 노드를 받아온다.
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            node = self.head
            for _ in range(idx):
                node = node.next
            return node

    def append(self, data): # 데이터를 Linked List 종단점으로 추가한다.
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
        else:
            node = self.head
            while node.next != None:
                node = node.next

            new_node = Node(data)
            node.next = new_node
            self.size += 1

    def insert(self, value, idx): # 데이터를 idx 위치에 추가한다.
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
        elif idx == 0:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            node = self.get(idx - 1)
            if node == None:
                return
            new_node = Node(value)
            next_node = node.next
            node.next = new_node
            new_node.next = next_node
            self.size += 1

    def delete(self, idx): # idx 위치의 노드를 삭제한다.
        if self.size == 0:
            print("Empty Linked List")
            return
        elif idx >= self.size:
            print("Index Error")
            return
        elif idx == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            node = self.get(idx - 1)
            node.next = node.next.pointer
            self.size -= 1

    def print_linked_list(self):
        node = self.head
        while node:
            if node.next != None:
                print(node.data, "-> ", end="")
                node = node.next
            else:
                print(node.data)
                node = node.next