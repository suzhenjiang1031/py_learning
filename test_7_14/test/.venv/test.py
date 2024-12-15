# class Factorial(object):
#     def PrintOut(self, n=4):
#         fn = n
#         jc = 1
#         for i in range(1,fn+1):
#             jc = jc * i
#         print("4的阶乘为{0:}".format(jc))
#         print("时间空间复杂度为O(n)")
#
#
# FA = Factorial();
# FA.PrintOut();

# class Fibonacci(object):
#     def PrintOut(self):
#         a = 1
#         b = 2
#         for i in range(1,18):
#             c = a + b
#             a = b
#             b = c
#         print("第20项的值为{0:}".format(c))
#         print("时间空间复杂度为O(n)")
#
# FS = Fibonacci()
# FS.PrintOut()

# class FibonacciSum(object):
#     def PrintOut(self):
#         print("请输入数字:")
#         n = int(input())
#         jc = 1
#         sum = 0
#         for i in range(1, n + 1):
#             jc = jc * i
#             sum = sum + jc
#         print(f"1! + ... {n}! = {sum}")
#         print("时间空间复杂度为O(n)")
# FS = FibonacciSum()
# FS.PrintOut()

# class FibonacciDC(object):
#     def PrintOut(self):
#         print("请输入数字:")
#         n = int(input())
#         sum = 0
#         for i in range(1, n + 1):
#             jc = 1
#             for j in range(1, i + 1):
#                 jc = jc * j
#             sum = sum + jc
#         print(f"1! + ... + {n}! = {sum}")
#         print("时间空间复杂度为O(n的平方)")
#
# FS = FibonacciDC()
# FS.PrintOut()
#
# class GetMaxFromN(object):
#     def PrintOut(self):
#         n = 10
#         num = input(f"请输入{n}个整数，每个数字以空格分隔")
#         num = num.split()
#         len = num.__len__()
#         for i in range(0, len):
#             num[i] = int(num[i])
#         max = num[0]
#         for i in range(1, len):
#             if max < num[i]:
#                 max = num[i]
#         print(f"最大值为{max}")
# GM = GetMaxFromN()
# GM.PrintOut()

# class GetMaxFromN(object):
#     def PrintOut(self):
#         n = 10
#         num = input(f"请输入{n}个整数，用空格分隔\n")
#         num = num.split(" ")
#         num_len = num.__len__()
#         list = [0 for i in range(num_len + 1)]
#         for i in range(0, num_len):
#             list[i + 1] = int(num[i])
#         for i in range(2,len(list)):
#             list[0] = list[i]
#             idx = i
#             while(list[idx - 1] < list[0]):
#                 list[idx] = list[idx - 1]
#                 idx = idx -1
#             list[idx] = list[0]
#         print(f"最大值为{list[1]}")
#
# GM = GetMaxFromN()
# GM.PrintOut()

# from math import *
# class CompareValue(object):
#     def PrintOut(self):
#         n = 10
#         jc = 1
#         print(f"当n = {n}时:")
#         for i in range(1, n + 1):
#             print(f"log2 {i} = {log(i,2)}")
#             print(f"sqrt({i}) = {sqrt(2)}")
#             print(f"{i} = {i}")
#             print(f"{i}log2{i} = {i * log(i,2)}")
#             print(f"{i}² = {i ** 2}")
#             print(f"{i}三次方 = {i ** 3}")
#             print("power(2, i) = {2 ** i}")
#             jc = jc * i
#             print(f"{i}! = {jc}")
#
# GM = CompareValue()
# GM.PrintOut()

# class SetOrder(object):
#     def PrintOut(self):
#         temp = 0
#         num = input("请输入10个整数，中甲用空格分隔:")
#         num = num.split(" ")
#         len = num.__len__()
#         for i in range(len):
#             num = [int(x) for x in num]
#
#         for i in range(0,len - 1):
#             for j in range(0,len - 1 - i):
#                 if(num[j] > num[j + 1]):
#                     temp = num[j]
#                     num[j] = num[j + 1]
#                     num[j + 1] = temp
#         print("排序后的列表",num)
#
# GM = SetOrder()
# GM.PrintOut()

# class SetOrder(object):
#     def InsertSort(self,lst):
#         n = len(lst)
#         if n <= 1:
#             return lst
#         for i in range(1, n):
#             j = i
#             target = lst[i]
#
#             while j > 0 and target < lst[j - 1]:
#                 lst[j] = lst[j - 1]
#                 j = j - 1
#             lst[j] = target
#         return lst
#
#     def PrintOut(self):
#         n = 10
#         x = input("请输入10个整数(中间用空格分隔):")
#         x = x.split(" ")
#         arr = []
#         for i in x:
#             arr.append(int(i))
#         arr = self.InsertSort(arr)
#         print("数列按序排列如下: ")
#         for i in arr:
#             print(i, end = ' ')
#
# SO = SetOrder()
# SO.PrintOut

