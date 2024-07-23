class SequenceList(object):
    def __init__(self):
        self.SeqList = []

    def CreateSeqList(self):
        print("------------------------------------------------------")
        print("-------请输入需要逆序的数字，回车确认，如需结束请输入'#'-------")
        print("------------------------------------------------------")
        # Num = input("请输入数字: ")
        # while Num != '#':
        #     self.SeqList.append(Num)
        #     Num = input("请输入数字: ")
        while True:
            num = input("请输入数字:")
            if num == '#':
                break
            try:
                num = int(num)
                self.SeqList.append(num)
            except:
                print("请输入有效的数字:")
        print("顺序表建立完成")

    def TraverseElement(self):
        print("------------------顺序表中的元素------------------------")
        Seqlistlen = len(self.SeqList)
        for i in range(0,Seqlistlen):
            print("第",i+1,"个元素为",self.SeqList[i])

    def ReverseElement(self):
        SeqListlen = len(self.SeqList)
        i = 0
        j = SeqListlen - 1
        # for i in range(0, int(SeqListlen / 2)):
        #     flag = self.SeqList[i]
        #     self.SeqList[i] = self.SeqList[j]
        #     self.SeqList[j] = flag
        #     j = j - 1
        # while i < SeqListlen / 2:
        #     flag = self.SeqList[i]
        #     self.SeqList[i] = self.SeqList[j]
        #     self.SeqList[j] = flag
        #     i = i + 1
        #     j = j -1
        self.SeqList.reverse()

        print("------------------逆序后的顺序表-----------------------")
        for i in range(0,SeqListlen):
            print("第",i+1,"个元素为",self.SeqList[i])

RT = SequenceList()
RT.CreateSeqList()
RT.TraverseElement()
RT.ReverseElement()