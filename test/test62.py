from collections import deque

def bfs(capacity, flow, s, t, parent):
    visited = [False] * len(capacity)
    queue = deque([s])
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
        # 找到增广路径的最小容量
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u
        # 增加路径上的流
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
        max_flow += path_flow
    return max_flow

# 主程序读取输入
def main():
    N, M = map(int, input().split())
    capacity = [[0]*N for _ in range(N)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        capacity[s-1][e-1] += c  # 注意合并重边
    print(edmonds_karp(N, 0, N-1, capacity))  # 家乡是点1（索引0），大海是点N（索引N-1）

if __name__ == "__main__":
    main()
