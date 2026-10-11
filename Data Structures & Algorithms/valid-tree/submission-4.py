class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 0:
            return True
        
        adj = defaultdict(set)
        visited = set()
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)


	#dfs on 1st element false if there is a cycle, no keeping track of prev, just   remove from adj list!!
        def dfs(node) -> bool:
            if node in visited:
                return False
            if adj[node] == []:
                return True
            # no cycle, and has children
            visited.add(node)
            for child in adj[node]:
                adj[child].remove(node)
                if not dfs(child):
                    return False

            return True
		


        if not dfs(0):
            return False
        

        return len(visited) == n



        