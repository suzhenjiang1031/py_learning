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

def tree_height(root):
    if not root:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height) + 1

while True:
    try:
        preorder = input().split()
        root = build_tree(preorder)
        height = tree_height(root)
        print(height)

    except EOFError:
        break
