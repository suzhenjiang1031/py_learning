import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering, KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score
import matplotlib

# 设置 matplotlib 使用支持中文的字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用 SimHei 字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 设置随机种子以确保可重复性
np.random.seed(42)

# 加载数据集（用于演示的合成数据）
def load_data():
    n_samples = 1000
    data = {
        'CustomerID': range(n_samples),
        'Flight_Frequency': np.random.poisson(5, n_samples),
        'Total_Spend': np.random.normal(1000, 300, n_samples),
        'Average_Ticket_Price': np.random.normal(200, 50, n_samples),
        'Loyalty_Points': np.random.normal(500, 100, n_samples),
        'Satisfaction_Score': np.random.randint(1, 6, n_samples)
    }
    df = pd.DataFrame(data)
    return df

# 数据预处理
def preprocess_data(df):
    df = df.fillna(df.mean(numeric_only=True))
    numeric_cols = ['Flight_Frequency', 'Total_Spend', 'Average_Ticket_Price', 
                   'Loyalty_Points', 'Satisfaction_Score']
    Q1 = df[numeric_cols].quantile(0.25)
    Q3 = df[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[numeric_cols] < (Q1 - 1.5 * IQR)) | 
              (df[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df

# 特征提取
def extract_features(df):
    features = df[['Flight_Frequency', 'Total_Spend', 'Average_Ticket_Price', 
                  'Loyalty_Points', 'Satisfaction_Score']]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    return features_scaled, features.columns

# 聚类方法
def perform_clustering(X, n_clusters=3):
    results = {}
    
    # DIANA（分裂层次聚类）
    Z = linkage(X, method='ward')
    diana_labels = fcluster(Z, t=n_clusters, criterion='maxclust')
    results['DIANA'] = diana_labels
    
    # AGNES（凝聚层次聚类，使用不同链接方法）
    linkages = ['ward', 'complete', 'average', 'single']
    for linkage_method in linkages:
        agnes = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage_method)
        results[f'AGNES_{linkage_method}'] = agnes.fit_predict(X)
    
    # K-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    results['K-means'] = kmeans.fit_predict(X)
    
    return results, Z

# 可视化
def plot_results(X, cluster_results, Z, feature_names):
    fig = plt.figure(figsize=(20, 12))
    fig.suptitle('客户分群结果', fontsize=16)
    
    # 子图1：DIANA 树状图
    plt.subplot(2, 4, 1)
    dendrogram(Z, truncate_mode='lastp', p=12)
    plt.title('DIANA 树状图')
    
    # 各聚类方法的散点图
    methods = list(cluster_results.keys())
    for i, method in enumerate(methods, 2):
        plt.subplot(2, 4, i)
        sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=cluster_results[method], 
                       palette='deep', legend=False)
        plt.title(method)
        plt.xlabel(feature_names[0])
        plt.ylabel(feature_names[1])
    
    plt.tight_layout()
    plt.savefig('customer_segmentation.png')
    plt.close()

# 客户价值评估
def assess_customer_value(df, cluster_labels):
    df['Cluster'] = cluster_labels
    cluster_summary = df.groupby('Cluster').agg({
        'Flight_Frequency': 'mean',
        'Total_Spend': 'mean',
        'Satisfaction_Score': 'mean',
        'CustomerID': 'count'
    }).rename(columns={'CustomerID': 'Count'})
    
    cluster_summary['Value_Score'] = (
        0.4 * cluster_summary['Total_Spend'] / cluster_summary['Total_Spend'].max() +
        0.3 * cluster_summary['Flight_Frequency'] / cluster_summary['Flight_Frequency'].max() +
        0.3 * cluster_summary['Satisfaction_Score'] / cluster_summary['Satisfaction_Score'].max()
    )
    
    return cluster_summary.sort_values('Value_Score', ascending=False)

def main():
    df = load_data()
    df_cleaned = preprocess_data(df)
    X, feature_names = extract_features(df_cleaned)
    cluster_results, Z = perform_clustering(X)
    plot_results(X, cluster_results, Z, feature_names)
    kmeans_summary = assess_customer_value(df_cleaned, cluster_results['K-means'])
    
    print("\n客户价值评估 (K-means):")
    print(kmeans_summary)
    
    print("\n轮廓系数:")
    for method, labels in cluster_results.items():
        score = silhouette_score(X, labels)
        print(f"{method}: {score:.3f}")

if __name__ == "__main__":
    main()