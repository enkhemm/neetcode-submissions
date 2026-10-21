class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        for edge in edges:
            edge.sort()

        edges.sort(key=lambda x: x[0])
        
        count = 0
        visited = set()

        unvisited = [1] * (n-1)  # nodes that are single graphs
        for fromNode, toNode in edges:
            if fromNode not in visited:        
                visited = set()
                count += 1
                # visited.add(fromNode, toNode)

            visited.add(fromNode)
            visited.add(toNode)
            unvisited[fromNode] = 0
            unvisited[fromNode] = 0

        return count + sum(unvisited)

# 1,2  1,3  2,3 
# visited = 1,2,3

# 1 - 2
# \  /
#  3

# 0
"""
what is kahns algorithm?
it uses a deque and iterative search BST to determine number of connected components?

dfs - find any cycles, undirected, acyclic, DAG? 
no kahn is directed no cycle
kahn uses indegree - number of nodes connected to it..
this one no direction so no graphs
hashmap: 

i want to sort edges by the first element
we will always go deep
use a set to keep track of the current component there can be cycles! 
traverse each element fromnode and tonode in edges
if fromnode is not in set

"""

