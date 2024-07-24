class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def CreateLinkedList(self):
        print("请输入数字按回车确认，若想结束输入'#'。")
        cNode = self.head
        while True:
            num = input("请输入当前结点的值：")
            if num == '#':
                break
            try:
                nNode = Node(num)
                if self.head is None:
                    self.head = nNode
                    cNode = self.head
                else:
                    cNode.next = nNode
                    cNode = cNode.next
            except:
                print("输入有误，重新输入")
        print("单链表创建完成")

    def TraverseElement(self):
        if self.head is None:
            print("当前链表为空\n")
            return
        print("当前链表为：")
        cNode = self.head
        while cNode and cNode.next != None:
            print(cNode.data, "->", end = " ")
            cNode = cNode.next
        print(cNode.data)

SSL = SingleLinkedList()
SSL.CreateLinkedList()
SSL.TraverseElement()


