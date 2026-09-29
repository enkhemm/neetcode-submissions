# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #use bfs? so use a queue

        if not root:
            return None
        q = deque([root])
        #q.append(root)
        # n = q.popleft()
        # print(n.val)

        while q:
            node = q.popleft()
            node.right, node.left = node.left, node.right

            if node.right: #something in node.r
                q.append(node.right)
            if node.left:
                q.append(node.left)

        
        return root


        