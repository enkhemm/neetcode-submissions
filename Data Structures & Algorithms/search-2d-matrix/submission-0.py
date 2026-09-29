class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row most likely to have target
        
        rows = len(matrix)
        cols = len(matrix[0])
        bestR = rows - 1


        for i in range(rows - 1): #0-5
            if target == matrix[i][0]:
                return True

            # found best row
            if target > matrix[i][0] and target < matrix[i+1][0]:
                bestR = i
                break

            # target pretty big assign to 
            # bestR = rows -1

        print(bestR)
        # bs thru that row
        l = 0
        r = len(matrix[bestR]) - 1

       

        while l <= r:
            mid = (r+l) // 2
            if matrix[bestR][mid] == target:
                return True

            elif matrix[bestR][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    
    

    
    # def maxTickets(tickets: List[int]) -> int:

    #     # compare i to the i + 1

    #     sorted_arr = sorted(tickets)
    #     #          lr
    #     # [2,3,3,4,14,15]
    #     l = 0
    #     max_len = 0
    #     for r in range(1, len(tickets) - 1):
    #         if 