# class SequenceList(object):
#     def __init__(self):
#         self.SeqList = []
#
#     def CreateSequenceList(self):
#         print("----------------------------")
#         print("请输入数据后按回车键确认，若想结束输入请按'#'")
#         print("----------------------------")
#         Element = input("请输入元素: ")
#         while Element != '#':
#             self.SeqList.append(Element)
#             Element = input("请输入元素：")
#         print("顺序表SL创建完成")
#
#     def ReverseElement(self):
#         SeqListLen = len(self.SeqList)
#         i = 0
#         j = SeqListLen - 1
#         while i < SeqListLen / 2:
#             flag = self.SeqList[i]
#             self.SeqList[i] = self.SeqList[j]
#             self.SeqList[j] = flag
#             i = i + 1
#             j = j - 1
#         print("-------------转置后的顺序表--------------")
#
#         for i in range(0, SeqListLen):
#             print("第",i + 1,"个元素的值为",self.SeqList[i])
#
#
#     def TraverseElement(self):
#         SeqListLen = len(self.SeqList)
#         print("-------------遍历顺序表中的元素-----------")
#
#         for i in range(0, SeqListLen):
#             print("第",i + 1,"个元素的值为",self.SeqList[i])
#
# SL = SequenceList()
# SL.CreateSequenceList()
# SL.TraverseElement()
# SL.ReverseElement()

# class SequenceList(object):
#     def __init__(self):
#         self.SeqList = []
#
#     def CreateSeqList(self):
#         print("------------------------------------------------------")
#         print("-------请输入需要逆序的数字，回车确认，如需结束请输入'#'-------")
#         print("------------------------------------------------------")
#         # Num = input("请输入数字: ")
#         # while Num != '#':
#         #     self.SeqList.append(Num)
#         #     Num = input("请输入数字: ")
#         while True:
#             num = input("请输入数字:")
#             if num == '#':
#                 break
#             try:
#                 num = int(num)
#                 self.SeqList.append(num)
#             except:
#                 print("请输入有效的数字:")
#         print("顺序表建立完成")
#
#     def TraverseElement(self):
#         print("------------------顺序表中的元素------------------------")
#         Seqlistlen = len(self.SeqList)
#         for i in range(0,Seqlistlen):
#             print("第",i+1,"个元素为",self.SeqList[i])
#
#     def ReverseElement(self):
#         SeqListlen = len(self.SeqList)
#         i = 0
#         j = SeqListlen - 1
#         # for i in range(0, int(SeqListlen / 2)):
#         #     flag = self.SeqList[i]
#         #     self.SeqList[i] = self.SeqList[j]
#         #     self.SeqList[j] = flag
#         #     j = j - 1
#         # while i < SeqListlen / 2:
#         #     flag = self.SeqList[i]
#         #     self.SeqList[i] = self.SeqList[j]
#         #     self.SeqList[j] = flag
#         #     i = i + 1
#         #     j = j -1
#         self.SeqList.reverse()
#
#         print("------------------逆序后的顺序表-----------------------")
#         for i in range(0,SeqListlen):
#             print("第",i+1,"个元素为",self.SeqList[i])
#
# RT = SequenceList()
# RT.CreateSeqList()
# RT.TraverseElement()
# RT.ReverseElement()

