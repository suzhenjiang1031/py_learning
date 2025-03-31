def max_diff_partition(n, arr):
    arr.sort(reverse=True) 
    sum1, sum2 = 0, 0
    count1, count2 = 0, 0

    for num in arr:
        if count1 <= count2:
            sum1 += num
            count1 += 1
        else:
            sum2 += num
            count2 += 1

    return abs(sum1 - sum2)

n = int(input())
arr = list(map(int, input().split()))

print(max_diff_partition(n, arr))
