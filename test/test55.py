# 选择相关特征
features = ['MONTH', 'DAY_OF_MONTH', 'DAY_OF_WEEK', 'AIRLINE', 'ORIGIN_AIRPORT',
            'DESTINATION_AIRPORT', 'SCHEDULED_DEPARTURE', 'SCHEDULED_ARRIVAL',
            'DISTANCE', 'DEPARTURE_DELAY']

# 目标：是否延误（延误大于15分钟定义为延误）
df = df[features].dropna()
df['DELAYED'] = df['DEPARTURE_DELAY'].apply(lambda x: 1 if x > 15 else 0)
df = df.drop(columns=['DEPARTURE_DELAY'])

# 编码分类变量
from sklearn.preprocessing import LabelEncoder

categorical_cols = ['AIRLINE', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

print(df.head())
