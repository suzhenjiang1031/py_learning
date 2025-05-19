def knapsack_1d(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for j in range(capacity, weights[i]-1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]

weights = [2, 1, 3]
values = [12, 10, 20]
capacity = 5

print("最大价值（一维 DP）：", knapsack_1d(weights, values, capacity))
