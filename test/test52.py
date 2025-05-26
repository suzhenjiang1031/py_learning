# 归并排序：分治经典例子
def merge_sort(arr):
    # 基本情况：一个元素直接返回
    if len(arr) <= 1:
        return arr

    # 1. 分：将数组分成两半
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # 对左边排序
    right = merge_sort(arr[mid:])  # 对右边排序

    # 2. 治：合并两个有序子数组
    return merge(left, right)

# 辅助函数：合并两个有序数组
def merge(left, right):
    result = []
    i = j = 0

    # 比较左右数组的元素，按顺序放入结果数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 剩下的元素直接加入（因为本身已排序）
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 测试用例
arr = [6, 3, 8, 5, 2, 7, 4, 1]
sorted_arr = merge_sort(arr)
print("排序前：", arr)
print("排序后：", sorted_arr)
