class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1

        result = []
        k = 0
        while i < j:

            for k in range(len(nums)):
                if k == i or k == j: continue

                if (nums[i] + nums[j] + nums[k] == 0):
                    result.append([i, j, k])

            j -= 1

        while i < j:

            for k in range(len(nums)):
                if k == i or k == j: continue

                if (nums[i] + nums[j] + nums[k] == 0):
                    result.append([i, j, k])

            i += 1
        
        return result
        