class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        




        #check each square, then vertic, then horiz

        seen = set()
        # starting w horiz
        for row in range(9):
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
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.add(board[row][col])
                else:
                    return False

        seen.clear()
        # each box
        # i = 0
        # j = 0
        # while i < 7:

        #     for row in range(i, i + 3):
                
        #         for col in range(j, j + 3):
        #             if board[row][col] not in seen:
        #                 seen.add(board[row][col])
        #             else:
        #                 return False
        #         j += 3
            
        #     i += 3
        
        i = 0
        j = 0

        while j < 8:
            for col in range(j, j+3):
                while i < 8:
                    for row in range (i, i + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] not in seen:
                            seen.add(board[row][col])
                        else:
                            return False
                    i += 3
            j += 3

        return True




    # def solutions(nums):
    #     ans = 0
    #     curr = 1 # how many valid subarrays end at this index, behaves like a count!
    #     for i in range(len(nums)):
    #         if i > 0:
    #             if nums[i] % 2 != nums[i-0] % 2:
    #                 current += 1

    #             else:
    #                 current = 1
    #             ans += current

        
    #     return ans