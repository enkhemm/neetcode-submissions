class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        is to rey and sum all the values at odd indexes and then sum all the vcalues as even indexexs, then csompare adn return the max this wil be 2n - n
        other way: start from the very first index then don't count the node immediately after it but exoplore all the instance ither than that! -- needs recursion?


        """
        # [0, 1, 2, 3] -even:  0, 4e;  1 - 4e
        # [0, 1, 2] - odd:  0, 2e - error;   1- 3e


        # failed for =[2,1,1,2] that complicates it because now we have to l
        # sum_even, sum_odd = 0, 0
        # for i in range(0, len(nums) , 2):
        #     sum_even += nums[i]

        # for i in range(1, len(nums), 2):
        #     sum_odd += nums[i]

        # return max(sum_even, sum_odd)

        # # attempting iterative solution..
        # res, curr_sum = 0, 0
        # while not the end of nums:
        #     for i in range(len(nums)):
        #         curr_sum = nums[i]
        #         for j in range(i + 2, len(nums))

        # # attempting recursive solution

        # res = 0
        # for i in range(len(nums)):




        # return max(nums[i] + dfs(i + 2), dfs(i + 1))

        # def help(prev, n):
        #     if n is adjacent then return?


        # help(0)
        # return max





        def dfs(i):
            if i > len(nums) - 1:
                return 0

            return max(dfs(i + 1), nums[i] + dfs(i + 2))

        return dfs(0)










