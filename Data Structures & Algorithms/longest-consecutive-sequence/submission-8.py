class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # max_len = 1

        # s_nums = sorted(nums)

        # if len(nums) == 0:
        #     return 0

        # curr = 1
        # for i in range(len(s_nums) - 1): # 0 to len -1
        #     if s_nums[i+1] - s_nums[i] == 1:
        #         curr += 1
        #     elif s_nums[i] == s_nums[i+1]:
        #         continue
        #     else:
        #         if curr > max_len:
        #             max_len = curr
        #         curr = 1
        # if curr > max_len:
        #     max_len = curr


        # return max_len


        #  Use sets!
        numSet = set(nums)

        maxLen = 0

        for n in nums:
            curr = 1
            if (n - 1) not in numSet: #are brackets necessary here?
                while (n + curr) in numSet:
                    curr += 1
                
                maxLen = max(curr, maxLen)

            
        
        return maxLen


