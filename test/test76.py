import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成示例数据（包含噪声）
np.random.seed(42)
data = np.concatenate([np.random.normal(50, 10, 100), [200, -50]])  # 添加两个异常值
df = pd.DataFrame({'value': data})

# 检测异常值（Z分数法）
z_scores = np.abs((df['value'] - df['value'].mean()) / df['value'].std())
threshold = 3
outliers = df[z_scores > threshold]

print("检测到的异常值：")
print(outliers)

# 处理异常值：用中位数替换
df_cleaned = df.copy()
df_cleaned.loc[z_scores > threshold, 'value'] = df['value'].median()

# 可视化
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(df['value'])
plt.title('原始数据（含噪声）')
plt.subplot(1, 2, 2)
plt.boxplot(df_cleaned['value'])
plt.title('清洗后数据')
plt.show()

# 缺失值处理示例
df_with_missing = df.copy()
df_with_missing.loc[::10, 'value'] = np.nan  # 每10行插入缺失值
print("\n缺失值数量：", df_with_missing['value'].isna().sum())
df_with_missing['value'].fillna(df_with_missing['value'].mean(), inplace=True)
print("缺失值填充后：", df_with_missing['value'].isna().sum())