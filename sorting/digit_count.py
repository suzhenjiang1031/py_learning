def count_digits(n):
    digit_count = {str(i): 0 for i in range(10)}

    for page in range(1, n + 1):
        for digit in str(page):
            digit_count[digit] += 1

    return digit_count

n = int(input("请输入你需要统计的页数："))
result = count_digits(n)
print(result)
