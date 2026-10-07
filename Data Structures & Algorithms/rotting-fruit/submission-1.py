class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        fresh, minutes = 0,0
        rows, cols = len(grid), len(grid[0])
        directions = [ (0,1), (1,0), (0,-1), (-1, 0) ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r, c))
        # print(fresh)
# 2  2  0
# 0  2  0
# 0  0  1

#  q = ,  1,1

        while q and fresh > 0:
            times = len(q)
            for _ in range(times):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or 
                        grid[nr][nc] == 0):
                        continue

                    if (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            minutes += 1

        # print(fresh)

        return minutes if fresh == 0 else -1



















        