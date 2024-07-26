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
        print("请输入数据后按回车确认，若想结束则输入'#'。")
        cNode = self
        while True:
            try:
                data = input("请输入当前结点的值：")
                if data == '#':
                    break
                nNode = DoubleLinkedNode(int(data))
                cNode.next = nNode
                nNode.prve = cNode
                cNode = cNode.next
            except:
                print("输入有误，重新输入")
        print("双链表DDL创建完成！")

    def TraverseDoubleLinkedListByNext(self):
        cNode = self.next
        print("您创建的双链表为：")
        while cNode.next != None:
            print(cNode.data, "->", end = " ")
            cNode = cNode.next
        print(cNode.data)

DDL = DoubleLinkedList()
DDL.CreateDoubleLinkedList()
DDL.TraverseDoubleLinkedListByNext()