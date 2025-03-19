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
df['StockCode'] = df['StockCode'].astype(str)  # 强制转换为字符串

# 数据清洗
df = df[(~df['InvoiceNo'].str.startswith('C')) & (df['Quantity'] > 0)].dropna(subset=['StockCode'])

# 创建购物篮
baskets = df.groupby('InvoiceNo')['StockCode'].apply(list).reset_index()

# 转换为one-hot编码
te = TransactionEncoder()
te_ary = te.fit(baskets['StockCode'].tolist()).transform(baskets['StockCode'].tolist())
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

# 挖掘频繁项集
frequent_itemsets = apriori(df_onehot, min_support=0.01, use_colnames=True)

# 生成关联规则
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# 筛选规则
rules_filtered = rules[(rules['confidence'] > 0.5) & (rules['lift'] > 1)]
rules_filtered = rules_filtered.sort_values(by='lift', ascending=False)

# 打印前10条规则
print(rules_filtered.head(10))