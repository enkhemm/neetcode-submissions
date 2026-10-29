class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        # pseudocode
        # map that keys key a position and value is going to be the parent the position came from in a path
        # hashset track positions we visited

        # huse a queue to keep track of layer by layers

        # visited = set()

        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        node2parent = { (0, 0): None }
        visited = set([(0,0)])
        directions = [(1,0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        q = deque([(0, 0)])

        while q:
            # reached dest?
            # explore directions
                # if condition are valid we append to q

            r, c = q.popleft()

            if r == n -1 and c == n - 1:
                path = [] 
                curr = (r, c)

                while curr is not None:
                    path.append((curr))
                    curr = node2parent[curr]

                # return path.reverse() # path[::-1]
                return len(path)


                cr, cc = r, c
                while (cr, cc) is not None:  #?
                    path.append(node2parent[(cr, cc)])
                    cr, cc = node2parent[(cr, cc)]

                return len(path)

            # neet to explore all direction
            for dr, dc in directions:
                nr, nc = r + dr, c+ dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    node2parent[(nr,nc)] = (r, c)

                    visited.add((nr, nc))
                    q.append((nr, nc))

        return -1
        