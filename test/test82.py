import matplotlib.pyplot as plt

# 初始化参数
cwnd_list = []
rtt_list = []

cwnd = 1
ssthresh = 16
rtt = 1

# 阶段 1：慢启动 + 拥塞避免，直到 cwnd 达到 40（模拟正常增长）
while cwnd < 40:
    cwnd_list.append(cwnd)
    rtt_list.append(rtt)
    
    if cwnd < ssthresh:
        cwnd *= 2  # 慢启动：指数增长
    else:
        cwnd += 1  # 拥塞避免：线性增长

    rtt += 1

# 阶段 2：发生三次重复 ACK（快速重传）
cwnd_list.append(cwnd)
rtt_list.append(rtt)
ssthresh = cwnd // 2
cwnd = ssthresh
rtt += 1

# 快速恢复后继续线性增长几轮
for _ in range(5):
    cwnd_list.append(cwnd)
    rtt_list.append(rtt)
    cwnd += 1
    rtt += 1

# 阶段 3：超时（模拟严重丢包）
cwnd_list.append(cwnd)
rtt_list.append(rtt)
ssthresh = cwnd // 2
cwnd = 1  # 回到慢启动
rtt += 1

# 慢启动重新开始几轮
for _ in range(5):
    cwnd_list.append(cwnd)
    rtt_list.append(rtt)
    if cwnd < ssthresh:
        cwnd *= 2
    else:
        cwnd += 1
    rtt += 1

# 绘图
plt.figure(figsize=(10, 5))
plt.plot(rtt_list, cwnd_list, marker='o')
plt.title('TCP 拥塞窗口（cwnd）随 RTT 变化模拟')
plt.xlabel('RTT（轮次）')
plt.ylabel('拥塞窗口 cwnd')
plt.grid(True)
plt.show()
