from functools import lru_cache

def count(k, n):
    """
    计算从1到n的页码中，数字k出现的总次数。
    
    参数:
        k (int): 要统计的数字 (0-9)
        n (int): 总页码数
    
    返回:
        int: 数字k的出现次数
    """
    s = str(n)
    len_s = len(s)
    
    @lru_cache(None)
    def dfs(pos, limit, leading):
        """
        递归函数，计算从pos位开始的k出现次数。
        
        参数:
            pos (int): 当前处理的位数
            limit (bool): 是否受n的限制
            leading (bool): 是否仍处于前导零状态
        
        返回:
            tuple: (count, num)，count是k的出现次数，num是有效数字个数
        """
        if pos == len_s:
            return (0, 0) if leading else (0, 1)
        
        up = int(s[pos]) if limit else 9
        ans_count = 0
        ans_num = 0
        
        for d in range(up + 1):
            if leading and d == 0:
                count_suffix, num_suffix = dfs(pos + 1, limit and d == int(s[pos]), True)
            else:
                count_suffix, num_suffix = dfs(pos + 1, limit and d == int(s[pos]), False)
                ans_count += (d == k) * num_suffix  # 当前位d==k时，贡献num_suffix次
            ans_count += count_suffix
            ans_num += num_suffix
        
        return (ans_count, ans_num)
    
    count_result, _ = dfs(0, True, True)
    return count_result

def statistically_digital(n):
    """
    统计从1到n的页码中，数字0到9分别出现的次数。
    
    参数:
        n (int): 总页码数
    
    返回:
        list: 包含10个整数，对应0到9的出现次数
    """
    return [count(k, n) for k in range(10)]