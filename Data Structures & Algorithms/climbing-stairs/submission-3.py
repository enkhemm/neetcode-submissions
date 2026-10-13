class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 1

        # if n < 0:
        #     return 0

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # time complexixty: O(2^n)
        # def dfs (i):
        #     if i >= n:
        #         return i==n
        #     return dfs(i+1) + dfs( i+2)

        # return dfs(0)

        # key: steps left, val: how many ways


        # there 2 branches need to explore 

        memo = {}
        res = 0

        def backtrack(remain):

            if remain == 0:
                return 1
            if remain < 0:
                return 0

            if remain in memo:
                return memo[remain]

            memo[remain] = backtrack(remain - 1) + backtrack(remain - 2)
            return memo[remain]
                
        return backtrack(n)





        