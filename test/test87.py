import numpy as np

# 设置随机种子确保可复现
np.random.seed(42)

# 每个用户的码序列（正交 or 几乎正交）
codebook = {
    'A': np.array([1, -1, 1, -1]),
    'B': np.array([1, 1, -1, -1]),
    'C': np.array([-1, 1, 1, -1])
}

# 每个用户发送的比特流（1表示+1，0表示-1）
bitstream = {
    'A': [1, 0, 1],
    'B': [0, 0, 1],
    'C': [1, 1, 0]
}

# 映射成 +1/-1 格式
mapped_bits = {
    user: [1 if b == 1 else -1 for b in bits]
    for user, bits in bitstream.items()
}

# 添加 AWGN 高斯白噪声函数
def add_awgn(signal, snr_db):
    snr = 10 ** (snr_db / 10)
    power_signal = np.mean(np.square(signal))
    noise_power = power_signal / snr
    noise = np.random.normal(0, np.sqrt(noise_power), size=signal.shape)
    return signal + noise

# 发送：每个时刻将所有用户的扩频信号叠加，并加噪声
snr_db = 10  # 信噪比 (dB)
channel_signals = []
for i in range(len(mapped_bits['A'])):
    total_signal = sum(mapped_bits[u][i] * codebook[u] for u in codebook)
    noisy_signal = add_awgn(total_signal, snr_db)
    channel_signals.append(noisy_signal)

# 接收：每个用户解扩并解码
decoded = {}
for user in codebook:
    user_decoded = []
    for signal in channel_signals:
        bit = np.dot(signal, codebook[user]) / len(codebook[user])
        user_decoded.append(1 if bit > 0 else 0)
    decoded[user] = user_decoded

# 显示结果
print("发送比特流：")
for u in bitstream:
    print(f"用户 {u}: {bitstream[u]}")

print("\n解码结果：")
for u in decoded:
    print(f"用户 {u}: {decoded[u]}")
