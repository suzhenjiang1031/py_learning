class DoubleLinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList(object):
    def __init__(self):
        self.next = None
        self.prev = None

    def CreateDoubleLinkedList(self):
        print("输入数据后按回车确认，若想结束则输入'#'。")
        cNode = self
        while True:
            try:
                data = input("请输入当前结点的值：")
                if data == '#':
                    break
                nNode = DoubleLinkedNode(int(data))
                cNode.next = nNode
                nNode.prev = cNode
                cNode = cNode.next
            except:
                print("输入有误，重新输入")
        print("双创建完成")

    def TraverseDoubleLinkedListByNext(self):
        cNode = self.next
        print("当前创建的双链表为：")
        while cNode.next != None:
            print(cNode.data, "->", end = " ")
            cNode = cNode.next
        print(cNode.data)

    def DeleteElement(self):
        print("---删除元素---")
        Element = input("请输入要删除的结点值：")
        cNode = self.next
        pNode = self.prev
        while cNode.next != None:
            if cNode.data == int(Element):
                nNode = cNode.next
                pNode.next = nNode
                del cNode
                cNode = nNode
            else:
                pNode = cNode
                cNode = cNode.next
        if cNode.data == int(Element):
            pNode.next = None
            del cNode
        print(f"成功删除值为{Element}的所有结点！")
        self.TraverseDoubleLinkedListByNext()


DDL = DoubleLinkedList()
DDL.CreateDoubleLinkedList()
DDL.TraverseDoubleLinkedListByNext()
DDL.DeleteElement()