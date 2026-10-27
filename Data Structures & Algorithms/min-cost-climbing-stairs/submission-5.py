class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # memo = {}

        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     memo[i] = min(cost[i] + dfs(i+1), cost[i] + dfs(i + 2))
            
        #     return memo[i]

        # return min(dfs(0), dfs(1))
        # return dfs(0)

        # [10, 45, 30, 1] [0, 0]
        # 0    1   2   3   4  5

        cost.extend([0, 0])

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        
        return min(cost[1], cost[0])


