class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item, self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            return item
        return None

    def peek(self):
        if not self.is_empty():
            return self.top.data
        return None

    def __iter__(self):
        current = self.top
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return " -> ".join(str(item) for item in self)

def is_valid_move(maze, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

def solve_maze(maze, start, end):
    stack = Stack()
    stack.push((start, [start]))  # 存储当前位置和路径

    while not stack.is_empty():
        (current_pos, path) = stack.pop()
        x, y = current_pos

        if current_pos == end:
            return path

        # 标记当前位置为已访问
        maze[x][y] = 2

        # 上下左右四个方向
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = x + move[0], y + move[1]
            if is_valid_move(maze, next_x, next_y):
                stack.push(((next_x, next_y), path + [(next_x, next_y)]))

    return None

# 迷宫表示
# 0 - 路径
# 1 - 墙壁
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0]
]

start = (0, 0)
end = (5, 4)

path = solve_maze(maze, start, end)

if path:
    print("找到路径:", path)
else:
    print("没有路径")
