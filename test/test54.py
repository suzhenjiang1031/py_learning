from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 10, 20]
}

grid_search = GridSearchCV(DecisionTreeClassifier(criterion='gini'), param_grid, cv=3)
grid_search.fit(X_train, y_train)

print("最优参数:", grid_search.best_params_)
best_model = grid_search.best_estimator_
y_pred_opt = best_model.predict(X_test)

print("优化后准确率:", accuracy_score(y_test, y_pred_opt))
