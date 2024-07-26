#不带头结点的循环的单链表
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularSingleLinkedList(object):
    def __init__(self):
        self.next = None

    def CreateCircularSingleLinkedList(self):
        print("输入一个有序的循环单链表，输入数据后按回车确认，若想结束输入'#'")
        cNode = self
        while True:
            try:
                data = input("请输入当前结点的值：")
                if data == '#':
                    break
                nNode = Node(int(data))
                cNode.next = nNode
                nNode.next = self.next
                cNode = cNode.next
            except:
                print("输入有误，重新输入")
        print("循环单链表CSLL创建完成！")

    def TraverseElement(self):
        cNode = self.next
        if cNode.next == None:
            print("当前单链表为空！")
            return
        print("你当前的单链表为：")
        while cNode.next != self.next:
            print(cNode.data, "->", end="")
            cNode = cNode.next
        print(cNode.data, "->", end="")
        print(cNode.next.data)

CSLL = CircularSingleLinkedList()
CSLL.CreateCircularSingleLinkedList()
CSLL.TraverseElement()