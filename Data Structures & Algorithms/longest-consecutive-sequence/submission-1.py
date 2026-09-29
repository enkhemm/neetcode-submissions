class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_len = 1

        # sort array
        # iterate
        # if prev - i = 1 => curr + 1
        # if double move on
        # if not compare with max len and keep the higher count
        s_nums = sorted(nums)

        curr = 1
        for i in range(len(s_nums) - 1): # 0 to len -1
            if s_nums[i+1] - s_nums[i] is 1:
                curr += 1
            elif s_nums[i] is s_nums[i+1]:
                continue
            else:
                if curr > max_len:
                    max_len = curr
                curr = 1
        if curr > max_len:
            max_len = curr


        return max_len
