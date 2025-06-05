def find_major_element(arr):
    # Boyer-Moore 投票法找候选主元素
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    # 验证是否真的是主元素
    if candidate is not None:
        actual_count = arr.count(candidate)
        if actual_count > len(arr) // 2:
            return f"{candidate} {actual_count}"
    return "no exist"

try:
    while True:
        line = input()
        if line == '':
            break
        n = int(line)
        if n == 0:
            print("no exist")
            continue
        nums = list(map(int, input().split()))
        print(find_major_element(nums))
except EOFError:
    pass
