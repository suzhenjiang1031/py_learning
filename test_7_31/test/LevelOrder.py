class CircularSequenceQueue:
    def __init__(self):
        self.MaxQueueSize = 4
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    def InitQueue(self, Max):
        self.MaxQueueSize = Max
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    #元素入队
    def EnQueue(self, x):
        if (self.rear + 1) % self.MaxQueueSize != self.front:
            self.rear = (self.rear + 1) % self.MaxQueueSize
            self.s[self.rear] = x
        else:
            print("队列已满，无法入队")

    #元素出队
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空，无法出队")
            return
        else:
            self.front = (self.front + 1) % self.MaxQueueSize
            return self.s[self.front]

class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.lchild = None
        self.rchild = None

class BinaryTree(object):
    def CreateBinaryTree(self, root):
        data = input('->')
        if data == '#':
            root = None
        else:
            root.data = data
            root.lchild = BinaryTreeNode()
            self.CreateBinaryTree(root.lchild)
            root.rchild = BinaryTreeNode()
            self.CreateBinaryTree(root.rchild)

    def LevelOrder(self, root):
        tSequeceQueue = CircularSequenceQueue()
        tSequeceQueue.InitQueue(100)
        tSequeceQueue.EnQueue(root)
        tTreeNode = None
        while tSequeceQueue.IsEmptyQueue() == False:
            tTreeNode = tSequeceQueue.DeQueue()
            self.VisitBinaryTreeNode(tTreeNode)
            if tTreeNode.lchild is not None:
                tSequeceQueue.EnQueue(tTreeNode.lchild)
            if tTreeNode.rchild is not None:
                tSequeceQueue.EnQueue(tTreeNode.rchild)

    def VisitBinaryTreeNode(self, BinaryTreeNode):
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data, end = "")

    def PrintOut(self, root):
        bTN = BinaryTreeNode()
        print("创建一颗二叉树\n")
        print('                 A')
        print('                / \\')
        print('               B   E')
        print('              /   / \\')
        print('             C   D   F')
        print('A B C # # # E D # # F # #')
        print("请仿照上述序列，输入某一二叉树中各节点的值(#表示空结点)，每输入一个值按回车换行：")
        root.CreateBinaryTree(bTN)
        print("对二叉树进行层次遍历：")
        root.LevelOrder(bTN)

bT = BinaryTree()
bT.PrintOut(bT)