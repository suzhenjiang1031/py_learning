import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, LSTM, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam
import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')

# 1. 数据收集
def load_data():
    # 假设数据集为 CSV 文件，包含代码特征和坏味标签
    # 实际使用 GitHub 数据集：https://github.com/BINH-NGUYENTHANH/codesmellDataset
    data = pd.read_csv('codesmell_dataset.csv')  # 替换为实际数据集路径
    print("数据概览:")
    print(data.info())
    print("\n缺失值统计:")
    print(data.isnull().sum())
    return data

# 2. 数据预处理
def preprocess_data(data):
    # 假设数据包含 AST 特征和词向量特征
    features = [col for col in data.columns if col.startswith('feature_')]  # 特征列
    X = data[features]
    y = data[['GodClass', 'LongMethod', 'FeatureEnvy', 'DataClass']]  # 多标签
    
    # 填补缺失值
    X = X.fillna(0)
    
    # 标准化特征
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # 数据增强：SMOTE 过采样
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    
    # 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, test_size=0.15, random_state=42
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.1765, random_state=42  # 0.1765 ≈ 15/85
    )
    
    # 重塑为 3D 输入（samples, timesteps, features）
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_val = X_val.reshape(X_val.shape[0], X_val.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

# 3. 模型构建
def build_model(input_shape, num_classes):
    model = Sequential([
        Input(shape=input_shape),
        Conv1D(filters=64, kernel_size=3, activation='relu', padding='same'),
        Dropout(0.5),
        LSTM(128, return_sequences=False),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='sigmoid')  # 多标签分类
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# 4. 模型训练
def train_model(model, X_train, y_train, X_val, y_val):
    history = model.fit(
        X_train, y_train, validation_data=(X_val, y_val),
        epochs=50, batch_size=64, verbose=1,
        callbacks=[tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)]
    )
    return history

# 5. 模型评估
def evaluate_model(model, X_test, y_test, labels):
    y_pred = (model.predict(X_test) > 0.5).astype(int)
    for i, label in enumerate(labels):
        print(f"\n{label} 性能:")
        print(classification_report(y_test[:, i], y_pred[:, i]))

# 主函数
def main():
    print("加载数据...")
    data = load_data()
    
    print("\n预处理数据...")
    X_train, X_val, X_test, y_train, y_val, y_test = preprocess_data(data)
    
    print("\n构建模型...")
    model = build_model(input_shape=(X_train.shape[1], 1), num_classes=y_train.shape[1])
    
    print("\n训练模型...")
    history = train_model(model, X_train, y_train, X_val, y_val)
    
    print("\n评估模型...")
    evaluate_model(model, X_test, y_test, ['GodClass', 'LongMethod', 'FeatureEnvy', 'DataClass'])

if __name__ == "__main__":
    main()