# class SequenceList(object):
#     def __init__(self):
#         self.SeqList = []
#
#     def CreateSequenceList(self):
#         print("---------------------------------------")
#         print("---请输入数据后回车确认，若想结束请输入'#'---")
#         print("---------------------------------------")
#         while True:
#             num = input("请输入数字：")
#             if num == '#':
#                 break
#             try:
#                 num = int(num)
#                 self.SeqList.append(num)
#             except:
#                 print("请重新输入数字：")
#         print("顺序表创建完成")
#
#     def DeleteDuplication(self):
#         resultList = []
#         for item in self.SeqList:
#             if not item in resultList:
#                 resultList.append(item)
#         SeqListLen = len(resultList)
#         print("\n---删除重复的顺序表---")
#         for i in range(0, SeqListLen):
#             print(f"第{i + 1}个元素为{resultList[i]}")
#
#     def TraverseElement(self):
#         SeqListLen = len(self.SeqList)
#         print("---遍历顺序表中元素---")
#         for i in range(0, SeqListLen):
#             print(f"第{i + 1}个元素的值为{self.SeqList[i]}")
#
# SL = SequenceList()
# SL.CreateSequenceList()
# SL.TraverseElement()
# SL.DeleteDuplication()
#
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class SingleLinkedList(object):
#     def __init__(self):
#         self.next = None
#
#     def CreateSingleLinkedList(self):
#         print("请输入数据按回车确认，若想结束输入请按'#'。")
#         cNode = self
#         while True:
#             Element = input("请输入当前结点的值:")
#             if Element == '#':
#                 break
#             try:
#                 nNode = Node(int(Element))
#                 cNode.next = nNode
#                 cNode = cNode.next
#             except:
#                 print("输入有误，重新输入")
#         print("单链表创建完成！")
#
#     def TraverseElement(self):
#         cNode = self
#         if cNode.next == None:
#             print("\n当前链表为空！")
#             return
#         print("您当前的链表为：")
#         while cNode.next != None:
#             cNode = cNode.next
#             print(cNode.data,"->", end = "")
#         print("None")
#
# SSL = SingleLinkedList()
# SSL.CreateSingleLinkedList()
# SSL.TraverseElement()

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class SingleLinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def CreateLinkedList(self):
#         print("请输入数据后按回车确认，若想结束则输入'#'")
#         cNode = self
#         while True:
#             Element = input("请输入当前结点的值：")
#             if Element == '#':
#                 break
#             try:
#                 nNode = Node(Element)
#                 if self.head is None:
#                     self.head = nNode
#                     cNode = self.head
#                 else:
#                     cNode.next = nNode
#                     cNode = cNode.next
#             except:
#                 print("输入有误，重新输入")
#         print("单链表创建完成")
#
#     def TraverseElement(self):
#         if self.head == None:
#             print("\n当前单链表为空！")
#             return
#         print("当前的单链表为：")
#         cNode = self.head
#         while cNode:
#             print(cNode.data, "->", end=" ")
#             cNode = cNode.next
#         print("None")
#
#     def InsertElementInhead(self):
#         print("---首端插入元素---")
#         Element = input("请输入待插入结点的值：")
#         if Element == '#':
#             return
#         try:
#             nNode = Node(int(Element))
#             nNode.next = self.head
#             self.head = nNode
#         except:
#             print("输入有误，重新输入")
#         print("当前的单链表为：")
#         self.TraverseElement()
#
#     def InsertElementInTail(self):
#         print("---尾部插入元素---")
#         Element = input("请输入待插入结点的值：")
#         if Element == '#':
#             return
#         try:
#             nNode = Node(int(Element))
#             if self.head is None:
#                 self.head = nNode
#             else:
#                 cNode = self.head
#                 while cNode.next is not None:
#                     cNode = cNode.next
#                 cNode.next = nNode
#         except:
#             print("输入有误，重新输入")
#         print("当前的单链表为：")
#         self.TraverseElement()
#
#     def InsertElement(self):
#         print("---插入指定元素---")
#         try:
#             ipos = int(input("请输入要插入的位置："))
#             if ipos <= 0:
#                 print("插入位置必须为正整数！")
#                 return
#             Element = int(input("请输入要插入结点的值："))
#             nNode = Node(Element)
#             if ipos == 1:
#                 nNode.next = self.head
#                 self.head = nNode
#             else:
#                 pos = 1
#                 cNode = self.head
#                 while pos < (ipos - 1) and cNode is not None:
#                     cNode = cNode.next
#                     pos += 1
#                 if cNode is None:
#                     print("位置超出链表长度")
#                     return
#                 nNode.next = cNode.next
#                 cNode.next = nNode
#         except:
#             print("输入有误，重新输入")
#         print("当前单链表为：")
#         self.TraverseElement()
#
#     def DeleteElement(self):
#         print("---删除指定元素位置---")
#         try:
#             ipos = int(input("请输入要删除的位置："))
#             if ipos <= 0:
#                 print("删除位置必须为正整数")
#                 return
#             if self.head is None:
#                 print("链表为空，无法删除")
#                 return
#             if ipos == 1:
#                 self.head = self.head.next
#             else:
#                 pos = 1
#                 cNode = self.head
#                 while pos < (ipos - 1) and cNode.next is not None:
#                     cNode = cNode.next
#                     pos += 1
#                 if cNode is None or cNode.next is None:
#                     print("位置超出链表长度")
#                     return
#                 cNode.next = cNode.next.next
#         except:
#             print("输入有误，重新输入")
#         print("当前链表为：")
#         self.TraverseElement()
#
#     def Delete(self):
#         print("---删除指定元素---")
#         try:
#             Element = int(input("请输入要删除的结点元素："))
#             if self.head is None:
#                 print("链表为空，无法删除")
#                 return
#             if self.head.data == Element:
#                 self.head = self.head.next
#                 print("删除成功")
#                 self.TraverseElement()
#                 return
#             cNode = self.head
#             while cNode.next is not None:
#                 if cNode.next.data == Element:
#                     cNode.next = cNode.next.next
#                     print("删除成功")
#                     self.TraverseElement()
#                     return
#                 cNode = cNode.next
#             print("未查找到该元素！")
#         except:
#             print("输入有误，重新输入")
#         print("当前链表为：")
#         self.TraverseElement()

