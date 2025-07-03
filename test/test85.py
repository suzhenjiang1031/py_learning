import numpy as np

# 定义每个用户的伪随机码（注意尽量正交）
codebook = {
    'A': np.array([1, -1, 1, -1]),
    'B': np.array([1, 1, -1, -1]),
    'C': np.array([1, -1, -1, 1])
}

# 用户发送的数据（可以是 +1 或 -1）
data = {
    'A': 1,
    'B': -1,
    'C': 1
}

# 发送：所有用户的扩频信号叠加
channel_signal = sum(data[u] * codebook[u] for u in data)
print("信道中的复合信号：", channel_signal)

# 接收端解扩
for user in codebook:
    recovered = np.dot(channel_signal, codebook[user]) / len(codebook[user])
    print(f"用户 {user} 解扩后数据：{recovered:.2f}")
