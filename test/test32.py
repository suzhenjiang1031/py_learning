import math
import queue

# 节点类：表示搜索树中的一个状态
class Node:
    def __init__(self, cp, cw, myid):
        self.cp = cp  # 当前收益（current profit）
        self.cw = cw  # 当前重量（current weight）
        self.id = myid  # 节点编号（对应一棵完全二叉树）

# 上界函数：用于估计该节点向下扩展可能达到的最大价值（限界条件）
def bound(node):
    global c, goods, n
    cleft = c - node.cw  # 背包剩余容量
    b = node.cp          # 当前已获得价值
    i = int(math.log2(node.id)) + 1  # 当前节点在层数 i

    # 尽可能装满剩下的物品（按性价比排序）
    while i < n and goods[i][1] <= cleft:
        cleft -= goods[i][1]
        b += goods[i][2]
        i += 1

    # 如果还有容量但下一个物品装不下，则部分装入（分数法）
    if i < n:
        b += goods[i][2] / goods[i][1] * cleft

    return b

# 主算法函数：分支限界法（队列式 BFS）
def queue_branch(capacity):
    global goods, n
    bestp = 0  # 当前最优价值
    best = 0   # 最优节点编号（用于反推出选择方案）
    que = queue.Queue()
    root = Node(0, 0, 1)  # 初始根节点
    que.put(root)

    while not que.empty():
        current_node = que.get()
        depth = int(math.log2(current_node.id))  # 当前节点所在深度

        # 如果到达叶子节点
        if depth == n:
            if current_node.cp > bestp:
                bestp = current_node.cp
                best = current_node.id
        else:
            # 左子节点：选择当前层物品（尝试装入）
            next_weight = current_node.cw + goods[depth][1]
            next_profit = current_node.cp + goods[depth][2]
            if next_weight <= capacity:
                if next_profit > bestp:
                    bestp = next_profit
                    best = current_node.id * 2
                que.put(Node(next_profit, next_weight, current_node.id * 2))

            # 右子节点：不选择当前物品，判断是否有潜力再扩展
            if bound(current_node) > bestp:
                que.put(Node(current_node.cp, current_node.cw, current_node.id * 2 + 1))

    return bestp, best

# 根据最终的 best 节点 id 反推选择的物品
def get_bestx(best):
    global n, goods
    bestx = [0] * n
    i = best
    while i > 1:
        parent = i // 2
        is_left = (i % 2 == 0)
        depth = int(math.log2(i)) - 1
        if is_left:
            bestx[goods[depth][0]] = 1  # 说明该层选择了物品
        i = parent
    return bestx

# 主程序
if __name__ == '__main__':
    n = 5                # 物品数量
    c = 10               # 背包容量
    # goods = [编号, 重量, 价值]
    goods = [[0, 2, 6], [1, 2, 3], [2, 6, 5], [3, 5, 4], [4, 4, 6]]
    # 按性价比（价值/重量）从大到小排序（用于上界估计）
    goods.sort(key=lambda x: x[2] / x[1], reverse=True)

    bestp, best = queue_branch(c)
    bestx = get_bestx(best)

    print("最大价值为：", bestp)
    print("最优解为：", bestx)
