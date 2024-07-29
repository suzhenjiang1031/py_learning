def digui(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return digui(n - 1) + digui(n - 2)

n = int(input("请输入需要测试的台阶数："))
result = digui(n)
print(f"{n}个台阶共有{result}个走法")