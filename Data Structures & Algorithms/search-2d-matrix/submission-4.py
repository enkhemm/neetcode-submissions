class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row most likely to have target
        
        # rows = len(matrix)
        # cols = len(matrix[0])
        # bestR = rows - 1


        # for i in range(rows - 1): #0-5
        #     if target == matrix[i][0]:
        #         return True

        #     # found best row
        #     if target > matrix[i][0] and target < matrix[i+1][0]:
        #         bestR = i
        #         break

        #     # target pretty big assign to 
        #     # bestR = rows -1

        # print(bestR)
        # # bs thru that row
        # l = 0
        # r = len(matrix[bestR]) - 1

       

        # while l <= r:
        #     mid = (r+l) // 2
        #     if matrix[bestR][mid] == target:
        #         return True

        #     elif matrix[bestR][mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1

        # return False


        # after solution:

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            

            row = (top+bottom) // 2
            # if target == matrix[mid][0]:
            #     return True
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if top > bottom:
            return False

        # row = mid

        l = 0
        r = cols - 1

        while l <= r:
            m = (r+l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m-1

            else:
                return True

        return False






