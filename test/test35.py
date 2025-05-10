def backtrack(i, cw, cp):
    global bestp, c, goods, n
    if i == n:
        if cp > bestp:
            bestp = cp
        return
    if cw + goods[i][1] <= c:
        backtrack(i + 1, cw + goods[i][1], cp + goods[i][2])  # 选
    backtrack(i + 1, cw, cp)  # 不选
