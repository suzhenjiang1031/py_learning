from functools import lru_cache

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

@lru_cache(None)
def dfs(i, remaining):
    if i == len(weights):
        return 0
    if weights[i] > remaining:
        return dfs(i+1, remaining)
    return max(dfs(i+1, remaining), dfs(i+1, remaining - weights[i]) + values[i])

print("最大价值（记忆化 DFS）:", dfs(0, capacity))
