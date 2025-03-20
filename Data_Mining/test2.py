import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 使用绝对路径加载数据集
try:
    df = pd.read_excel(r'D:\python_learning\py_learning\Data_Mining\Online Retail.xlsx')
    print("文件加载成功！")
except FileNotFoundError:
    print("错误：找不到 'Online Retail.xlsx' 文件，请检查文件路径！")
    exit(1)
except Exception as e:
    print(f"加载文件时发生错误：{e}")
    exit(1)

# 转换为字符串类型
df['InvoiceNo'] = df['InvoiceNo'].astype(str)
df['StockCode'] = df['StockCode'].astype(str)

# 数据清洗
df = df[(~df['InvoiceNo'].str.startswith('C')) & (df['Quantity'] > 0)].dropna(subset=['StockCode'])

# 取样（可选）
df = df.sample(frac=0.1, random_state=42)  # 取10%数据

# 创建 StockCode 到 Description 的映射
stockcode_to_desc = df[['StockCode', 'Description']].drop_duplicates().set_index('StockCode')['Description'].to_dict()

# 创建购物篮
print("正在创建购物篮...")
baskets = df.groupby('InvoiceNo')['StockCode'].apply(list).reset_index()

# 转换为one-hot编码
print("正在转换为one-hot编码...")
te = TransactionEncoder()
te_ary = te.fit(baskets['StockCode'].tolist()).transform(baskets['StockCode'].tolist())
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

# 挖掘频繁项集
print("正在挖掘频繁项集...")
frequent_itemsets = apriori(df_onehot, min_support=0.01, use_colnames=True)

# 生成关联规则
print("正在生成关联规则...")
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# 筛选规则
print("正在筛选规则...")
rules_filtered = rules[(rules['confidence'] > 0.5) & (rules['lift'] > 1)]
rules_filtered = rules_filtered.sort_values(by='lift', ascending=False)

# 添加商品描述
rules_filtered['antecedents_desc'] = rules_filtered['antecedents'].apply(lambda x: [stockcode_to_desc[item] for item in x])
rules_filtered['consequents_desc'] = rules_filtered['consequents'].apply(lambda x: [stockcode_to_desc[item] for item in x])

# 打印前10条规则
print(rules_filtered[['antecedents_desc', 'consequents_desc', 'support', 'confidence', 'lift']].head(10))

# 保存结果
rules_filtered.to_csv('association_rules.csv', index=False)
print("规则已保存到 association_rules.csv")