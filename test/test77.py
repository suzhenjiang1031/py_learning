from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载数据集
iris = load_iris()
X, y = iris.data, iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 构建决策树模型
clf = DecisionTreeClassifier(max_depth=3, criterion='gini', random_state=42)
clf.fit(X_train, y_train)

# 预测并评估
y_pred = clf.predict(X_test)
print(f"准确率: {accuracy_score(y_test, y_pred):.2f}")

# 可视化决策树（需安装graphviz）
from sklearn.tree import export_graphviz
import graphviz
dot_data = export_graphviz(clf, out_file=None, feature_names=iris.feature_names, 
                           class_names=iris.target_names, filled=True)
graph = graphviz.Source(dot_data)
graph.render("iris_decision_tree", view=True)