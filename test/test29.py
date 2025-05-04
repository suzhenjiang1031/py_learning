try:
    a = int(input("请输入分子："))
    b = int(input("请输入分母："))
    print("结果是：", a / b)
except ZeroDivisionError:
    print("错误：分母不能为 0")
except ValueError:
    print("输入必须是数字")
