class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        l, r = 0, len(nums) - 1 # indexes

        while l < r:
            curr = nums[l] + nums[r]
            if curr == target:
                return [l, r]
            if curr > target:
                r -= 1
            else:
                l += 1
        
        return []

