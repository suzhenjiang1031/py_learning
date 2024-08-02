class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.lchild = None
        self.rchild = None

def CreateBinaryTree():
    data = input()
    if data == '#':
        root = None
    else:
        root = BinaryTreeNode()
        root.lchild = CreateBinaryTree()
        root.rchild = CreateBinaryTree()
        return root

def PreOrder(root):
    if root != None:
        print(root.data, end=" ")
        PreOrder(root.lchild)
        PreOrder(root.rchild)

def InOrder(root):
    if root != None:
        InOrder(root.lchild)
        print(root.data, end=" ")
        InOrder(root.rchild)

def PostOrder(root):
    if root != None:
        PreOrder(root.lchild)
        PreOrder(root.rchild)
        print(root.data, end=" ")

while True:
    try:
        root = CreateBinaryTree()
        PreOrder(root)
        print()
        InOrder(root)
        print()
        PreOrder(root)
        print()
    except:
        break