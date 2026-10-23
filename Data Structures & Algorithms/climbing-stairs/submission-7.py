class Solution:
    def climbStairs(self, n: int) -> int:

        # self.memo = {}

        # if n in self.memo:
        #     return memo[n]
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n  == 2:
        #     return 2
        
        # self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # return self.memo[n]

        memo = {}
        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n  == 2:
                return 2
            
            if n in memo:
                return memo[n]

            memo[n] = dfs(n-1) + dfs(n - 2)
            return memo[n]

        return dfs(n)