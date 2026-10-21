class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # using bfs
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        visited = set()

        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                q = deque([i])
                while q:
                    node = q.popleft()
                    visited.add(node)
                    for nei in adj[node]: 
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)


        return count





        