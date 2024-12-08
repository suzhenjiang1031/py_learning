class BTNode():
    def __init__(self):
        self.data = "#"
        self.LeftChild = None
        self.RightChild = None

def CreateBinaryTree(depth,d,width):
    data = input()
    if data == "#":
        Root = None
    else:
        Root = BTNode()
        depth[d]+=1
        if depth[d]>width[0]:
            width[0]=depth[d]
        Root.data = data
        Root.LeftChild = CreateBinaryTree(depth,d+1,width)
        Root.RightChild = CreateBinaryTree(depth,d+1,width)
    return Root

while True:
    try:
        depth=[0]*100
        d=0
        width=[0]
        ROOT = CreateBinaryTree(depth,d,width)
        print(width[0])
        # LevelOrder(ROOT)
        # print(getWidth(ROOT))
    except:
        break