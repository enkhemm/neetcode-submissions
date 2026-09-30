# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root) -> int:
        if not root:
            return 0

        return 1 + max(self.dfs(root.left), self.dfs(root.right))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = []

        stack.append(root)
        while stack:

            node = stack.pop()
            if not node:
                continue

            stack.append(node.left) #0
            stack.append(node.right) #3

            longest_left = self.dfs(node.left)
            longest_right = self.dfs(node.right)

            diameter = longest_left + longest_right # 3
            res = max(diameter, res) #3

        return res



