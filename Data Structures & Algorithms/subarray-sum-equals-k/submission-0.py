class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # what if the nums has only positive values? canw we break out look early at the very first condition where sum breaks and stop the move on to the next i? would tham mean that time complexity would be a lot better than if there were both positive and negative numbers?

        res = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum == k:
                    res += 1

        return res
