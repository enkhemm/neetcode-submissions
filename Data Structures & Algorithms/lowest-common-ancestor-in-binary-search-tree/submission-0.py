# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # i want to use bfs because in that way we can track the levels after finding the p or q
        # iterative bfs using queues wont act work bcz we need to go back to where parent is
        # so we use iterative stack to track the number level we are at
        # 

        # find where the node is and name the leve what level it is located at
        if not root:
            # or TreeNode()?
            return TreeNode

        def findPathToNode(root, node) -> List:
            # OMG I FORGOT IT IS A BST NOT BT:
            res = []
            # adds paths from root until  p
            while root != node:
                res.append(root)
                if node.val < root.val:
                    root = root.left
                else:
                    root = root.right
            res.append(root)
                

            return res

        
        pathp = findPathToNode(root, p)
        pathq = findPathToNode(root, q)
        print(pathp)
        print(pathq)

        while len(pathp) != len(pathq):
            if len(pathp) > len(pathq):
                pathp.pop()
            else:
                pathq.pop()



        while pathp[-1] != pathq[-1]:
            pathp.pop()
            pathq.pop()

        return pathp[-1] 








