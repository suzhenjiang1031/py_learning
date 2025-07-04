# 添加噪声
def add_awgn(signal, snr_db):
    snr = 10 ** (snr_db / 10)
    power_signal = np.mean(np.square(signal))
    noise_power = power_signal / snr
    noise = np.random.normal(0, np.sqrt(noise_power), size=signal.shape)
    return signal + noise

# 示例：对每一帧添加 SNR = 10dB 的噪声
noisy_signal = [add_awgn(s, snr_db=10) for s in signal]

# 解码
print("\n解码结果（含噪声）:")
for user in codebook:
    decoded = []
    for sig in noisy_signal:
        bit = np.dot(sig, codebook[user]) / len(codebook[user])
        decoded.append(round(bit))
    print(f"用户 {user}：{decoded}")
