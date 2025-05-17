def knapsack_dp_trace(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # 回溯找出选择了哪些物品
    res = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            res.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], res[::-1]

val, items = knapsack_dp_trace(weights, values, capacity)
print("最大价值：", val)
print("选择的物品编号：", items)
