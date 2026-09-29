class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        added = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in added:
                return [added[difference], i]

            added[nums[i]] = i
