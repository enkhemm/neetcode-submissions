class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create hashmap where key is value and value is a list of neighbors?
        # for each n 
        #     if the n is not in set increment count
        #     and call dfs on n

        nodeMap = defaultdict(list)
        for node1, node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)

        # populate the visited
        def dfs(num):
            if num in visited:
                return

            visited.add(num)
            for neighbor in nodeMap[num]:
                dfs(neighbor)


        visited = set()
        count = 0
        for num in range(n):
            if num not in visited:
                count += 1
                dfs(num)

        return count
        




        # for edge in edges:
        #     edge.sort()

        # edges.sort(key=lambda x: x[0])
        # # print(edges)
        
        
        # count = 0
        # visited = set()

        # unvisited = [1] * (n)  # nodes that are single graphs

        # # print(unvisited)
        # for fromNode, toNode in edges:
        #     if fromNode not in visited:        
        #         visited = set()
        #         count += 1
        #         # visited.add(fromNode, toNode)

        #     visited.add(fromNode)
        #     visited.add(toNode)
        #     unvisited[fromNode] = 0
        #     # print(toNode)
        #     unvisited[toNode] = 0
        
        # # print(unvisited)

        # return count + sum(unvisited)

# unvisited = 

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


for each n we build an adjecency list where map: 
    key: node, value: eachh neighbor

hashmap that has all keys: nodes, values: all the neighbors

visited = set

dfs goes as deep as possible

for each n:
    if node is not in the visited set
    we 
    we call dfs on this node



"""

