class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def CreateLinkedList(self):
        print("请输入数据后按回车确认，若想结束则输入'#'")
        cNode = self
        while True:
            Element = input("请输入当前结点的值：")
            if Element == '#':
                break
            try:
                nNode = Node(Element)
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
        if self.head == None:
            print("\n当前单链表为空！")
            return
        print("当前的单链表为：")
        cNode = self.head
        while cNode and cNode.next != None:
            print(cNode.data,"->",end = " ")
            cNode = cNode.next
        print(cNode.data)

#首端插入元素函数
    def InsertElementInhead(self):
        print("---首端插入元素---")
        Element = int(input("请输入待插入结点的值："))
        if Element == '#':
            return
        try:
            nNode = Node(int(Element))
            nNode.next = self.head
            self.head = nNode
        except:
            print("输入有误，重新输入")
        print("当前的单链表为：")
        cNode = self.head
        while cNode != None and cNode.next != None:
            print(cNode.data, "->", end = " ")
            cNode = cNode.next
        print(cNode.data)

    def InsertElementInTail(self):
        print("---尾部插入元素---")
        cNode = self.head
        Element = input("请输入待插入结点的值：")
        if Element == '#':
            return
        while cNode.next != None:
            cNode = cNode.next
        try:
            nNode = Node(int(Element))
            cNode.next = nNode
            cNode = self.head
        except:
            print("输入有误，重新输入")
        while cNode and cNode.next != None:
            print(cNode.data, "->", end = "")
            cNode = cNode.next
        print(cNode.data)

    # def InsertElement(self):
        # pos = 1
        # cNode = self.head
        # try:
        #     ipos = int(input("请输入要插入的位置："))
        #     while pos < (ipos - 1) and cNode.next != None:
        #         cNode = cNode.next
        #         pos = pos + 1
        #     Element = int(input("情输入要插入结点的值："))
        #     nNode = Node(Element)
        #     temp = cNode.next
        #     cNode.next = nNode
        #     nNode.next = temp
        # except:
        #     print("输入有误，重新输入")
        # cNode = self.head
        # while cNode and cNode.next != None:
        #     print(cNode.data, "->", end="")
        #     cNode = cNode.next
        # print(cNode.data)

    def InsertElement(self):
        print("---插入指定元素---")
        try:
            ipos = int(input("请输入要插入的位置："))
            if ipos <= 0:
                print("插入位置必须为正整数！")
                return
            Element = int(input("请输入要插入结点的值："))
            nNode = Node(Element)
            if ipos == 1:
                nNode.next = self.head
                self.head = nNode
            else:
                pos = 1
                cNode = self.head
                while pos < (ipos - 1) and cNode is not None:
                    cNode = cNode.next
                    pos += 1
                if cNode is None:
                    print("位置超出链表长度")
                    return
                nNode.next = cNode.next
                cNode.next = nNode
        except:
            print("输入有误，重新输入")
        self.TraverseElement()

    def DeleteElement(self):
        print("---删除指定元素位置---")
        try:
            ipos = int(input("请输入要删除的位置："))
            if ipos <= 0:
                print("删除位置必须为正整数")
                return
            if self.head is None:
                print("链表为空，无法删除")
                return
            if ipos == 1:
                self.head = self.head.next
            else:
                pos = 1
                cNode = self.head
                while pos < (ipos - 1) and cNode.next is not None:
                    cNode = cNode.next
                    pos += 1
                if cNode is None:
                    print("位置超出链表长度")
                    return
                cNode.next = cNode.next.next
        except:
            print("输入有误，重新输入")
        self.TraverseElement()

    def Delete(self):
        print("---删除指定元素---")
        try:
            Element = input("请输入要删除的结点元素：")
            if self.head is None:
                print("链表为空，无法删除")
                return
            if self.head.data == Element:
                self.head = self.head.next
                print("删除成功")
                self.TraverseElement()
                return
            cNode = self.head
            while cNode.next is not None:
                if cNode.next.data == Element:
                    cNode.next = cNode.next.next
                    print("删除成功")
                    self.TraverseElement()
                cNode = cNode.next
            if cNode.data == Element:
                cNode.next = None
        except:
            print(" ")



SSL = SingleLinkedList()
SSL.CreateLinkedList()
SSL.TraverseElement()
# SSL.InsertElementInhead()
# SSL.InsertElementInTail()
# SSL.InsertElement()
# SSL.DeleteElement()
SSL.Delete()

