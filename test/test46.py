def knapsack_with_path(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # 回溯路径
    w = capacity
    path = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            path.append(i-1)
            w -= weights[i-1]
    path.reverse()

    return dp[n][capacity], path

weights = [1, 3, 4, 5]
values = [15, 20, 30, 45]
capacity = 7

result, selected = knapsack_with_path(weights, values, capacity)
print("最大价值:", result)
print("选择物品索引:", selected)
