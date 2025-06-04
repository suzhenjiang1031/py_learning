import sys

def solve(case_iter):
    """逐个测试用例处理，返回每个用例的最大期待值"""
    results = []
    while True:
        try:
            Q = int(next(case_iter))          # 预算
            M = int(next(case_iter))          # 物品数量
        except StopIteration:                 # 文件读完
            break

        prices  = [int(next(case_iter)) for _ in range(M)]
        values  = [int(next(case_iter)) for _ in range(M)]

        # 一维 0-1 背包：dp[c] 表示花费 ≤ c 时能得到的最大期待值
        dp = [0]*(Q + 1)
        for cost, val in zip(prices, values):
            # 逆序遍历保证每件物品至多选一次
            for c in range(Q, cost - 1, -1):
                dp[c] = max(dp[c], dp[c - cost] + val)

        results.append(str(dp[Q]))
    return results


def main() -> None:
    data = sys.stdin.read().strip().split()
    answers = solve(iter(data))
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
