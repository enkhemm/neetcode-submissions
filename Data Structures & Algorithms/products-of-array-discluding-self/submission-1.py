class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums) 
        pref, post, res = [0] * size, [0] * size, [0] * size
        
        # pref[0] = nums[0]
        # post[size-1] = nums[size-1]

        total = 1
        for i in range(size - 1):
            total *= nums[i]
            pref[i] = total        

        total = 1
        for i in range(size-1, -1, -1):
            total *= nums[i]
            post[i] = total
        
        res[0] = post[1]
        res[size - 1] = pref[size - 2]

        print(pref)
        print(post)

        for i in range(1, size - 1):
            res[i] = pref[i - 1] * post[i + 1]

        return res



        