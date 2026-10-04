class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """
        


        """
        rows = len(grid)
        cols = len(grid[0])
        #pos[row][col]

        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        seen = set()
        res = 0

        def dfs(grid, row, col) -> None: # determine how big the island is using the directions vicinity and populate the places we've seen in the set
            #nonlocal seen is this necessary??

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return None

            if (row, col) in seen or grid[row][col] == "0":
                return None
            
            seen.add((row, col))

            for dx, dy in directions:
                dfs(grid, row+dx, col+dy)

            """
            check if out of bounds
            check if already visited or water
            
            for directions:
                add to seen
                dfs(new directions)

            """


            # seen.add((row, col))

            # for dx, dy in directions:
            #     x, y = row + dx, col + dy

            #     if x < 0 or x >= cols:  #dx > cols - 1 is the same?
            #         return None
            #     if y >= rows or y < 0:
            #         return None
                
            #     if grid[x][y] == "1":
            #         dfs(grid, x, y)


                
            # if grid[row][col] in seen:
            #     return 0
            # if grid[row][col] == 0:
            #     return 0
            # # if grid[row][col] == 1 and tuple(row, col) not in seen:
            # else:
            #     seen.add(tuple(row, col))
            #     # res += 1
            #     for dx, xy in directions:
            #         x, y = row+dx, col+dy
            #         if x < 0 or x >= cols:  #dx > cols - 1 is the same?
            #             return 0
            #         if y >= rows or y < 0:
            #             return 0
                    
            #         check = dfs(grid[row][col])

            # return 1
            

        # have i discovered a new eligibale island? 
            # -yes: cool let's mark all the sections 1 in that island and it's borders water
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:

                    res += 1
                    dfs(grid, row, col)
        
        return res
