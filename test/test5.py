def max_programs(n, L, lengths):
    # 对程序长度进行排序
    lengths.sort()
    count = 0  # 能存储的程序数
    total_length = 0  # 当前使用的磁带长度
    
    # 贪心选择：从小到大依次添加程序
    for length in lengths:
        if total_length + length <= L:
            total_length += length
            count += 1
        else:
            break
            
    return count

# 测试
n = 5
L = 10
lengths = [2, 3, 4, 5, 1]
result = max_programs(n, L, lengths)
print(f"最多可以存储的程序数: {result}")