class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        #check each square, then vertic, then horiz

        seen = set()
        # starting w horiz
        for row in range(9):
            seen.clear()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    return False
        
        # check vert
        seen.clear()
        for col in range(9):
            seen.clear()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    return False


        i = 0
        j = 0
        # while j < 9:
        #     i = 0
        #     while i < 9:
        #         seen.clear()
        #         for col in range(j, j+3):
                    
        #             for row in range(i, i+3):
        #                 if board[row][col] == ".":
        #                     continue
        #                 if board[row][col] not in seen:
        #                     seen.add(board[row][col])
        #                 else:
        #                     return False
        #                 i += 3
        #         j += 3

        while j < 9:
            i = 0
            while i < 9:
                seen.clear()
                for col in range (j, j + 3):
                    for row in range(i, i+ 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] not in seen:
                            seen.add(board[row][col])
                        else:
                            return False
                i = i+3    
            j = j+3

        return True
