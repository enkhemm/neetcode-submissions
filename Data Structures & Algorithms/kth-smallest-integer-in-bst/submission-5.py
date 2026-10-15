# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder traversal after consult with chatgpt:

        # usign dfs:
        # count = 0
        # res = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     res.append(node.val)
        #     if len(res) == k:
        #         return

        #     dfs(node.right)


        # dfs(root)
        # return res[k - 1]

        cnt = k
        res = root.val

        def dfs(node):

            nonlocal res, cnt
            if not node:
                return

            dfs(node.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res



        