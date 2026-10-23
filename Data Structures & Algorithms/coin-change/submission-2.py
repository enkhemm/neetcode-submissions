class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount + 1] * (amount + 1)

        # dp[0] = 0
        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a - c])

        #             coin = 4
        
        # return dp[amount] if dp[amount] != amount + 1 else -1


        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            if remaining < 0:
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(remaining - coin))
                memo[remaining] = res

            return res



        res = dfs(amount)

        return res if res != float('inf') else -1


