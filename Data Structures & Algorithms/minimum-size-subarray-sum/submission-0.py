class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minLen = float('inf')
        
        # l = 0
        # currSum = nums[l]
        # # if currSum >= target:
        # #     minLen += 1
        # #     return minLen
        # for r in range(l, len(nums)):
        #     if currSum < target:
        #         currSum += nums[r]
            
        #     minLen = min(minLen, r - l + 1)
        #     l += 1
        #     currSum = 0

        # return minLen

        minLen = float('inf')
        r = 0
        # currSum = 0
        for r in range(0, len(nums)):
            currSum = 0
            for l in range(r, len(nums)):
                
                currSum += nums[l]

                if currSum >= target:
                    minLen = min(minLen, l - r + 1)
                    # currSum = 0
                    break # need to find a way to restart loop but starting from r until end again

        return 0 if minLen == float('inf') else minLen





