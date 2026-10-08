class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """



        """

        res, path = [], []
        curr = 0
 

        def dfs(ind, currSum, path):
            if currSum == target:
                res.append(path.copy())
                return
            
            if currSum > target or ind >= len(nums):
                return

            path.append(nums[ind])
            dfs(ind, currSum + nums[ind], path)

                
            path.pop()
            dfs(ind+1, currSum, path)


        dfs(0, 0, [])

        return res

            