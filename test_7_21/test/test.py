class GetMaxFromN(object):
    def PrintOut(self):
        n = 10
        num = input(f"请输入{n}个整数，用空格分隔\n")
        num = num.split(" ")
        num_len = num.__len__()
        list = [0 for i in range(num_len + 1)]
        for i in range(0, num_len):
            list[i + 1] = int(num[i])
        for i in range(2,len(list)):
            list[0] = list[i]
            idx = i
            while(list[idx - 1] < list[0]):
                list[idx] = list[idx - 1]
                idx = idx -1
            list[idx] = list[0]
        print(f"最大值为{list[1]}")

GM = GetMaxFromN()
GM.PrintOut()