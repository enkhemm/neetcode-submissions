# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp = []
	
         # list of treenodes that we need to process, after writing this realized that maybe bfs doesnt work so need to switch to dfs
        q = deque([root])
        
        while q:
            node = q.popleft()
            if not node:
                continue
            # if node.val > hp[0]
            #     continue
            if len(hp) < k:
                heapq.heappush_max(hp, node.val)
            if len(hp) == k and node.val < hp[0]:
                heapq.heappop_max(hp)
                heapq.heappush_max(hp, node.val)


            q.append(node.left)
            q.append(node.right)


        return hp[0]
	
#         5
#     3      6
#   2   4       
# 1

# q = 6, 2, 4
# hp = 5 3

#    3
# 1      6  k = 3

