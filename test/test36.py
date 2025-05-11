def dfs_memo(i, cw, cp, memo):
    global goods, c, n
    if i == n:
        return cp
    if (i, cw) in memo:
        return memo[(i, cw)]

    res = dfs_memo(i + 1, cw, cp, memo)
    if cw + goods[i][1] <= c:
        res = max(res, dfs_memo(i + 1, cw + goods[i][1], cp + goods[i][2], memo))
    memo[(i, cw)] = res
    return res
