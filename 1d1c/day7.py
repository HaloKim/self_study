# 1991
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    print(node.data, end='')
    if not node.left == '' : preorder(node.left)
    if not node.right == '' : preorder(node.right)
def inorder(node):
    if not node.left == '' : inorder(node.left)
    print(node.data, end='')
    if not node.right == '' : inorder(node.right)
def postorder(node):
    if not node.left == '' : postorder(node.left)
    if not node.right == '' : postorder(node.right)
    print(node.data, end='')

count = int(input())
tree = []
for i in range(count):
    x,y,z = input().split()
    node = Node(x)
    if y == '.':
        y = ''
    if z == '.':
        z = ''
    node.left = y
    node.right = z
    tree.append(node)

for i in range(count):
    for j in range(count):
        if tree[i].data == tree[j].left: 
            tree[j].left = tree[i]
        elif tree[i].data == tree[j].right: 
            tree[j].right = tree[i]
            
preorder(tree[0])
print()
inorder(tree[0])
print()
postorder(tree[0])