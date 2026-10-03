# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # if root.left and root.left.val >= root.val:
        #     return False
        # if root.right and root.right.val <= root.val:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        return self.isInRange(root, float("-inf"), float("inf"))


    def isInRange(self, root, low, high):
        if not root:
            return True
        # when validity breaks
        if root.val >= high or root.val <= low:
            return False

        left =  self.isInRange(root.left, low, root.val)
        right = self.isInRange(root.right, root.val, high)

        return left and right

    #       2
    # 1           3

    # isV(3)
    # return true and .true
    # return isV(null) and isV(null) -> true


#                 0
#       -1000             1000
# -2000         -1    1     
        