# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        inMap = defaultdict(int)
        for i, n in enumerate(inorder):
            inMap[n] = i

        root = TreeNode(preorder[0])

        rootInd = 0

        def dfs(l, r) -> TreeNode:
            if not preorder or not inorder:
                return None
                
            nonlocal rootInd
            root = TreeNode(preorder[rootInd])
            mid = inMap[rootInd]
            mid.left = dfs(rootInd + 1, mid + 1)
            mid.right = dfs(mid+1, len(preorder))

            rootInd += 1
            return root


        dfs(0, len(preorder))
        return root








#         if not preorder or not inorder:
#             return None

#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
#         return root
        """
        preorder: node, left, right
        1, 2,  5,  3, 6, 4
        inorder: left, node, right
        5, 2,  1,  6, 3, 4


                1
            2        3
        5         6      4
 
        use two pointers??
        first in pre will be the root

        
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        """
# Amazon oa: dp problem
# list of binary digits in a string 0s and 1s, based of the string determine the subsequent of the largest pair of twin integers by removing various subsequences of strings..