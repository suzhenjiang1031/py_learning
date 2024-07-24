class SequenceList(object):
    def __init__(self):
        self.SeqList = []

    def CreateSeqList(self):
        print("请输入元素用回车确认，若想结束则输入'#'")
        while True:
            num = input("请输入：")
            if num == '#':
                break
            try:
                num = int(num)
                self.SeqList.append(num)
            except:
                print("输入有误，请重新输入")
        print("顺序表创建完成")

    def DeleteDuplication(self):
        resultList = []
        for item in self.SeqList:
            if not item in resultList:
                resultList.append(item)
        for i in range(0,len(resultList)):
            print(f"删除重复元素的列表第{i + 1}个元素：{resultList[i]}")

    def TraverseSeqlist(self):
        for i in range(0,len(self.SeqList)):
            print(f"第{i + 1}个元素为{self.SeqList[i]}")

RT = SequenceList()
RT.CreateSeqList()
RT.TraverseSeqlist()
RT.DeleteDuplication()