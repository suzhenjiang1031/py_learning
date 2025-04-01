def max_diff_partition(n, arr):
    total_sum = sum(arr)
    target_size = n // 2
    
    dp = [[0] * (target_size + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, target_size) + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i-1])
    
    if n % 2 == 0:
        s1 = dp[n][target_size]
        s2 = total_sum - s1
        return abs(s1 - s2)
    else:
        s1_size1 = dp[n][target_size]  
        s2_size1 = total_sum - s1_size1
        diff1 = abs(s1_size1 - s2_size1)
        
        s1_size2 = dp[n][target_size + 1]          
        s2_size2 = total_sum - s1_size2

        diff2 = abs(s1_size2 - s2_size2)
        
        return max(diff1, diff2)

n = int(input())
arr = list(map(int, input().split()))

result = max_diff_partition(n, arr)
print(result)