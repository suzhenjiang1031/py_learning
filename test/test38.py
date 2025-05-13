def knapsack_dp(weight, value, capacity):
    n = len(weight)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填表
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + value[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
