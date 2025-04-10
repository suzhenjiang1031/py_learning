def knapsack_01(n, C, weights, values):
    dp = [[0 for _ in range(C + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(C + 1):
            dp[i][j] = dp[i-1][j]
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j - weights[i-1]] + values[i-1])
                
    return dp[n][C]

def main():
    results = []
    
    while True:
        try:
            line = input().strip()
            if not line: 
                break
            n, C = map(int, line.split())
            
            weights = []
            values = []
            for _ in range(n):
                w, v = map(int, input().strip().split())
                weights.append(w)
                values.append(v)
            
            max_value = knapsack_01(n, C, weights, values)
            results.append(max_value)
            
        except EOFError:
            break
            
    for result in results:
        print(result)

if __name__ == "__main__":
    main()