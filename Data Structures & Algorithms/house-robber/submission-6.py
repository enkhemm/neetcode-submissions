class Solution:
    def rob(self, nums: List[int]) -> int:


        memo = {}

        def dfs(i: int) -> int:
            if i >= len(nums): # 5 > 5
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]


        return dfs(0)
    """
    at each i there are 2 choices:
    rob i and then add rob i+2
    or rob i+1

    helper: i current position returns max that can be robbed\
        dfs(i)
        i > out or range return 0
        if i > len(nums):
            return 0

        max(nums[i] + dfs(nums[i+2]), dfs(nums[i+1]))

        [2,9,8,30,6]

        max(2+30, dfs(9))

        dfs(8) -> max(8+6, 30) -> 30
        dfs(6) -> 6 + dfs(i7) , dfs(6)
        dfs(30) -> max(30 + 0, 6) - > 30
        dfs(9) -> mx(39, dfs(8)[hint memo]) -

        memoization


    """


