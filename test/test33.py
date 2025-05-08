import math

def dfs(i, cw, cp):
    global bestp, bestx, x, c, goods, n

    if i >= n:
        if cp > bestp:
            bestp = cp
            bestx = x[:]
        return

    # 计算当前节点的上界，如果不能超过当前最优值就剪枝
    if bound(i, cw, cp) <= bestp:
        return

    # 尝试选择第 i 个物品
    if cw + goods[i][1] <= c:
        x[i] = 1
        dfs(i + 1, cw + goods[i][1], cp + goods[i][2])

    # 尝试不选择第 i 个物品
    x[i] = 0
    dfs(i + 1, cw, cp)

# 上界函数：估计从第 i 个物品开始最多能得到多少价值
def bound(i, cw, cp):
    global goods, c, n
    cleft = c - cw
    b = cp
    while i < n and goods[i][1] <= cleft:
        cleft -= goods[i][1]
        b += goods[i][2]
        i += 1
    if i < n:
        b += goods[i][2] / goods[i][1] * cleft
    return b

# 主程序
if __name__ == '__main__':
    n = 5
    c = 10
    # [原始编号, 重量, 价值]
    goods = [[0, 2, 6], [1, 2, 3], [2, 6, 5], [3, 5, 4], [4, 4, 6]]
    # 按照性价比排序（贪心估计用）
    goods.sort(key=lambda x: x[2] / x[1], reverse=True)

    # 初始变量
    bestp = 0
    bestx = [0] * n  # 存储最优解的选择
    x = [0] * n      # 当前选择路径

    dfs(0, 0, 0)

    print("最大价值为：", bestp)
    # 恢复原始编号顺序输出结果
    answer = [0] * n
    for i in range(n):
        answer[goods[i][0]] = bestx[i]
    print("最优解为：", answer)
