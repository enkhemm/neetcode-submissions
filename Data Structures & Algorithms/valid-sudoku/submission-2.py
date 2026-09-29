class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqs = collections.defaultdict(set)
    

        for r in range(9):
            for c in range(9):

                #check vert and horizontal
                if (board[r][c] == "."):
                    continue
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in rows[r]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])

                #check squares
                if board[r][c] in sqs[(r//3, c//3)]:
                    return False
                sqs[(r//3, c//3)].add(board[r][c])
        
        return True
