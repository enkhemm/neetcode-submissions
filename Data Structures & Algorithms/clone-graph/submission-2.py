"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


"""
new node = use hash map to check whether the node exists, return the newly copied node

"""

class Solution:

    

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {} # key: val -> Node of the copy w that value


        def dfs(node) -> Optional['Node']:
            if not node:
                return None

            if node in old_to_new:
                return old_to_new[node]

            new_copied = Node(node.val)
            old_to_new[node] = new_copied

            for neighbor in node.neighbors:
                copied_neighbor = dfs(neighbor)
                new_copied.neighbors.append(copied_neighbor)

            return new_copied


        return dfs(node)

        

        # copy_Node

        # always thinking abotu having helper dfs?
        # 
        # def dfs()

        