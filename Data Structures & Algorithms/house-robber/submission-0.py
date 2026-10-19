class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        is to rey and sum all the values at odd indexes and then sum all the vcalues as even indexexs, then csompare adn return the max this wil be 2n - n
        """
        # [0, 1, 2, 3] -even:  0, 4e;  1 - 4e
        # [0, 1, 2] - odd:  0, 2e - error;   1- 3e



        sum_even, sum_odd = 0, 0
        for i in range(0, len(nums) , 2):
            sum_even += nums[i]

        for i in range(1, len(nums), 2):
            sum_odd += nums[i]

        return max(sum_even, sum_odd)
