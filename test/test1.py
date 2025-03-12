def max_program(n,L,lengths):
    dp = [0] * (L + 1)

    for i in range(n):
        program_len = lengths[i]
        
        for j in range(L,program_len-1,-1):
            dp[j] = max(dp[j], dp[j-program_len] + 1)
    return max(dp)

if __name__ == '__main__':
    n = 5
    L = 10
    lengths = [4, 2, 4, 6, 3]

    result = max_program(n, L, lengths)
    print(f"最多可以存储{result}个程序")