# SSL = SingleLinkedList()
# SSL.CreateLinkedList()
# SSL.TraverseElement()
# SSL.InsertElementInhead()
# SSL.InsertElementInTail()
# SSL.InsertElement()
# SSL.DeleteElement()
# SSL.Delete()

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class CircularSingleLinkedList(object):
#     def __init__(self):
#         self.next = None
#
#     def CreateCircularSingleLinkedList(self):
#         print("输入一个有序的循环单链表，输入数据后按回车确认，若想结束输入'#'")
#         cNode = self
#         while True:
#             try:
#                 data = input("请输入当前结点的值：")
#                 if data == '#':
#                     break
#                 nNode = Node(int(data))
#                 cNode.next = nNode
#                 nNode.next = self.next
#                 cNode = cNode.next
#             except:
#                 print("输入有误，重新输入")
#         print("循环单链表CSLL创建完成！")
#
#     def TraverseElement(self):
#         cNode = self.next
#         if cNode.next == None:
#             print("当前单链表为空！")
#             return
#         print("你当前的单链表为：")
#         while cNode.next != self.next:
#             print(cNode.data, "->", end = "")
#             cNode = cNode.next
#         print(cNode.data)
#
# CSLL = CircularSingleLinkedList()
# CSLL.CreateCircularSingleLinkedList()
# CSLL.TraverseElement()

# class DoubleLinkedNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class DoubleLinkedList(object):
#     def __init__(self):
#         self.next = None
#         self.prev = None
#
#     def CreateDoubleLinkedList(self):
#         print("请输入数据后按回车确认，若想结束则输入'#'。")
#         cNode = self
#         while True:
#             try:
#                 data = input("请输入当前结点的值：")
#                 if data == '#':
#                     break
#                 nNode = DoubleLinkedNode(int(data))
#                 cNode.next = nNode
#                 nNode.prve = cNode
#                 cNode = cNode.next
#             except:
#                 print("输入有误，重新输入")
#         print("双链表DDL创建完成！")
#
#     def TraverseDoubleLinkedListByNext(self):
#         cNode = self.next
#         print("您创建的双链表为：")
#         while cNode.next != None:
#             print(cNode.data, "->", end = " ")
#             cNode = cNode.next
#         print(cNode.data)
#
# DDL = DoubleLinkedList()
# DDL.CreateDoubleLinkedList()
# DDL.TraverseDoubleLinkedListByNext()
#
# class DoubleLinkedNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
# class DoubleLinkedList(object):
#     def __init__(self):
#         self.next = None
#         self.prev = None
#
#     def CreateDoubleLinkedList(self):
#         print("输入数据后按回车确认，若想结束则输入'#'。")
#         cNode = self
#         while True:
#             try:
#                 data = input("请输入当前结点的值：")
#                 if data == '#':
#                     break
#                 nNode = DoubleLinkedNode(int(data))
#                 cNode.next = nNode
#                 nNode.prev = cNode
#                 cNode = cNode.next
#             except:
#                 print("输入有误，重新输入")
#         print("单链表创建完成")
#
#     def TraverseDoubleLinkedListByNext(self):
#         cNode = self.next
#         print("当前创建的单链表为：")
#         while cNode.next != None:
#             print(cNode.data, "->", end = " ")
#             cNode = cNode.next
#         print(cNode.data)
#
#     def DeleteElement(self):
#         Element = input("请输入要删除的结点值：")
#         cNode = self.next
#         pNode = self
#         while cNode.data != None:
#             if cNode.data == int(Element):
#                 nNode = cNode.next
#                 pNode.next = nNode
#                 del cNode
#                 cNode = nNode
#             else:
#                 pNode = cNode
#                 cNode = cNode.next
#         if cNode.data == int(Element):
#             pNode.next = None
#             del cNode
#         print(f"成功删除值为{Element}的所有结点！")
#         cNode = self.next
#         self.TraverseDoubleLinkedListByNext()
#
# DDL = DoubleLinkedList()
# DDL.TraverseDoubleLinkedListByNext()
# DDL.DeleteElement()

