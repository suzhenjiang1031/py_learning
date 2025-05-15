if __name__ == "__main__":
    weight = [2, 1, 3, 2]
    value = [12, 10, 20, 15]
    capacity = 5

    # 方法1：动态规划
    print("动态规划解法：", knapsack_dp(weight, value, capacity))

    # 方法2：递归+备忘录
    memo = {}
    print("记忆化递归解法：", knapsack_dfs_memo(0, capacity, weight, value, memo))

    # 方法3：分支限界法 DFS
    global max_value
    max_value = 0
    best = [0]
    # 先按单位价值排序，提升剪枝效率
    items = sorted(zip(weight, value), key=lambda x: x[1] / x[0], reverse=True)
    sorted_weight, sorted_value = zip(*items)
    knapsack_branch_bound(0, 0, 0, capacity, sorted_weight, sorted_value, best)
    print("分支限界法解法：", max_value)
