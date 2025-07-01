import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初始化变量
rtt_list = []
cwnd_list = []
ssthresh_list = []

# 初始状态
cwnd = 1
ssthresh = 16
rtt = 1

# 数据记录函数
def record(cwnd, ssthresh, rtt):
    rtt_list.append(rtt)
    cwnd_list.append(cwnd)
    ssthresh_list.append(ssthresh)

# 阶段 1：慢启动和拥塞避免直到 cwnd 接近 40
while cwnd < 40:
    record(cwnd, ssthresh, rtt)
    if cwnd < ssthresh:
        cwnd *= 2  # 慢启动
    else:
        cwnd += 1  # 拥塞避免
    rtt += 1

# 阶段 2：模拟快速重传（三个重复 ACK）
record(cwnd, ssthresh, rtt)
ssthresh = cwnd // 2
cwnd = ssthresh
rtt += 1

# 快速恢复后线性增长几轮
for _ in range(5):
    record(cwnd, ssthresh, rtt)
    cwnd += 1
    rtt += 1

# 阶段 3：模拟超时
record(cwnd, ssthresh, rtt)
ssthresh = cwnd // 2
cwnd = 1  # 回到慢启动
rtt += 1

# 重新慢启动几轮
for _ in range(5):
    record(cwnd, ssthresh, rtt)
    if cwnd < ssthresh:
        cwnd *= 2
    else:
        cwnd += 1
    rtt += 1

# 创建绘图
fig, ax = plt.subplots()
line1, = ax.plot([], [], 'bo-', label='cwnd')
line2, = ax.plot([], [], 'r--', label='ssthresh')

ax.set_xlim(0, max(rtt_list) + 1)
ax.set_ylim(0, max(cwnd_list) + 10)
ax.set_xlabel('RTT（轮次）')
ax.set_ylabel('窗口大小')
ax.set_title('TCP 拥塞控制动态模拟（cwnd & ssthresh）')
ax.grid(True)
ax.legend()

# 更新函数
def update(frame):
    line1.set_data(rtt_list[:frame], cwnd_list[:frame])
    line2.set_data(rtt_list[:frame], ssthresh_list[:frame])
    return line1, line2

# 动画生成
ani = animation.FuncAnimation(fig, update, frames=len(rtt_list), interval=300, blit=True)

# 显示动画
plt.show()
