class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(root):
    # 使用中序遍历打印二叉树
    if root:
        print_tree(root.left)
        print(root.value, end=" ")
        print_tree(root.right)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 打印二叉树
    print("二叉树中序遍历结果: ", end='')
    print_tree(root)

if __name__ == "__main__":
    main()
