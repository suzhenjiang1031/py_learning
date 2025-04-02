def max_diff_partition(n, arr):
    half_n = (n + 1) // 2
    total_sum = 0
    s1 = 0
    for i in range(n):
        total_sum += arr[i]
        if i < half_n:
            s1 += arr[i]
    return 2 * s1 - total_sum

n = int(input())
arr = list(map(int, input().split()))
print(max_diff_partition(n, arr))