from collections import deque
import sys

def bfs(capacity, flow, s, t, parent):
    visited = [False] * len(capacity)
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if not visited[v] and capacity[u][v] - flow[u][v] > 0:
                parent[v] = u
                visited[v] = True
                if v == t:
                    return True
                queue.append(v)
    return False

def edmonds_karp(n, s, t, capacity):
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0
    while bfs(capacity, flow, s, t, parent):
        # 找增广路径上的最小残量
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u
        # 更新路径上的流量
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
        max_flow += path_flow
    return max_flow

# 主函数，处理输入
def main():
    n, m, s, t = map(int, input().split())
    capacity = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        capacity[u - 1][v - 1] += c  # 允许重边合并容量
    print(edmonds_karp(n, s - 1, t - 1, capacity))

if __name__ == "__main__":
    main()
