class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # what if the nums has only positive values? canw we break out look early at the very first condition where sum breaks and stop the move on to the next i? would tham mean that time complexity would be a lot better than if there were both positive and negative numbers?
        
        # res = 0
        # for i in range(len(nums)):
        #     currSum = 0
        #     for j in range(i, len(nums)):
        #         currSum += nums[j]
        #         if currSum == k:
        #             res += 1

        # return res

        # efficient solution:
        """
        keep track of another array with 0s and travers nums using i:
        in prefi = numsi  prefif - 1

        pref = [2, 1, 2, 4]
        pref = [2, ] 
        if pref i-1 + numsi == k count and update prei

        if prefi == k we count++

        the actual solution after looking at neetcode is so unintuituve bro

        """
        preMap = defaultdict(int) # key: prefix sum -> val: counts that add to that sum
        preMap[0] = 1
        res = 0 # returning
        currSum = 0 # we will be addin all the values seen till now.. do currSum - k = x
        # x means we should get rid of a subarr that adds up to x to

        for n in nums:
            currSum += n
            rem = currSum - k
            if rem in preMap:
                res += preMap[rem]
            preMap[currSum] += 1

        return res











