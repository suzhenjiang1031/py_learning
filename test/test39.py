def knapsack_dfs_memo(i, remaining, weight, value, memo):
    if i == len(weight):
        return 0
    if (i, remaining) in memo:
        return memo[(i, remaining)]
    
    # 不选
    res = knapsack_dfs_memo(i + 1, remaining, weight, value, memo)
    # 选
    if remaining >= weight[i]:
        res = max(res, knapsack_dfs_memo(i + 1, remaining - weight[i], weight, value, memo) + value[i])

    memo[(i, remaining)] = res
    return res
