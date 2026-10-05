"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
            nighbors: List[Node]
"""

from typing import Optional



class Solution:
    # time: is oh of n (number of nodes ) * number of edges
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.seen = set()
        if not node:
            return None
        if node in self.seen:
            return None

        copied_node = Node(node.val)
        self.seen.add(node)

        for neighbor in node.neighbors:
            copied_neighbor = self.cloneGraph(neighbor) 
            if copied_neighbor:
                copied_node.neighbors.append(copied_neighbor)
            

        return copied_node


# node: Node(val=1, neighbors=[Node(val=2, neighbors), Node(val=4, neighbors)])
# return copied_node the exact same thing but newly creates


        
        