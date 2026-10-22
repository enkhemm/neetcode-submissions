class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        adj = defaultdict(list)
        rows = len(heights)
        cols = len(heights[0])

        # Build directed adjacency list
        for r in range(rows):
            for c in range(cols):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if heights[nr][nc] <= heights[r][c]:
                        adj[(r, c)].append((nr, nc))

        def dfs_p(r, c):
            if r == 0 or c == 0:
                return True

            visited.add((r, c))

            for nr, nc in adj[(r, c)]:
                if (nr, nc) not in visited:
                    if dfs_p(nr, nc):
                        return True

            return False

        def dfs_a(r, c):
            if r == rows - 1 or c == cols - 1:
                return True

            visited.add((r, c))

            for nr, nc in adj[(r, c)]:
                if (nr, nc) not in visited:
                    if dfs_a(nr, nc):
                        return True

            return False

        res = []

        for r in range(rows):
            for c in range(cols):
                visited = set()
                is_P = dfs_p(r, c)

                visited = set()
                is_A = dfs_a(r, c)

                if is_P and is_A:
                    res.append([r, c])

        return res
 
        
        
        
        # dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # adj = defaultdict(list)
        # rows = len(heights)
        # cols = len(heights[0])

        # # to get the valid neighbors of node
        # for r, c in heights:
        #     for dr, dc in dirs:
        #         new_dr = r+dr
        #         new_dc = c + dc
        #         if new_dr < 0 or new_dr > rows - 1 or new_dc < 0 or new_dc > cols:
        #             continue
        #         if heights[new_dr][new_dc] <= height[r][c]:
        #             adj[(r, c)].append([new_dr, new_dc])
        

        # def dfs_p(r, c):
        #     nonlocal visted
        #     if r == 0 or c == 0:
        #         return True
        #     if (r, c) not in visited: 
        #         visited.add((r, c))

        #     for new_r, new_c in adj[(r, c)]:
        #         answer = visited.add((r, c))
        #         return True if answer
            
        #     return False
            
        # def dfs_a((r, c)):
        #     nonlocal visted
        #     if r == rows -1 or c == cols -1:
        #         return True

        #     if (r, c) in visited:



        #     for new_r, new_c in adj[(r, c)]:
        #         if (r, c) not in visited:
        #             answe = visited.add((r, c))
        #             return True if answer

        

        # res = []
        # for r in range(rows):

        #     for c in range(cols):
        #         visited = set()
        #         is_P = dfs_p(r, c)
        #         visited = set()
        #         is_A = dfs_a(r, c)
        #         if is_P and is_A:
        #             res.append([r, c])

        # return res






        