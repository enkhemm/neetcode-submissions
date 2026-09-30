# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height_left = self.dfs(root.left)
        height_right = self.dfs(root.right)

        if abs(height_left - height_right) > 1:
            return False

        return self.isBalanced(root.right) and self.isBalanced(root.left)

    def dfs(self, root) -> int:
        if not root:
            return 0

        return 1 + max(self.dfs(root.left), self.dfs(root.right))