import numpy as np

# 用户码序列（正交的伪随机序列）
code_A = np.array([1, -1, 1, -1])
code_B = np.array([1, 1, -1, -1])

# 用户要发送的数据
data_A = 1   # 表示 +1
data_B = -1  # 表示 -1

# 发送时进行扩频
signal_A = data_A * code_A
signal_B = data_B * code_B

# 多用户信号在信道中叠加
channel_signal = signal_A + signal_B
print("信道中传播的信号：", channel_signal)

# 接收端：用户 A 用自己的码解扩
recovered_A = np.dot(channel_signal, code_A) / len(code_A)
print("用户 A 解扩后恢复的数据：", recovered_A)

# 接收端：用户 B 用自己的码解扩
recovered_B = np.dot(channel_signal, code_B) / len(code_B)
print("用户 B 解扩后恢复的数据：", recovered_B)
