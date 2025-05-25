# 活动选择问题：选择最多的不重叠活动

def activity_selection(activities):
    # 按照活动的结束时间进行排序
    activities.sort(key=lambda x: x[1])  # x 是 (开始时间, 结束时间)

    selected = []  # 存放选择的活动
    current_end = 0  # 当前结束时间

    for start, end in activities:
        if start >= current_end:
            selected.append((start, end))
            current_end = end  # 更新结束时间

    return selected


# 测试用例
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]

selected_activities = activity_selection(activities)

print("最多可以安排的活动数量为：", len(selected_activities))
print("安排的活动为：", selected_activities)
