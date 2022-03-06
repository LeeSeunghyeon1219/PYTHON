class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

## Tree 구현하기
root = Node('A')
node_2 = Node('B')
node_3 = Node('C')
root.left = node_2
root.right = node_3

node_4 = Node('D')
node_5 = Node('E')
node_2.left = node_4
node_2.right = node_5

node_6 = Node('F')
node_7 = Node('G')
node_3.left = node_4
node_3.right = node_5

def pre_order(node):
    if node == None:
        return

    print(f"{node.data}  ", end="")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(f"{node.data}  ", end="")
    in_order(node.right)

def post_order(node):
    if node == None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f"{node.data}  ", end="")