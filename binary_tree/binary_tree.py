class BTNode():
    def __init__(self):
        self.data = '#'
        self.LeftChild = None
        self.RightChild = None

def PreOrder(Root):
    if Root != None:
        print(Root.data, end = '')
        PreOrder(Root.LeftChild)
        PreOrder(Root.RightChild)

def InOrder(Root):
    if Root != None:
        InOrder(Root.LeftChild)
        print(Root.data, end = '')
        InOrder(Root.RightChild)

def PostOrder(Root):
    if Root != None:
        PostOrder(Root.LeftChild)
        PostOrder(Root.RightChild)
        print(Root.data, end = '')

def CreatBinaryTree():
    data = input()
    if data == '#':
        Root = None
    else:
        Root = BTNode()
        Root.data = data
        Root.LeftChild = CreatBinaryTree()
        Root.RightChild = CreatBinaryTree()
    return Root

while True:
    try:
        ROOT = CreatBinaryTree()
        PostOrder(ROOT)
        print()
        InOrder(ROOT)
        print()
        PostOrder(ROOT)
        print()

    except:
        break