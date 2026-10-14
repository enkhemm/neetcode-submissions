class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    continue
                k = 1
                # it is 1 and potentially new big square we must investigate

                # for i in range()            
                """
                expand as much until end of rows or cols whicheverr shorter

                """
                # expand as far from starting points r,c
                while True:
                    if r + k > rows or c+k > cols:
                        break
                    all_ones = True
                    
                    # valid row col that can form a square
                    # check every row below
                    for i in range(c, c + k):
                        if matrix[r+k-1][i] == "0":
                            all_ones = False
                            break

                    # try cols
                    if all_ones:
                        for i in range(r, r + k):
                            if matrix[i][c+k-1] == "0":
                                all_ones = False
                                break

                    if not all_ones:
                        break
                    
                    res = max(res, k * k)
                    k += 1


        return res
