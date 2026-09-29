class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, post, res = [], [], []
        size = len(nums) 
        # pref[0] = nums[0]
        # post[size-1] = nums[size-1]

        total = 0
        for i in range(size):
            total *= nums[i]
            pref = nums[i]

        print(pref)

        total = 0
        for i in range(size-1, -1, -1):
            total *= nums[i]
            post = nums[i]
        
        res[0] = post[1]
        res[size - 1] = pref[size - 2]

        for i in range(1, size - 1):
            res[i] = pref[i - 1] * post[i + 1]

        return res



        