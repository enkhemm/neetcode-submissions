# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, maxSoFar) -> int:
            
            if not node: return 0

            res = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            res += dfs(node.right, maxSoFar)
            res += dfs(node.left, maxSoFar)
          
            return res
                
        return dfs(root, root.val)
        