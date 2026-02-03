class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def bfs(root):
    if not root:
        return []

    queue = [root]
    while queue:
        node = queue.pop(0)

        
        print(node.value, end = " ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

bfs(root)