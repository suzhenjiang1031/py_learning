class SetOrder(object):
    def PrintOut(self):
        temp = 0
        num = input("请输入10个整数，中甲用空格分隔:")
        num = num.split(" ")
        len = num.__len__()
        for i in range(len):
            num = [int(x) for x in num]

        for i in range(0,len - 1):
            for j in range(0,len - 1 - i):
                if(num[j] > num[j + 1]):
                    temp = num[j]
                    num[j] = num[j + 1]
                    num[j + 1] = temp
        print("排序后的列表",num)

GM = SetOrder()
GM.PrintOut()