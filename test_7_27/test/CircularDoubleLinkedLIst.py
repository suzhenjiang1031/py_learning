class CircularDoubleLinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoubleLinkedList(object):
    def __init__(self):
        self.__head = None
        self.next = None
        self.prev = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cNode = self.__head
        while cNode.next != self.__head:
            count += 1
            cNode = cNode.next
        return count


    def CreateDoubleLinkedList(self):
        print("输入结点数值后按回车确认，若想结束则输入'#'。")
        cNode = self.__head
        while True:
            try:
                data = input("请输入结点值：")
                if data == '#':
                    break
                nNode = CircularDoubleLinkedNode(int(data))
                cNode.next = nNode
                nNode.prev = cNode
                nNode.next = self.__head
                cNode = cNode.next
            except:
                print("输入有误，重新输入")
        print("循环双链表创建完成！")

    def TraverseCircularDoubleLinkedListByNext(self):
        cNode = self.__head
        while cNode.next != self.__head:
            print(cNode.data, "->", end=" ")
            cNode = cNode.next
        print(cNode.data)

    def DeleteElement(self):
        print("---删除元素---")
        Element = input("请输入要删除的第一个结点值：")
        cNode = self.next
        pNode = self.prev
        while cNode.next != self.__head and cNode.data != int(Element):
            pNode = cNode
            cNode = cNode.next
        if cNode.data == int(Element):
            nNode = cNode.next
            pNode.next = nNode
            del cNode
        print(f"删除第一个值为{Element}的循环双链表为：")
        self.TraverseCircularDoubleLinkedListByNext()

    def Delete(self):
        print("删除所有值为奇数的结点")
        cNode = self.__head.next
        pNode = self.__head.prev
        while cNode.next != self.__head:
            if (cNode.data % 2) != 0:
                break

            else:
                cNode = cNode.next

        #     if (cNode.data % 2) != 0:
        #         nNode = cNode.next
        #         pNode.next = nNode
        #         del cNode
        #         cNode = nNode
        #     else:
        #         pNode = cNode
        #         cNode = cNode.next
        # if (cNode.data / 2) != 0:
        #     nNode = cNode.prev
        #     nNode.next = self
        #     del cNode
        print("删除所有值为奇数的结点后的循环双链表为：")
        self.TraverseCircularDoubleLinkedListByNext()



CDLL = CircularDoubleLinkedList()
CDLL.CreateDoubleLinkedList()
CDLL.TraverseCircularDoubleLinkedListByNext()
# CDLL.DeleteElement()
# CDLL.Delete()