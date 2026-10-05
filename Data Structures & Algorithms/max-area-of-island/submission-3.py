class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time complexity: O(m*n)
        directions = [ (0, 1), (1,0), (0, -1), (-1, 0)]
        seen = set()
        res = 0 # maxArea

        rows = len(grid)
        cols = len(grid[0])
        
        # finds the area of the isalnd as well as populates the seen set with all the connected 1s
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0
            
            if grid[row][col] == 1 and (row, col) in seen:
                return 0


            # new land we haven’t seen:
            seen.add((row, col))
            res = 0

            for dx, dy in directions:
                res += dfs(row + dx, col + dy)
            return 1 + res

            # WHAT I HAD BEFORE BUT THEN FIXED:
            # for dx, dy in directions:
            #     return 1 + dfs(row + dx, col + dy)
            # what it does is: explore first direction only and then immediately leave the dfs..
                

        # row and col are indexes
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    area = dfs(row, col)
                    res = max(res, area)

                    
        return res
        