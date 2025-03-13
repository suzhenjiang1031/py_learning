class BTNode():
    def __init__(self):
        self.data = "#"
        self.LeftChild = None
        self.RightChild = None

def getWidth(Root):
    if Root is None:
        return 0
    queue = []
    queue.append(Root)
    max_width = 0
    while queue:
        level_size = len(queue)
        max_width = max(max_width, level_size)
        for _ in range(level_size):
            node = queue.pop(0)
            if node.LeftChild:
                queue.append(node.LeftChild)
            if node.RightChild:
                queue.append(node.RightChild)
    return max_width

def CreateBinaryTree():
    data = input()
    if data == "#":
        Root = None
    else:
        Root = BTNode()
        Root.data = data
        Root.LeftChild = CreateBinaryTree()
        Root.RightChild = CreateBinaryTree()
    return Root

while True:
    try:
        ROOT = CreateBinaryTree()
        print(getWidth(ROOT))
    except:
        break