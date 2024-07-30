class CircularSequenceQueue:
    def __init__(self):
        self.MaxQueueSize = 4
        self.s = [None for _ in range(self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    def InitQueue(self, Max):
        self.MaxQueueSize = Max
        self.s = [None for _ in range(self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    def IsEmptyQueue(self):
        return self.front == self.rear

    def EnQueue(self, x):
        if (self.rear + 1) % self.MaxQueueSize != self.front:
            self.rear = (self.rear + 1) % self.MaxQueueSize
            self.s[self.rear] = x
        else:
            print("队列已满，无法入队")

    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空，无法出队")
            return None
        else:
            self.front = (self.front + 1) % self.MaxQueueSize
            return self.s[self.front]


class BinaryTreeNode:
    def __init__(self, data='#'):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def CreateBinaryTree(self, Root):
        data = input('请输入节点数据 (或输入 # 表示为空节点): ')
        if data == '#':
            return None
        else:
            Root.data = data
            Root.lchild = self.CreateBinaryTree(BinaryTreeNode())
            Root.rchild = self.CreateBinaryTree(BinaryTreeNode())
            return Root

    def LevelOrder(self, Root):
        if Root is None:
            return

        tSequenceQueue = CircularSequenceQueue()
        tSequenceQueue.InitQueue(100)
        tSequenceQueue.EnQueue(Root)

        while not tSequenceQueue.IsEmptyQueue():
            tTreeNode = tSequenceQueue.DeQueue()
            if tTreeNode is not None:
                self.VisitBinaryTreeNode(tTreeNode)
                if tTreeNode.lchild is not None:
                    tSequenceQueue.EnQueue(tTreeNode.lchild)
                if tTreeNode.rchild is not None:
                    tSequenceQueue.EnQueue(tTreeNode.rchild)

    def VisitBinaryTreeNode(self, node):
        if node.data != '#':
            print(node.data, end=" ")

    def Print(self):
        root = BinaryTreeNode()
        self.CreateBinaryTree(root)
        self.LevelOrder(root)


bT = BinaryTree()
bT.Print()
