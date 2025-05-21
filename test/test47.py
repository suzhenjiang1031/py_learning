def solve_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0]*(capacity+1)
    for i in range(n):
        for j in range(capacity, weights[i]-1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]

cases = [
    ([1,2,3], [6,10,12], 5),
    ([2,3,4,5], [3,4,5,6], 5),
    ([1,3,4], [15,20,30], 4),
]

for idx, (w, v, c) in enumerate(cases):
    print(f"案例 {idx+1}: 最大价值 = {solve_knapsack(w, v, c)}")
