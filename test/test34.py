def knapsack_dp(capacity, goods):
    n = len(goods)
    dp = [0] * (capacity + 1)
    for i in range(n):
        weight = goods[i][1]
        value = goods[i][2]
        for j in range(capacity, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
    return dp[capacity]
