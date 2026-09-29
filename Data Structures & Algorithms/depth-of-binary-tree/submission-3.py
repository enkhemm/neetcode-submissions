# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        # if not root:
        #     return 0
        
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iter dfs
        if not root:
            return 0
        # maxDepth = 0
        # stack = []
        # stack.append(root) # stack is a list itself of it is not the same requirement as deque([root])
        # curr = 0

        # while stack:
        #     node = stack.pop()
        #     curr += 1
            
        #     if not node.right and not node.left:
        #         maxDepth = max(maxDepth, curr)
        #         curr = 0
        #     if node.right:
        #         stack.append(node.right)
                
        #     if node.left:
        #         stack.append(node.left)
                

        # return maxDepth

        #After kelly and solution:
        res = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if node: # if curr is not empty
                res = max(res, depth)
                stack.extend(((node.left, depth + 1), (node.right, depth + 1)))

            else:
                continue

        return res

    
        