class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 1

        # if n < 0:
        #     return 0

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        def dfs (i):
            if i >= n:
                return i==n
            return dfs(i+1) + dfs( i+2)

        return dfs(0)
        