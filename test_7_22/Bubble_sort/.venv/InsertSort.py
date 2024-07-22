class SetOrder(object):
    def InsertSorb(self,lst):
        n = len(lst)
        if n <= 1:
            return lst
        for i in range(1,n):
            idx = i
            target = lst[i]
            while idx > 0 and lst[idx] < lst[idx - 1]:
                lst[idx] = lst[idx - 1]
                idx = idx - 1
            lst[idx] = target
        return lst

    def PrintOut(self):
        n = input("请输入需要排序的整数，用空格分隔 ")
        num = n.split(" ")
        arr = []
        for i in range(len(num)):
            arr.append(num[i])
        arr = self.InsertSorb(arr)
        print("排序完的序列为:")
        for i in arr:
            print(i, end = " ")

SO = SetOrder()
SO.PrintOut()
