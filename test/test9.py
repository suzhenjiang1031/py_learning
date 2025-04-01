def max_diff(arr):
    arr.sort(reverse=True)   
    s1 = 0
    s2 = 0
    n1 = 0
    n2 = 0

    for num in arr:
        if n1 < n2:
            s1 += num
            n1 += 1
        elif n1 > n2:
            s2 += num
            n2 += 1
        else:  # n1 == n2
            if s1 <= s2:
                s1 += num
                n1 += 1
            else:
                s2 += num
                n2 += 1

    return abs(s1 - s2)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_diff(arr)
    print(result)