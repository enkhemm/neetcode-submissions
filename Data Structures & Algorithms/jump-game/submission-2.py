class Solution:
    def canJump(self, nums: List[int]) -> bool:
        [1,2,3,0,0]

        n = len(nums)

        memo = {} # i index to wether it can reach
        def dfs(i) -> bool:
            if i >= n - 1:
                return True

            if i in memo:
                return memo[i]
            
            if nums[i] == 0:
                return False

            for j in range(1, nums[i] + 1):
                if dfs(i+j):
                    memo[i] = True
                    return True
                # res = dfs(i + j)
                # memo[i] = res
            memo[i] = False
            return memo[i]
        
        return dfs(0)
        # return memo[0]

