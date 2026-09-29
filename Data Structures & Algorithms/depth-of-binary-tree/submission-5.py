# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # REDO

        # recursive:

        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        stack = []
        max_depth = 0 # (4, 3)

        if not root:
            return max_depth

        stack.append((root, 1))
        max_depth = (root, 1)

        # FIFO
        # [] (node, depth)

        while stack:
            cur, d = stack.pop() 

            if not cur:
                continue

            if d > max_depth[1]:
                max_depth = (cur, d)
            
            stack.append((cur.left, d + 1))
            stack.append((cur.right, d + 1))
        
        return max_depth[1]

        # # iterative
        # stack = []
        # # stack is going to be the node and the height at that level
        # depth = 0
        # if not root:
        #     return depth

        # depth += 1
        # stack.append((root, depth))

        # while stack:
        #     node = stack.pop()
        #     if not node:
        #         continue
        #     stack.append(root.left, node[1]+1)
        
        # return depth








