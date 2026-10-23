class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # tabulation solution

        
        """
        dp[a] -> arraw that stores minimum coins needed to make amount
        [1, 4, 3, 5] 7
        0, inf, inf, inf, inf

        if 0 return 0
        
        iterate amount: 1 - 8
            iterate coins
                if amount >= coin:


        """

        dp = [float('inf')] * (amount + 1) # minimum coins needed to make amount
        dp[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], 1 + dp[a - coin])


        return dp[amount] if dp[amount] != float('inf') else -1