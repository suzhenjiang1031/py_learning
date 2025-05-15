def knapsack_branch_bound(i, current_weight, current_value, capacity, weight, value, best):
    global max_value
    if i == len(weight):
        if current_value > max_value:
            max_value = current_value
        return

    # bound 剪枝
    remain = capacity - current_weight
    bound = current_value
    for j in range(i, len(weight)):
        if weight[j] <= remain:
            remain -= weight[j]
            bound += value[j]
        else:
            bound += value[j] / weight[j] * remain
            break
    if bound < max_value:
        return  # 剪枝

    # 尝试选
    if current_weight + weight[i] <= capacity:
        knapsack_branch_bound(i + 1, current_weight + weight[i], current_value + value[i], capacity, weight, value, best)
    # 尝试不选
    knapsack_branch_bound(i + 1, current_weight, current_value, capacity, weight, value, best)
