class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder):
    if not preorder:
        return None

    val = preorder.pop(0)
    if val == '#':
        return None
    node = TreeNode(val)
    node.left = build_tree(preorder)
    node.right = build_tree(preorder)
    return node

def find_levels(root, nodes):
    def dfs(node, level, target):
        if not node:
            return
        if node.val == target:
            levels.append(level)
            return

        dfs(node.left, level + 1, target)
        dfs(node.right, level + 1, target)

    levels = []

    for node in nodes:
        level = dfs(root, 1, node)
        levels.append(level)
    return levels
    
while True:
    try:
        preorder = input().strip().split()
        nodes = input().strip()
        root = build_tree(preorder)
        nodes = nodes.strip()
        nodes = nodes.split(',')
        levels = find_levels(root, nodes)
        print(','.join(str(level) for level in levels))
        
    except EOFError:
        break

