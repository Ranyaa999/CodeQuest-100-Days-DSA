class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Input: space-separated integers
nodes = list(map(int, input("Enter nodes: ").split()))

root = None
for key in nodes:
    root = insert(root, key)

print("In-order traversal:", end=' ')
inorder(root)
print()
