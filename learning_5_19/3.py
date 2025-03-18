class CircularSequenceQueue:
    #默认的初始化循环队列的函数
    def __init__(self):
        self.MaxQueueSize=4
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0
    #初始化循环队列的函数
    def InitQueue(self,Max):
        self.MaxQueueSize=Max
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0
    #判断循环队列是否为空的函数
    def IsEmptyQueue(self):
        if self.front==self.rear:
             iQueue=True
        else:
             iQueue=False
        return iQueue
    #元素入队的函数
    def EnQueue(self,x):
          if (self.rear+1)%self.MaxQueueSize!=self.front:
              self.rear=(self.rear+1)%self.MaxQueueSize
              self.s[self.rear]=x
          else:
            print("队列已满，无法入队")
            return
    #元素出队的函数
    def DeQueue(self):
        if self.IsEmptyQueue():
           print("队列为空，无法出队")
           return
        else:
            self.front=(self.front+1)%self.MaxQueueSize
            return self.s[self.front]
#类说明：定义一个二叉树的结点
class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.LeftChild  = None
        self.RightChild = None
#类说明：定义一个二叉树
class BinaryTree(object):
    #创建二叉树的函数
    def CreateBinaryTree(self, Root):
        data = input()
        if data == '#':
            Root = None
        else:
            Root.data = data
            Root.LeftChild = BinaryTreeNode()
            self.CreateBinaryTree(Root.LeftChild)
            Root.RightChild = BinaryTreeNode()
            self.CreateBinaryTree(Root.RightChild)
        return Root
    #层次遍历二叉树的函数
    def LevelOrder(self,Root):
        if Root == None:
            return
        tSequenceQueue = CircularSequenceQueue()
        tSequenceQueue.InitQueue(100)
        tSequenceQueue.EnQueue(Root)
        tTreeNode = None
        while tSequenceQueue.IsEmptyQueue() == False:
            tTreeNode = tSequenceQueue.DeQueue()
            self.VisitBinaryTreeNode(tTreeNode)
            if tTreeNode.LeftChild is not None:
                tSequenceQueue.EnQueue(tTreeNode.LeftChild)
            if tTreeNode.RightChild is not None:
                tSequenceQueue.EnQueue(tTreeNode.RightChild)
        print()
    #遍历二叉树的一个结点函数
    def VisitBinaryTreeNode(self, BinaryTreeNode):
        #值为#的结点代表空结点
        if BinaryTreeNode.data is not '#':
            print (BinaryTreeNode.data,end="")
while True:
    try:
        bTN = BinaryTreeNode()
        bT = BinaryTree()
        bTN=bT.CreateBinaryTree(bTN)
        bT.LevelOrder(bTN)
    except Exception:
        break