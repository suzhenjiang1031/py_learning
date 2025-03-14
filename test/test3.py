# 定义图：用邻接表存储
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node)  # 访问当前节点
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# 测试
print("递归 DFS 遍历：")
dfs_recursive(graph, 'A')
