class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, data):
        self.root = Node(data)

    def find(self, data):
        self.find_data=[]
        if self.find_node_by_recursion(self.root, data) == False:
            return "검색한 Data가 없습니다."
        else:
            return "->".join(self.find_data)

    def find_node_by_recursion(self, current_node, data):
        if current_node == None:  ## 현재 Node가 존재하지 않는 경우(연결 x)
            return False
        self.find_data.append(str(current_node.data)) ## 현재 Node Data값 저장
        if data == current_node.data:  ## 찾는 Node가 맞는 경우
            return current_node

        ## 찾은 Node가 맞지 않는 경우
        if data < current_node.data:  ### 왼쪽 Node 탐색(찾는 Data<현재 Node Data)
            return self.find_node_by_recursion(current_node.left, data)
        if data > current_node.data:  ### 오른쪽 Node 탐색(찾은 Data>현재 Node Data)
            return self.find_node_by_recursion(current_node.right, data)

    def insert(self, data):
        if self.root == None:
            self.set_root(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, current_node, data):
        if data == current_node.data: ## Node에 이미 중복 값이 존재할 경우
            print("이미 {0}값이 존재합니다. 중복된 값은 삽입할 수 없습니다.".format(data))
            return
        if data < current_node.data: ## 삽입할 Data<현재 Node의 Data 인 경우
            if current_node.left == None: ## 왼쪽에 Data가 없으면 왼쪽에 삽입할 Data로 노드 생성
                current_node.left = Node(data)
            else:
                self.insert_node(current_node.left, data)
        elif data > current_node.data: ## 삽입할 Data>현재 Node의 Data 인 경우
            if current_node.right == None: ## 오른쪽에 Data가 없으면 왼쪽에 삽입할 Data로 노드 생성
                current_node.right = Node(data)
            else:
                self.insert_node(current_node.right, data)

    def get_next_node(self, node):
        ## 삭제할 Node의 right subtree의 최소값을 찾는다.
        ### 방법: right subtree에서 가장 왼쪽에 있는 ndoe를 찾으면 된다.
        while node.left != None:
            node = node.left
        return node

    def delete(self, data):
        if self.root == None:
            print("트리에 노드가 존재하지 않습니다.")
        else:
            self.delete_node(None, self.root, data)

    def delete_node(self, parent, current_node, data):
        if current_node == None: ## Node에 값이 존재하지 않는경우
            print("트리에 {0}가 존재하지 않습니다.".format(data))
            return

        if data < current_node.data: ## 삭제할 Data<현재 Node의 Data 인 경우
            self.delete_node(current_node, current_node.left, data)
        elif data > current_node.data: ## 삭제할 Data>현재 Node의 Data 인 경우
            self.delete_node(current_node, current_node.right, data)
        else: ## 삭제할 Node 찾을 때
            if current_node.left == None and current_node.right == None: ## 자식 Node가 없을 경우
                if data < parent.data: ## 부모의 왼쪽에 Node가 있는 경우
                    parent.left = None
                else:## 부모의 오른쪽에 Node가 있는 경우
                    parent.right = None
            elif current_node.left != None and current_node.right == None: ## 자식 Node가 1개 있을 경우 (left)
                if data < parent.data: ## 삭제할 Data<부모 node의 Data 이면 부모 node left에 자식 Node 연결
                    parent.left = current_node.left
                else: ## 삭제할 Data>부모 node의 Data 이면 부모 node right에 자식 Node 연결
                    parent.right = current_node.left
            elif current_node.left == None and current_node.right != None: ## 자식 Node가 1개 있을 경우 (right)
                if data < parent.data: ## 삭제할 Data<부모 node의 Data 이면 부모 node left에 자식 Node 연결
                    parent.left = current_node.right
                else: ## 삭제할 Data>부모 node의 Data 이면 부모 node right에 자식 Node 연결
                    parent.right = current_node.right

            elif current_node.left != None and current_node.right != None: ## 자식 Node가 2개 있을 경우
                ## 삭제할 Node의 right subtree의 최소값을 찾는다
                next_node = self.get_next_node(current_node.right)

                current_node.data = next_node.data ## 찾은 Node의 data 복제
                self.delete_node(current_node, current_node.right, next_node.data) ## 복제한 data가 들어있는 node를 삭제

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print("{0}  ".format(node.data), end="")
    in_order(node.right)

BST = BinarySearchTree()
BST.set_root(7)

BST.insert(3)
BST.insert(1)
BST.insert(5)
BST.insert(10)
BST.insert(8)

BST.insert(4)
BST.insert(12)
BST.insert(15)

print("5 검색결과:",BST.find(5))
print("11 검색결과:",BST.find(11))

in_order(BST.root)
print("")

BST.delete(10)
in_order(BST.root)
print("")
