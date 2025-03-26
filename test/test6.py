def min_avg_waiting_time(n, s, times):
    # 对服务时间排序
    times.sort()
    
    # 如果服务台数大于等于顾客数，每个顾客等待时间为0
    if s >= n:
        return 0.0
    
    # 计算每个顾客的等待时间
    total_waiting = 0
    # 分成s组，每组由一个服务台处理
    for i in range(n):
        # 每个顾客的等待时间是前面同组顾客的服务时间之和
        # 同组前面的顾客数是 i // s
        prev_customers = i // s
        if prev_customers > 0:
            # 前prev_customers个顾客的服务时间之和
            group_start = (i // s) * s
            total_waiting += sum(times[group_start:i])
    
    # 计算平均等待时间
    avg_waiting = total_waiting / n
    return avg_waiting

# 测试
n = 5  # 顾客数
s = 2  # 服务台数
times = [4, 1, 5, 2, 3]  # 每个顾客的服务时间
result = min_avg_waiting_time(n, s, times)
print(f"最小平均等待时间: {result:.2f}")