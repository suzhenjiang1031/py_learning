def fractional_knapsack(weights, values, capacity):
    items = sorted([(v/w, w, v) for w, v in zip(weights, values)], reverse=True)
    total_value = 0
    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("最大价值（分数背包）:", fractional_knapsack(weights, values, capacity))
