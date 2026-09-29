class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        added = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in added:
                return [added[difference], i]

            added[nums[i]] = i


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] is target:
                    return [i, j]
