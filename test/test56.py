# ID3使用的信息增益，不是sklearn默认支持的，需要设置 criterion='entropy'
id3 = DecisionTreeClassifier(criterion='entropy', max_depth=10)
id3.fit(X_train, y_train)
y_pred_id3 = id3.predict(X_test)

print("ID3 分类报告:")
print(classification_report(y_test, y_pred_id3))
print("准确率:", accuracy_score(y_test, y_pred_id3))
