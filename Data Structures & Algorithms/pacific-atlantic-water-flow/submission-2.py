class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        
        # purpose: it fills the sets with all the valid nodes that water can flow from

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            visited.add((r, c))

            # check wehther the neighbors are valid.. fro dirs
            # valid: the r and c are within range, the neighbor value is more then r, c value
            # add it to visited and go to taht neighbor

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)



        pacific = set() # set of (r, c)
        atlantic = set()

        # top and bottoms
        for i in range(cols):
            dfs(0, i, pacific)
            dfs(rows - 1, i, atlantic)

        # left, right

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        res = []
        for r, c in pacific:
            if (r,c) in atlantic:
                res.append([r, c])


        return res



        
        



