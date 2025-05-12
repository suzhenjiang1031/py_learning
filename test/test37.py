from bisect import bisect_right
def meet_in_middle(capacity, goods):
    n = len(goods)
    half = n // 2

    def gen_subsets(arr):
        res = []
        for i in range(1 << len(arr)):
            w = v = 0
            for j in range(len(arr)):
                if i & (1 << j):
                    w += arr[j][1]
                    v += arr[j][2]
            if w <= capacity:
                res.append((w, v))
        return res

    left = gen_subsets(goods[:half])
    right = gen_subsets(goods[half:])

    right.sort()
    maxv = [0]
    for i in range(1, len(right)):
        maxv.append(max(maxv[-1], right[i][1]))

    ans = 0
    for lw, lv in left:
        remain = capacity - lw
        idx = bisect_right(right, (remain, float('inf'))) - 1
        if idx >= 0:
            ans = max(ans, lv + right[idx][1])
    return ans
