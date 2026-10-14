# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp = []
	
         # list of treenodes that we need to process
        q = deque([root])
        
        while q:
            node = q.popleft()
            if not node:
                continue
            if len(hp) < k:
                heapq.heappush_max(hp, node.val)
            if len(hp) == k and node.val < hp[-1]:
                heapq.heappop_max(hp)
                heapq.heappush_max(hp, node.val)


            q.append(node.left)
            q.append(node.right)


        return hp[0]
	

