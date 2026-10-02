# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use bst using iterative queue method
        # will keep track of an i variable just to know which which list element to append to in our lest 
        # res[i].append(val)
        

        # for loop to know how many elements to pop from the queue
        # i = 2 * i
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            times = len(q)
            level = []
            for _ in range(times):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level)

        return res

#          1
#     2          3 
# 4     5     6      7

# res=[[1]]
# q =  3 , 4, 5
# i = 2
# while:
#     2 times
#     node = 2

    # Time and space complexity: O(n)


        