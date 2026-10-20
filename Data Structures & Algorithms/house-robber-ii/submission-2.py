class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        0, 1, 2, 3

        [20,  9, 8, 3,  6]
        [10, 15, 14, 6, 6]

        memoization: recursion
        dfs(i)
        if out or range -> 0
        if i is the start of nums then we cant do connection to the last index.. dfs(i+1) -- dont do 6 -- 
        if i == 0: memo[i] = max(dfs(i+1), nums[i] + )
        orr if i == last element.. we dont add to the first element

        else 
        memo[i]
        return max(memo[0], memo[1])

        
        skip i+1
        rob i and rob i+2


        # after looking at hints.. no need to overcomplicate make as efficient as you can just do your own thingy separately and then compare
        """

        # 0 th until second to last
        memo0 = [-1] * (len(nums) - 1)
        memo1 = [-1] * len(nums)
        # check if more than 1 elements
        if len(nums) < 2:
            return nums[0]

        
        def dfs0(i):
            if i >= len(nums) - 1:
                return 0
            if memo0[i] != -1:
                return memo0[i]

            memo0[i] = max(nums[i] + dfs0(i+2), dfs0(i+1))
            return memo0[i]

        def dfs1(i):
            if i >= len(nums):
                return 0
            if memo1[i] != -1:
                return memo1[i]

            memo1[i] = max(nums[i] + dfs1(i+2), dfs1(i+1))
            return memo1[i]


        start0 = dfs0(0)
        start1 = dfs1(1) 

        return max(start0, start1)

            
