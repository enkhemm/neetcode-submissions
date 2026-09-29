# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iter dfs
        if not root:
            return 0
        maxDepth = 0
        stack = []
        stack.append(root) # stack is a list itself of it is not the same requirement as deque([root])
        curr = 1

        while stack:
            node = stack.pop()
            
            if not node.right and not node.left:
                maxDepth = max(maxDepth, curr)
                curr = 0
            if node.right:
                curr += 1
                stack.append(node.right)
                continue
            if node.left:
                curr += 1
                continue

        return maxDepth
        

    
        