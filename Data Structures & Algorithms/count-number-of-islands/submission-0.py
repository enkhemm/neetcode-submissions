class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        # Inside a loop we write the if statement for do something! something that is outside the norm, as in do these tedious jobs
        if not grid:
            return 0

        visited = set() # contains tuple of r and c of the position
        directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        count = 0
        rows = len(grid)
        cols = len(grid[0])


        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in directions: # List of 2 ints
                    newR = r + dr
                    newC = c + dc

                    # checing whether this new pos should be added to ques to perform another bfs
                    # check if new pos in row, col range, if it's 1, if it's not visited
                    if (newR in range(rows) and newC in range(cols)
                        and grid[newR][newC] == "1" and (newR, newC) not in visited):
                        q.append((newR, newC))
                        visited.add((newR, newC))
                    

        # iterate thru the grid
        for row in range(rows):
            for col in range(cols):
                # if new island not visited:
                if grid[row][col] == "1" and (row, col) not in visited:
                    count += 1
                    
                    bfs(row, col) # either 1 or 0
                    #visited.add((row, col))
                    

        return count
